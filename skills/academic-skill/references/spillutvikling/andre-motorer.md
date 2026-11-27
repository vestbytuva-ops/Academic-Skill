# Ebitengine, Bevy, pygame, LÖVE og Defold

## Ebitengine (Go)

- Bruk `Update` til simulering og input, `Draw` til bilde og `Layout` til logisk visningsstørrelse. Legg tilstandsbytte og kollisjon i oppdateringsdelen. Bruk prosjektets tidsenhet og se at antall oppdateringer kan variere uavhengig av tegningen.
- Behold teksturer, lyd og kartdata gjennom runder hvor de gjenbrukes. Bruk prosjektets assetlasting, for eksempel `embed.FS` ved innebygde filer. Test transform eller skalering for sprite, pikseltekst, kamera og eventuell Kage-shader i samme logiske oppløsning som spillet.
- Test kart, regler og lagring med `go test` der logikken kan kjøres uten vindu. Kjør hele inngangspunktet for å kontrollere input og bilde. Ved WebAssembly, bruk Go-verktøykjedens tilhørende støtteskript og prøv bygget fra en HTTP-server. [Ebitengine-dokumentasjonen](https://ebitengine.org/en/documents/)

## Bevy (Rust)

- Les Bevy-versjon og Cargo-funksjoner. Modellér data som komponenter eller ressurser, og legg systemer i passende schedules. Fest spillfaser til prosjektets state-oppsett. Bruk `FixedUpdate` der simuleringen krever fast steg. Gjør avhengigheter i systemrekkefølge eksplisitte når de påvirker resultatet.
- Ta høyde for når `Commands` blir anvendt og når ressurser blir ferdiglastet. Hold eierforhold for scener, objekter og handles tydelige. Sjekk at ny runde oppretter riktig antall entiteter og at utgåtte entiteter fjernes. Bruk tester med liten `App` der verden kan oppdateres uten renderer. [Bevy-eksempler](https://bevy.org/examples/) · [API-referansen](https://docs.rs/bevy/)

## pygame og pygame-ce (Python)

- Bruk ett sted for å hente hendelser, ett for spilltilstand og ett for å tegne og vise resultatet. Regn om millisekunder fra klokka til sekunder hvis spillreglene bruker sekunder. La programmet behandle avslutningshendelser også når scenen står på pause.
- Last og konverter bilder etter at visningsformatet er satt. Oppdater kollisjonsrektangelet fra posisjonen, særlig hvis posisjonen lagres med desimaler. Kjør regeltester med faste inndata og kort løkke. Bruk SDLs testoppsett der det passer, og sjekk vindu, lyd og kontroll i en ordinær kjøring. [pygame](https://www.pygame.org/docs/) · [pygame-ce](https://pyga.me/docs/)

## LÖVE (Lua)

- Følg prosjektets `love.load`, `love.update(dt)` og `love.draw`. Bruk hendelser for enkelttrykk og tilstand for taster som holdes. Bruk et avgrenset antall faste steg per oppdatering hvis fysikken bruker en akkumulator. Tegn verden med valgt kamera og hold HUD i skjermkoordinater.
- For skarp pikselgrafikk, prøv en logisk canvas som skaleres i heltallssteg med passende filtrering. Test omstart, vindusendring og at pakket `.love` har `main.lua` på forventet sted. [LÖVE-wikien](https://love2d.org/wiki/Main_Page)

## Defold (Lua)

- Finn bootstrap collection og input bindings i `game.project`. Bruk game objects og components med hver sin oppgave. Sjekk at skriptet har inndatafokus når det skal motta handlinger. Bruk `msg.post` og `on_message` med kjente mottakere. La `.gui_script` håndtere grensesnittet.
- Bruk en factory til oppretting av game objects og collection factory når flere objekter må instansieres sammen. Kontroller relative komponentadresser, meldinger og opprydding når en collection fjernes. Kjør editorprosjektet. Prøv Bob eller prosjektets etablerte byggjobb ved pakking og start den faktiske bundelen. [Defold-manualene](https://defold.com/manuals/introduction/)
