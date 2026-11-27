# Finn spillmotoren og den faktiske prosjektversjonen

Ta utgangspunkt i mappen, scenen eller filen brukeren spør om. I et repo med flere demoer kan hver demo ha sin egen motor. Bekreft at inngangspunktet for spillet bruker avhengigheten. En `.csproj` alene identifiserer ingen motor, og Lua-kode kan tilhøre både Defold, LÖVE og andre verktøy.

| Motor eller rammeverk | Spor i prosjektet | Versjonsgrunnlag | Veiledning |
| --- | --- | --- | --- |
| Godot | `project.godot` og scener som `.tscn` | Funksjonstaggene i prosjektfilen og den avtalte eller installerte editoren | [Godot](godot.md) |
| Unity | `Assets/` og `ProjectSettings/ProjectVersion.txt` | Editorversjonen i samme fil og pakkene i `Packages/packages-lock.json` | [Unity](unity-og-unreal.md#unity) |
| Unreal Engine | `.uproject`, ofte sammen med `Config/` og `Content/` | `EngineAssociation`, prosjektets oppsett og installert editor | [Unreal Engine](unity-og-unreal.md#unreal-engine) |
| Phaser | `phaser` i `package.json` og en Phaser-instans i spillets oppstart | Låsefilen i pakken som starter spillet | [Nettspill](nettspill.md#phaser) |
| PixiJS | `pixi.js` og bruk av PixiJS sin scene eller renderer i spillkoden | Låsefilen i spillpakken | [Nettspill](nettspill.md#pixijs) |
| three.js | `three` importert i koden som oppretter 3D-scenen | Låsefilen i spillpakken | [Nettspill](nettspill.md#threejs) |
| Roblox | `.rbxl` / `.rbxlx`, åpent Roblox Studio-prosjekt eller en Rojo-prosjektfil med Roblox-tre | Studio og gjeldende Creator Hub, samt prosjektets verktøy- og pakkelås | [Roblox](roblox.md) |
| Bevy | `bevy` i `Cargo.toml` og et `App`-inngangspunkt | `Cargo.lock` og eventuelle funksjonsflagg | [Bevy](andre-motorer.md#bevy-rust) |
| Ebitengine | Go-kode som importerer `github.com/hajimehoshi/ebiten/v2` | `go.mod`, eventuelle `replace`-innslag og `go.work` | [Ebitengine](andre-motorer.md#ebitengine-go) |
| pygame eller pygame-ce | `import pygame` i spillkoden | Python-avhengigheter og valgt miljø. Begge distribusjonene bruker importnavnet `pygame`. | [pygame](andre-motorer.md#pygame-og-pygame-ce-python) |
| LÖVE | `conf.lua` eller en `main.lua` som bruker `love.*` | Oppgitt LÖVE-versjon og installert runtime | [LÖVE](andre-motorer.md#löve-lua) |
| Defold | `game.project`, `.collection` og `.script` | Editor- eller Bob-versjonen prosjektet bygger med | [Defold](andre-motorer.md#defold-lua) |

Hvis Phaser, PixiJS og three.js ligger i samme låsefil, følg importene i scenen du skal endre. Ved Godot med C#, bruk Godot-ruten selv når prosjektet har en `.sln`. For egen eller ukjent motor, les prosjektets eksempler, bygginstruksjoner og lokale API-er. Bruk de motoruavhengige spillreferansene for selve problemet.

Bruk dokumentasjon for versjonen prosjektet har. Sjekk særlig større versjonsskifter, valgfrie pakker, renderpipeline og forskjeller mellom editor og eksport. Behandle en motoroppgradering som en egen endring hvis brukeren ber om den.
