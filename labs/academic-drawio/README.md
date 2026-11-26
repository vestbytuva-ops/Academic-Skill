# Academic Draw.io

Lag en redigerbar `.drawio`-fil til for eksempel en rapport, et metodekapittel eller en presentasjon. Du kan starte fra notater, en skisse eller et diagram du allerede har.

> Bruk $academic-drawio. Gjør metodedelen min om til et redigerbart flytskjema. Vis hva som skjer når en kilde må sjekkes nærmere.

## Kjør eksemplet

Kjør fra denne mappen med Python 3.10 eller nyere og åpne resultatet i draw.io eller diagrams.net.

```sh
python scripts/make_drawio.py assets/kildearbeid.json kildearbeid.drawio
```

Bruk [eksempelmodellen](assets/kildearbeid.json) som utgangspunkt. Hver node har en unik `id`, en `label` og koordinatene `x` og `y`. `kind` kan være `process`, `decision` eller `terminal` og er valgfri. Standardstørrelsen er 180 × 64, og `width` og `height` kan tilpasses. En pil har `from` og `to` med nodenes ID-er og kan ha en `label`. Velg et nytt filnavn når du genererer en ny versjon.

I draw.io kan du flytte figurer, rette pilene og eksportere PNG, SVG eller PDF. Bruk editoren når du vil videreutvikle et eksisterende diagram. [SKILL.md](SKILL.md) · [Draw.ios filformat](https://www.drawio.com/docs/reference/file-format/)

Arbeidsmåten fra tekst til redigerbare diagrammer er inspirert av [Agents365 drawio-skill](https://github.com/Agents365-ai/drawio-skill).
