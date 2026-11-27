# Nettspill med Phaser, PixiJS eller three.js

Finn komponenten som eier canvas, lastingen av ressurser og spilløkka. Bruk versjonen som faktisk er låst. Prøv i en nettleser med prosjektets utviklingsserver og deretter med det bygde innholdet. Se etter 404, feil i konsollen, endret visningsstørrelse og feil koordinater etter skalering. Prøv første brukerhandling og det å bytte fane og komme tilbake.

## Phaser

Bruk eksisterende `Scene`-oppsett. Last ressurser i `preload`, sett opp objekter og inndata i `create`, og legg løpende sceneoppgaver i `update`. Fjern varige DOM- eller globale hendelseslyttere når scenen stenges. Start scenen på nytt to ganger og kontroller at én handling fremdeles gir én respons.

Ved Arcade Physics, velg mellom bevegelig legeme og statisk geometri og mellom `collider` og `overlap`. Bruk fysikklegemets hastighet for vanlige bevegelser. Sjekk at kropp og sprite har forventet størrelse og forskyvning etter skalering. Se at fliser har aktiverte kollisjoner der de skal. Test rask bevegelse, målområdet og omstart. [Phaser-dokumentasjonen](https://www.phaser.io/oss/docs)

## PixiJS

Start programmet slik prosjektets PixiJS-versjon krever. I v8 brukes en asynkron `Application.init` før canvas tas i bruk. Bruk `Assets`-oppsettet til å laste teksturer og scenehierarkiet til å gruppere verdenselementer og HUD. La prosjektets spilløkke eie spillregler og fysisk tilstand. Velg konsekvent enhet fra ticker, og håndter langt tidssteg etter pause eller fanebytte.

Bruk pekehendelser og koordinater i riktig container. Ved omstart, koble av lyttere og fjern objekter som tilhører scenen. Frigjør teksturer når ingen aktive scener deler dem. Prøv berøring, skalering av visningen og at scenen fortsatt virker etter flere monteringer. [PixiJS Application](https://pixijs.com/8.x/guides/components/application)

## three.js

Bruk prosjektets `Scene`, kamera og renderer. Velg ett sted som eier animasjonsløkken. Ved ny visningsstørrelse, oppdater renderstørrelse og kameraets projeksjon. Kontroller ytelse med realistisk pikselforhold. Ved input med peking, regn om fra canvasets reelle visningsrektangel.

Bruk `GLTFLoader` eller prosjektets eksisterende laster til `.gltf` og `.glb`. Følg med på lastestatus og feil. Kontroller transform, skala, utstrekning og eventuell animasjon i den faktiske scenen. Ved fysisk baserte materialer, sjekk lys og miljø og bruk riktig fargerom for fargeteksturer og datakart. Når en scene tas bort, frigjør ressurser den eier og behold delte ressurser som andre scener bruker. [three.js-manualen](https://threejs.org/manual/) · [GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html)
