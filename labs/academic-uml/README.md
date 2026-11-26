# Academic UML

Lag et UML-diagram til en oppgave i IT, systemutvikling eller teknisk dokumentasjon. Kildeformatet er PlantUML eller Mermaid, slik at diagrammet kan oppdateres når oppgaven eller systemet endrer seg.

> Bruk $academic-uml. Lag et sekvensdiagram som viser hvordan en elev leverer en oppgave. Vis både godkjent og ugyldig fil.

## Prøv eksemplene

| Eksempel | Hva det viser |
| --- | --- |
| [Klassediagram](assets/klassediagram.puml) | Forholdet mellom en rapport, henvisningene og kildene |
| [Sekvensdiagram](assets/innlevering-sekvens.puml) | Meldinger og to mulige utfall når en elev leverer en fil |
| [Tilstandsdiagram](assets/utkast-tilstand.mmd) | Hvordan en fagtekst går fra utkast til vurdering og ferdig tekst |

For lokal SVG- eller PNG-eksport av PlantUML, bruk Python 3.10 eller nyere, Java og en lokalt tilgjengelig PlantUML-JAR. Klassediagrammet kan kreve Graphviz. Kjør fra denne mappen og erstatt stien til JAR-filen med din egen. [Last ned PlantUML](https://plantuml.com/download)

```sh
python scripts/render_plantuml.py assets/innlevering-sekvens.puml innlevering.svg --jar /sti/til/plantuml.jar
```

Du kan også åpne `.puml`- og `.mmd`-filene i en editor med støtte for formatet. [Notasjon og flere kommandoer](references/uml-notasjon.md) · [SKILL.md](SKILL.md)

Arbeidsmåten fra beskrivelse til diagramkilde og lokal forhåndsvisning er inspirert av [UML-MCP](https://github.com/antoinebou12/uml-mcp).
