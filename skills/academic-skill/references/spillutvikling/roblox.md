# Roblox Studio og Luau

## Behold prosjektets arbeidsmåte

Avklar hvem som eier hver del av prosjektet. Med Rojo kan kode og utvalgte objekter ligge i Git mens resten av scenen eies av Studio. Se i prosjektfilen før du flytter et skript eller en forekomst. Finn eksisterende moduler, tagger, maler og fjernhendelser før du oppretter nye. Hold serverlogikk på serveren, grensesnitt hos klienten og delte definisjoner i et område begge kan lese. Sammenlign filtreet og instansene i Studio der det er mulig. [Rojo i Roblox Creator Hub](https://create.roblox.com/docs/projects/rojo)

## Utvikle og kontroller etter oppgave

| Oppgave | Framgangsmåte og kontroll |
| --- | --- |
| Luau og nye spillobjekter | Bruk prosjektets `ModuleScript`-grenser og typetilnærming. Sett skript i riktig kjøringskontekst og gjenbruk konstruksjonen prosjektet bruker for venting, opprydding og initialisering. Sjekk Output i både server og klient. |
| Figur, rigg og animasjon | Koble logikk til den aktive karakterens levetid. Hent oppdaterte referanser ved `CharacterAdded`, og fjern lyttere og effekter når figuren forsvinner. Bruk eksisterende `Animator` og animasjonsmarkører når spillrespons avhenger av et bestemt tidspunkt. Prøv død og ny spawning. |
| Fysikk | Legg krefter og constraints på riktig assembly og bruk egnede kollisjons- og spørrefiltre. Sjekk hvem som simulerer bevegelige deler i nettspill. Prøv samme interaksjon med to klienter og se at resultatet er konsistent. |
| UI | La `StarterGui` og `PlayerGui` følge prosjektets levetid for HUD og menyer. Test skalering, sikker skjermsone, tekstlengde, valg med kontroller og berøringsmål i Studio. Prøv med ny figur og etter endring av skjermretning. |
| Nettverk og delte resultater | Bruk prosjektets remotes. Valider forespørsler på serveren mot spillerens tilstand og de gjeldende spillreglene. Bakgrunnsstrømming kan gjøre en instans midlertidig utilgjengelig hos en klient. Test normal flyt, avbrutt flyt og gjeninnkobling fra to klienter. |
| DataStore | Hold lagring på serveren. Bruk stabile nøkler og formatversjon. Bruk `UpdateAsync` når en ny verdi avhenger av den forrige, og håndter feil og lagringsbudsjett. Kjør prøver mot et separat testmiljø og kontroller gjenopptak etter ny innlogging. |
| Økonomi i simulator, tycoon eller idle-spill | Modellér inntjening og kostnad per runde. Beregn saldo og kjøp på serveren. Bruk et tak for belønning utenfor spillet og dobbeltsjekk at en gjentatt bekreftelse gir én tildeling. Ved betalt innhold, sjekk gjeldende regler og bruk prosjektets etablerte bekreftelsesflyt. |

Når Studio er tilgjengelig, start med enkel spilling og gå videre til **Server & Clients** ved delte systemer. Bruk enhetsemulatoren for skjermstørrelser og prøv på en faktisk målenhet når berøring, ytelse eller nettverk er avgjørende. Oppgi om du kontrollerte Rojo-bygg, aktiv scene, flere klienter eller utgitt testversjon. [Testmoduser i Studio](https://create.roblox.com/docs/studio/testing-modes) · [Data stores](https://create.roblox.com/docs/cloud-services/data-stores) · [Roblox Creator Hub](https://create.roblox.com/docs)
