# Godot

Les `project.godot`, scenen som bruker funksjonen, og aktuelle skript eller ressurser. Følg prosjektets språk og motorversjon. Et Godot-prosjekt med C# trenger Godot sin .NET-editor og en kompatibel SDK. Sjekk støtte for valgt eksportmål med den motorversjonen.

## Scener, data og GDScript eller C#

Gi hver gjenbrukbar scene en tydelig oppgave og få forventninger til scenen som instansierer den. Bruk `@export` i GDScript eller `[Export]` i C# for verdier som settes i editoren. Hold definisjoner som figurdata, ferdigheter eller gjenstander i `Resource` når det passer prosjektets oppsett. Opprett egen tilstand per instans for verdier som skal endres mens spillet går. Sjekk at redigering av én instans gir det resultatet som er tiltenkt for de andre som bruker samme ressurs.

Bruk signaler for hendelser som scenen som eier funksjonen kan koble til. Grupper egner seg til oppslag etter rolle. For scener som opprettes og fjernes flere ganger, sjekk at signaltilkobling og opprydding følger levetiden til både avsender og mottaker. Prøv endringen etter scenebytte og omstart. [Scener og noder](https://docs.godotengine.org/en/stable/getting_started/step_by_step/nodes_and_scenes.html) · [C#](https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp/index.html)

## Bevegelse, terreng og 3D

- I Godot 4, bruk `InputMap` til handlinger og `_physics_process(delta)` til fysikk. Sett `CharacterBody2D` eller `CharacterBody3D` sin `velocity` i enheter per sekund. `move_and_slide()` bruker fysikkstegets tid. Bruk kollisjonsresultatet for gulvtilstand og sjekk skråning, tak og overgangen mellom luft og bakken.
- Bruk et område for sensorer, et dynamisk legeme for objekter som reagerer på fysikk, og lag og masker for å avgrense hvilke objekter som kan møtes. For 3D, sjekk sceneakse, lokal kontra global transform og kollisjonsform sammen med synlig modell. Oppdater kamerafølge etter den bevegelsen kameraet skal vise.
- Følg tilemap-typen motorversjonen og prosjektet bruker. Ved `TileMapLayer`, hold terreng, dekorasjon og navigasjon i de lagene prosjektet forventer. Test skjøter og kollisjon på kartet, og bruk små endringer i eksisterende `TileSet` der fliser deles på tvers av nivåer. [CharacterBody2D](https://docs.godotengine.org/en/stable/classes/class_characterbody2d.html) · [TileMapLayer](https://docs.godotengine.org/en/stable/classes/class_tilemaplayer.html)

## UI, animasjon, lyd og shadere

Bruk `Control` og `Container` for skalerbart grensesnitt. Legg fokusrekkefølge og aktiv menykontekst der prosjektet styrer inndata. Bruk `AnimationPlayer` for tidslinjer og prosjektets `AnimationTree` hvis bevegelsen trenger blanding eller tilstander. Sjekk at animasjon og bevegelse har én definert eier for figurens posisjon.

Bruk vanlig lydspiller for meny eller musikk og posisjonell lydspiller når kilden hører hjemme i scenen. Velg riktig lydbuss. Velg `canvas_item` eller `spatial` etter hvor materialet tegnes. Test parametere, transparens og rendering med prosjektets valgte renderer. [Godot-manualen](https://docs.godotengine.org/en/stable/)

## Flerspiller, tester og eksport

Bruk prosjektets eksisterende `MultiplayerAPI`-oppsett og hold eierskap og oppretting av nettverksobjekter konsistent. Se at begge peers finner riktig scene og node, og prøv deltakelse, spillhendelse og frakobling i lokal test. [Flerspiller](https://docs.godotengine.org/en/stable/tutorials/networking/high_level_multiplayer.html)

Kjør prosjektets etablerte tester. Et headless skript som arver `SceneTree` kan avslutte med `quit(0)` ved suksess eller `quit(1)` ved feil. Bruk stien til en test som finnes i prosjektet, og importer avhengige ressurser før testen hvis oppsettet krever det. Ved eksport, sjekk `export_presets.cfg` og at riktige eksportmaler er installert. Kjør den eksporterte fila på målplattformen. [Godot på kommandolinjen](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html)
