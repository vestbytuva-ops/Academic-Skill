# Academic Pixel Art

En egen ferdighet for pikselkunst til spillprototyper, faglige illustrasjoner og presentasjoner. Den hjelper deg å velge hva som må være synlig i et lite motiv og å sjekke en animasjon rute for rute.

> Bruk $academic-pixel-art. Lag et 32 × 32-ikon av mikroskopet fra bildet mitt. Bruk åtte farger og behold gjennomsiktig bakgrunn.

## Prøv verktøyet

Med Python 3.10 eller nyere kan du kjøre fra denne mappen. Bruk et lokalt bilde som `referanse.png`. For et gjennomsiktig ikon må bildet ha gjennomsiktighet rundt motivet.

```sh
python -m pip install "Pillow>=10"
python scripts/pixel_art.py sprite referanse.png ikon.png --width 32 --height 32 --colors 8
```

Har du ferdige bilderuter, kan samme verktøy lage et PNG-spriteark og en GIF-løkke. [Kommandoer og arbeidsmåte](references/pikselkunst.md) · [SKILL.md](SKILL.md)

Arbeidsmåten fra referansebilde til kontrollerte bilderuter er inspirert av [Codixel](https://github.com/mankidev/codixel).
