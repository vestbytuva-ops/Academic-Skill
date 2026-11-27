# Fra prototype til bygg og utgivelse

## Prototype og game jam

1. Skriv spørsmålet prototypen skal besvare. «Får jeg spilleren til å forstå vekselbryteren uten tekst?» er testbart hvis banen gir et tidspunkt og en handling å observere. Velg på forhånd et kriterium for å fortsette eller justere ideen.
2. Lag en start, én omgang, et tydelig utfall og en omstart. Bruk plassholdere for deler som ikke avgjør forsøket. Hold forsøket i en egen scene eller mappe hvis det prøver noe uavhengig av hovedprosjektet. Sett bare inn målinger som forklarer forsøket, som tid fram til første bruk av bryteren.
3. Ved tidsfrist, lag et kjørbart bygg tidlig. Del resten i det som kreves for en hel runde og det som kan komme etter fullført runde. Sett av tid til omstart, eksport, test på målplattformen og kort instruks til den som skal prøve. Stryk oppgaver som ikke får plass i tidsbudsjettet.
4. Kjør en hel runde selv. Ved en spillertest, la deltakeren prøve uten ledende forklaring. Noter observasjonen og beslutningen den gir grunnlag for. Ved skoleprosjekt, vis hvilke krav dere har testet og hvilke dere bare har rukket å planlegge.

## Spilldesigndokument (GDD)

Oppdater prosjektets dokument når brukeren ber om det, eller bruk prosjektets mal hvis den finnes. Beskriv spillerens mål, kontroll, reglene som driver en runde, tilstand mellom runder og avgrensning. Gi hver viktig regel et konkret eksempel eller en kontroll. Bruk dato eller eier på uavklarte beslutninger der det hjelper teamet. For én ny mekanikk kan et kort notat med før- og ettertilstand være tilstrekkelig.

## Bygg og verifiser en kandidat

- Finn prosjektets eksportoppsett, startfil og versjonsmerking. Bruk motorens angitte verktøy og skill lokal test, kandidat og publisert versjon i rapporteringen. Noter versjon eller commit, plattform og hvor resultatet ligger.
- Start kandidaten fra en ny mappe eller fra testinstallasjonen. Gjennomfør første runde, omstart og relevant lasting av eldre spilldata. Kontroller at pakka inneholder alle nødvendige ressurser og krediteringer, og at bygget bruker rett startscene og ikon. Ved nettspill, test også samme arkiv på en lokal HTTP-server og i vertens innebygde visning når den er tilgjengelig.
- Gjør opplasting, endring av synlighet eller publisering når bestillingen omfatter den handlingen og tilgangen er avklart. Bruk etablerte utgivelseskanaler og prosjektets oppsett for hemmeligheter. Oppgi hvilke plattformkontroller som faktisk er gjennomført.

## itch.io

Skill mellom et spill for nettleseren og en nedlastbar pakke. For en nettutgave som lastes opp som ZIP, legg `index.html` og nødvendige filer der itch.io kan finne dem, med relative stier. Test oppstart, innlasting av filer, riktig bildestørrelse og lyd etter brukerhandling i den innebygde spilleren. For en nedlastbar utgave, bruk prosjektets kanal for riktig operativsystem med Butler eller nettgrensesnittet. Test at den valgte filen kan installeres eller pakkes ut og startes. Kontroller kanal, synlighet og eventuelle krav fra den aktuelle game jam-en. [Nettspill på itch.io](https://itch.io/docs/creators/html5) · [Butler](https://itch.io/docs/butler/)

## Steam

Kontroller App ID, hvilke depoter byggeoppsettet leverer, og at pakken og oppstartsvalgene dekker målplattformene. Bruk eksisterende SteamPipe-konfigurasjon. Bruk et lokalt forhåndsvisningsbygg for å kontrollere filtilordning før planlagt opplasting. Test kandidaten via en adgangsbegrenset betagren med fersk installasjon og oppdatering fra forrige versjon. Sjekk gjeldende Steamworks-krav til butikkinnhold, innholdsundersøkelse og godkjenning før butikk eller bygg gjøres offentlig. [SteamPipe](https://partner.steamgames.com/doc/sdk/uploading) · [Betagrener](https://partner.steamgames.com/doc/store/application/branches) · [Utgivelse](https://partner.steamgames.com/doc/store/releasing)
