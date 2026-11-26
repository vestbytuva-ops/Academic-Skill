---
name: academic-drawio
description: >-
  Lag eller rediger et diagram i draw.io eller diagrams.net. Bruk for redigerbare .drawio-filer,
  flytskjema og metodekart fra tekst, notater eller en skisse.
  Build or edit native draw.io diagrams from notes, sketches, or process descriptions.
---

# Redigerbare draw.io-diagrammer

1. Finn diagrammets mål, målgruppe og retning. Trekk ut trinn, aktører og forbindelser fra materialet. Hold navnene korte. Merk usikre forbindelser som antakelser, og merk uleselige deler av skisser for oppfølging. Bruk språket i oppgaven.
2. Lag en oversikt over noder og piler. Bruk en handlingsfrase i hvert prosesstrinn, et spørsmål i en beslutning og tydelige vilkår på pilene som går ut. Del store arbeidsforløp i oversikt og detaljer.
3. Bruk [JSON-eksemplet](assets/kildearbeid.json) og [generatoren](scripts/make_drawio.py) for et nytt diagram på én side. Gi nodene tydelige ID-er og posisjoner. Bruk draw.io-editoren hvis oppgaven krever flere sider, lag, svømmebaner eller presis plassering av piler.
4. Når en eksisterende `.drawio`-fil skal oppdateres, arbeid fra en kopi i draw.io. Behold sider, ID-er, posisjoner, stiler og koblinger i delene brukeren vil bevare. Bruk sidens XML-kilde når en liten, presis endring er enklere der.
5. Åpne den ferdige `.drawio`-filen når editoren er tilgjengelig og sjekk at figurer, tekst og piler kan redigeres. Se etter klippede etiketter og piler som er vanskelige å følge. Lever den redigerbare filen og eksporter et bilde dersom brukeren trenger det.

Fra skill-mappen kan du kjøre `python scripts/make_drawio.py assets/kildearbeid.json kildearbeid.drawio`. Hvis editoren mangler, kontroller XML-strukturen og oppgi hvilken visuell kontroll som gjenstår.
