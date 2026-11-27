"""Render one standalone PlantUML diagram to SVG or PNG with a local JAR."""
import argparse
from pathlib import Path
import re
import subprocess


def render(source, jar, image_format):
    markers = re.findall(r"(?im)^[ \t]*(@(?:start|end)\w+)\b", source)
    if [marker.lower() for marker in markers] != ["@startuml", "@enduml"]:
        raise ValueError("Kildefilen må inneholde én @startuml-blokk med @enduml.")
    result = subprocess.run(
        ["java", "-Djava.awt.headless=true", "-DPLANTUML_SECURITY_PROFILE=SANDBOX",
         "-jar", str(jar), "-pipe", "-charset", "UTF-8", "-nometadata", f"-t{image_format}"],
        input=source.encode("utf-8"), capture_output=True, check=False,
    )
    if result.returncode or not result.stdout:
        error = result.stderr.decode("utf-8", errors="replace").strip()
        raise ValueError(error or f"PlantUML ga ingen figur. Returkode: {result.returncode}.")
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--jar", type=Path, required=True)
    args = parser.parse_args()
    image_format = args.output.suffix.lower().removeprefix(".")
    if image_format not in {"svg", "png"}:
        parser.error("Utfilen må ha endelsen .svg eller .png.")
    if not args.jar.is_file():
        parser.error(f"Fant ingen PlantUML-JAR på {args.jar}.")
    try:
        data = render(args.source.read_text(encoding="utf-8-sig"), args.jar, image_format)
        with args.output.open("xb") as output:
            output.write(data)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
