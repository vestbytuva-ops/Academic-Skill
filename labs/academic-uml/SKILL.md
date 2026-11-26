---
name: academic-uml
description: >-
  Modellér et system med UML i PlantUML eller Mermaid. Bruk for klassediagram, sekvensdiagram,
  tilstandsdiagram, aktivitetsdiagram og brukstilfeller i en oppgave eller systembeskrivelse.
  Create, check, and render editable UML diagram source for coursework or technical documentation.
---

# UML for faglige og tekniske oppgaver

1. Avgrens systemet og avklar hva diagrammet skal vise. Ta modellens begreper og relasjoner fra oppgaveteksten, koden eller notatene. Bruk språket i oppgaven og oppgi antakelser som påvirker modellen.
2. Velg UML-type fra [notasjonsveiledningen](references/uml-notasjon.md). Bruk én visning per spørsmål. Ved et sekvensdiagram er spørsmålet for eksempel hvem som gjør hva og i hvilken rekkefølge.
3. Bruk PlantUML når oppgaven krever UML-notasjon som brukstilfeller eller aktivitetsdiagram. Bruk Mermaid for klassediagram, sekvensdiagram eller tilstandsdiagram som skal vises direkte i Markdown der den støttes. Følg formatet oppgaven eller brukeren angir.
4. Skriv en redigerbar `.puml`- eller `.mmd`-fil. Bruk [klassediagrammet](assets/klassediagram.puml), [innleveringssekvensen](assets/innlevering-sekvens.puml) eller [tilstandsdiagrammet](assets/utkast-tilstand.mmd) som syntakseksempel.
5. Kontroller navn, pilretning, multiplisitet eller rekkefølge mot oppgaven. Bruk [lokal PlantUML-eksport](scripts/render_plantuml.py) hvis brukeren trenger SVG eller PNG og Java og PlantUML er tilgjengelig. Vis Mermaid i en kompatibel forhåndsvisning. Vis kildefilen når en renderer mangler, og si om figuren ble kontrollert visuelt.
