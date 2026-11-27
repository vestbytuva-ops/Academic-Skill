# Spillsystemer og ytelse

## Oppførsel hos spillfigurer

| Velg modell ut fra regelen | Slik avgrenser du den |
| --- | --- |
| Tilstandsmaskin for få tydelige faser | Gi hver tilstand ansvar for start, oppdatering og avslutning. Skriv betingelsen for hver overgang. |
| Atferdstre for oppgaver som kan kombineres og avbrytes | Bestem når en gren melder suksess, feil eller fortsatt arbeid. Avslutt pågående oppgaver når en gren byttes ut. |
| Nyttebasert valg for flere mulige handlinger samtidig | Sammenlign poeng på samme skala. Håndter like poeng forutsigbart, og bruk minste varighet eller terskel for å unngå raske omvalg. |

La sanseinntrykk oppdatere et lite minne før beslutningen tas. Skill valg av mål fra stifinning og selve bevegelsen. Begrens hvor ofte en ny rute beregnes. Test en figur som når målet, mister det av syne, får et nytt mål eller møter en stengt vei. Logg overganger eller vis dem i editoren når oppførselen er vanskelig å lese.

## Dialog, valg og progresjon

Bruk stabile ID-er for replikk, svarvalg og flagg. Hold vilkår som «har funnet nøkkel» og virkninger som «legg nøkkel til i inventaret» i hver sin del av dialogdataene. Skriv test som følger hver gren til et gyldig neste punkt. Hindre dobbeltbruk av belønninger når brukeren går tilbake, eller når en meny åpnes på nytt.

Se at tekstboks, tastaturfokus og kontroll virker ved lange oversettelser og med tastatur, kontroller eller berøring etter behov. Prøv hopp over tekst, historikk og gjenopptak i midten av en scene. Bruk prosjektets dialogverktøy, som Ink eller Yarn Spinner, når det ligger til grunn for innholdet.

## Lagring og gjenoppretting

1. Frys en konsistent kopi av spilltilstanden ved et definert punkt. Lagre formatversjon, stabile ressurs-ID-er, verdier og eventuelt frø. Opprett motorobjekter fra de validerte verdiene når spillet lastes.
2. Bruk prosjektets lagringsplass og skriv lokale filer til en midlertidig fil i samme mappe før en atomisk erstatning. Behold siste verifiserte lagring hvis skriving feiler. Gi automatisk lagring og manuelle plasser egne mål, og koordiner samtidige skriv til den samme plassen.
3. Parse og valider før data tas i bruk. Oppgrader eldre format trinnvis og håndter ukjent nyere format med en lesbar melding, med originalfilen i behold. Kontroller avkortet fil, tomt datasett, manglende felt og en kopi fra en eldre versjon. Test lagring, full avslutning og lasting i en ny prosess.

## Flerspiller og synkronisering

Bestem hvilken instans som eier hver del av tilstanden. La klienten sende spillerens intensjon, la serveren validere relevante vilkår og avgjøre delte resultater, og vis det bekreftede resultatet hos klientene. Ved lokal prediksjon, sammenlign med serverens bekreftelse og korriger ved avvik. Bruk motorens eksisterende nettverkslag og velg pålitelig levering der rekkefølge og hvert enkelt resultat har betydning. Bruk prosjektets lokale testoppsett med to klienter til å sjekke tilkobling, forsinkelse, gjeninnkobling, opprydding og at begge ser samme resultat av en delt handling.

## Ytelse

Mål i en repeterbar scene på relevant maskinvare. Noter oppløsning, byggevariant og antall aktive objekter. Se etter topper i bildetid i tillegg til gjennomsnittlig FPS. Bruk profilverktøy til å finne om kostnaden ligger i CPU, GPU, fysikk, minne eller innlasting. Dersom problemet oppstår etter flere runder, ta målinger før og etter omstart for å finne ressurser eller lyttere som blir igjen. Gjenta samme måling etter én endring og oppgi både resultat og kostnad for bildekvalitet eller funksjon.
