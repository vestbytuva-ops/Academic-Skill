# Visuelle ferdigheter

Alle tre arbeidsmåtene er tilgjengelige via `academic-skill`. Prototypene her kan også installeres hver for seg. Veiledningen er skrevet på bokmål, og ferdighetene kan svare på norsk og engelsk. [Bruk dem via hovedskillen](../skills/academic-skill/references/visuelle-arbeidsmater.md)

| Ferdighet | Hva du kan lage | Lokal kjøring |
| --- | --- | --- |
| [Academic Pixel Art](academic-pixel-art/README.md) | Ikoner og sprites fra referansebilder, PNG-spriteark og GIF-løkker | Python og Pillow |
| [Academic Draw.io](academic-drawio/README.md) | Redigerbare flytskjema og metodekart i `.drawio` | Python. Åpne gjerne resultatet i draw.io. |
| [Academic UML](academic-uml/README.md) | Diagramkilde i PlantUML eller Mermaid, med lokal SVG- og PNG-eksport for PlantUML | Java og PlantUML-JAR ved bildeeksport med Python |

## Prøv én ferdighet i Codex

Kjør fra roten av en lokal utsjekk med Node.js og npm. Dette eksemplet kopierer Academic Draw.io til Codex-ferdighetene for prosjektet.

```sh
npx skills add ./labs/academic-drawio --skill academic-drawio -a codex --copy -y
```

Velg `$academic-drawio` i en ny Codex-chat. Bytt begge forekomstene av `academic-drawio` i kommandoen hvis du vil prøve `academic-pixel-art` eller `academic-uml`. I andre klienter som støtter Agent Skills kan du bruke hele mappen til den ferdigheten du vil legge til.

Byggeskriptet synkroniserer verktøyene og eksempelfilene herfra til den ordinære installasjonen. Kjør `python tools/build.py` fra prosjektroten etter en endring i en delt fil. [Bygging og testing](../README.md#build-and-validate)
