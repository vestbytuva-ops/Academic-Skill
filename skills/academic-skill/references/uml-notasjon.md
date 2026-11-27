# Velg UML-diagram

| Spørsmål | Velg | Kontroller |
| --- | --- | --- |
| Hvilke begreper eller klasser inngår, og hvordan henger de sammen? | Klassediagram | Les multiplisiteten ved begge ender. Bruk komposisjon der delen tilhører helheten og følger livsløpet dens. |
| Hva skjer når noen utfører én bestemt handling? | Sekvensdiagram | La tiden gå nedover. Følg meldingene, og vis viktige avvik i en `alt`-blokk. |
| Når går et objekt fra én tilstand til en annen? | Tilstandsdiagram | Navngi tilstander med status og merk overganger med hendelse og eventuelt vilkår. |
| Hvilke handlinger og valg inngår i arbeidsflyten? | Aktivitetsdiagram | Gi handlingene verb og sjekk at greinene har tydelige vilkår. |
| Hva vil hver aktør oppnå med systemet? | Brukstilfellediagram | Plasser systemets brukstilfeller innenfor systemgrensen og aktørene utenfor. |

I et klassediagram for kildebruk leses `Henvisning "0..*" --> "1" Kilde` slik at én henvisning viser til én kilde, mens én kilde kan ha null eller flere henvisninger. I et sekvensdiagram for innlevering kan godkjent og ugyldig fil være to utfall av samme validering. Hold rekkefølgen stabil for begge utfallene. I et tilstandsdiagram for en fagtekst kan `Lever` ta teksten fra `Utkast` til `Til vurdering`.

## Lokal eksport

Kjør fra skill-mappen. PlantUML-verktøyet leser en selvstendig `@startuml`-blokk og velger bildeformat fra endelsen på utfilen. Sett inn stien til din PlantUML-JAR. Har du Mermaid i Markdown-editoren, kan du lime inn innholdet fra `.mmd`-filen i en kodeblokk merket `mermaid`. Med Mermaid CLI kan du også eksportere den lokalt.

```sh
python scripts/render_plantuml.py assets/klassediagram.puml klassediagram.svg --jar /sti/til/plantuml.jar
mmdc -i assets/utkast-tilstand.mmd -o utkast-tilstand.svg
```

[PlantUML-notasjon](https://plantuml.com/) · [Mermaid-notasjon](https://mermaid.js.org/intro/)
