"""Prepare pixel sprites, sheets and animation previews from local images."""
import argparse
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps


def open_image(path):
    with Image.open(path) as image:
        return ImageOps.exif_transpose(image).convert("RGBA")


def sprite(image, width, height, colors):
    """Fit the subject while keeping transparent pixels out of the palette."""
    scale = min(width / image.width, height / image.height)
    size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    method = Image.Resampling.BOX if scale < 1 else Image.Resampling.NEAREST
    fitted = image.resize(size, method)
    pixels = fitted.load()
    positions = [
        (x, y) for y in range(fitted.height) for x in range(fitted.width)
        if pixels[x, y][3] >= 128
    ]
    canvas = Image.new("RGBA", (width, height))
    if not positions:
        return canvas

    sample = Image.new("RGB", (len(positions), 1))
    sample.putdata([pixels[position][:3] for position in positions])
    colored = sample.quantize(colors=colors, dither=Image.Dither.NONE).convert("RGB")
    palette_pixels = colored.load()
    canvas_pixels = canvas.load()
    left, top = (width - fitted.width) // 2, (height - fitted.height) // 2
    for index, (x, y) in enumerate(positions):
        canvas_pixels[left + x, top + y] = (*palette_pixels[index, 0], 255)
    return canvas


def sheet(frames):
    width, height = frames[0].size
    combined = Image.new("RGBA", (width * len(frames), height))
    for index, frame in enumerate(frames):
        combined.paste(frame, (index * width, 0))
    return combined


def gif_frame(image, shared_palette):
    """Use the animation palette and reserve index 255 for transparency."""
    indexed = image.convert("RGB").quantize(palette=shared_palette, dither=Image.Dither.NONE)
    palette = indexed.getpalette()
    indexed.putpalette(palette + [0] * (768 - len(palette)))
    transparent = image.getchannel("A").point(lambda alpha: 255 if alpha < 128 else 0)
    indexed.paste(255, (0, 0), transparent)
    return indexed


def positive_int(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("Bruk et positivt heltall.")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    convert = commands.add_parser("sprite", help="Lag én PNG-sprite fra et bilde.")
    convert.add_argument("source", type=Path)
    convert.add_argument("output", type=Path)
    convert.add_argument("--width", type=positive_int, required=True)
    convert.add_argument("--height", type=positive_int, required=True)
    convert.add_argument("--colors", type=int, default=8, metavar="1–256")
    for name, help_text in (("sheet", "Lag et horisontalt PNG-ark."), ("gif", "Lag en GIF-løkke.")):
        combine = commands.add_parser(name, help=help_text)
        combine.add_argument("output", type=Path)
        combine.add_argument("frames", type=Path, nargs="+")
        if name == "gif":
            combine.add_argument("--duration-ms", type=int, default=120)

    args = parser.parse_args()
    suffix = ".gif" if args.command == "gif" else ".png"
    if args.output.suffix.lower() != suffix:
        parser.error(f"Utfilen må ha endelsen {suffix}.")
    try:
        with BytesIO() as encoded:
            if args.command == "sprite":
                if not 1 <= args.colors <= 256:
                    parser.error("--colors må være mellom 1 og 256.")
                sprite(open_image(args.source), args.width, args.height, args.colors).save(encoded, "PNG")
            else:
                frames = [open_image(path) for path in args.frames]
                if any(frame.size != frames[0].size for frame in frames):
                    parser.error("Alle bilderuter må ha samme bredde og høyde.")
                if args.command == "sheet":
                    sheet(frames).save(encoded, "PNG")
                else:
                    if not 10 <= args.duration_ms <= 655_350:
                        parser.error("--duration-ms må være mellom 10 og 655350.")
                    shared_palette = sheet(frames).convert("RGB").quantize(colors=255, dither=Image.Dither.NONE)
                    first, *rest = (gif_frame(frame, shared_palette) for frame in frames)
                    first.save(
                        encoded, "GIF", save_all=True, append_images=rest,
                        duration=round(args.duration_ms / 10) * 10, loop=0,
                        disposal=2, transparency=255, background=255, optimize=False,
                    )
            with args.output.open("xb") as output:
                output.write(encoded.getbuffer())
    except (OSError, ValueError, Image.DecompressionBombError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
