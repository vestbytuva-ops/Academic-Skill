# Arkitektur og utviklingsplan

## 1. Hva fantes fra før?

Hele filtreet på `main` ved revisjon `97db0255ddfb924a25ec0f408087f101bea530fe` inneholdt tre filer. Alle tre ble hentet og kontrollert byte for byte mot Git-objektene før arbeidet startet. Mappen er en lokal arbeidskopi uten Git-historikk. [Originalversjonen på GitHub](https://github.com/vestbytuva-ops/Academic-Skill/tree/97db0255ddfb924a25ec0f408087f101bea530fe)

| Fil i den opprinnelige skill-mappen | Funksjon | Beslutning |
|---|---|---|
| `SKILL.md` | Målform, elevens egen tekst, én styrke og opptil to forbedringer, lærerrespons, tekstanalyse, drøfting, essay, øving og kildesjekk. | Behold navnet og praksisen. Del ut detaljer etter oppgavetype. |
| `references/forskningsverktoy.md` | Litteratursøk, design, utvalgsstørrelse, dataanalyse, usikkerhet og vitenskapelige leveranser. Krever faktisk beregning før tall oppgis. | Behold hele filen og lenk til den fra koordinatoren. |
| `agents/openai.yaml` | Visningsnavn og kort beskrivelse for OpenAI-klienter. | Behold filen. En annen vert kan lese de samme Markdown-instruksjonene. |

Plasseringen `.agents/skills/academic-skill` og klientmetadataene peker mot prosjektlokal bruk i Codex. Fagfunksjonene var instruksjoner til en språkmodell. Det fantes ingen egen tjeneste, database, installasjonsrutine, Office-adapter, testpakke eller rotlisens i treet. NDLA, Udir og Ordbøkene var oppslagslenker. Forskningsveiledningen foreslo metoder uten å levere kode som utfører dem.

Den opprinnelige håndteringen av personlig stil var fornuftig: bruk elevens egen tekst og skill den fra lærerkommentarer. Det manglet en måte å vise hva en stilobservasjon bygde på, avgrense den til en sjanger og la eleven korrigere den. Den tydeligste risikoen var at en lokal preferanse kunne bli behandlet som et varig særtrekk. En annen risiko var at en godt formulert omskriving kunne endre hvor sikkert et funn var.

## 2. Foreslått arkitektur

Behold én oppdagbar Academic Skill. Oppgaven bestemmer hvilken fagveiledning agenten trenger. Lese- og skriveoppgaver kan dermed fungere hos en vert som bare har tilgang til tekst. Et nytt modulnavn skal først få en egen fil når det finnes en konkret arbeidsflyt og en prøve som kan avdekke feil i den.

| Ansvar | Første lokale leveranse | Neste utvidelse |
|---|---|---|
| academic-core | `SKILL.md` velger språk, arbeidsform, kilder og referanser. | Utvid rutingen når en ny modul faktisk er tilgjengelig. |
| personal-voice | Observasjoner på forespørsel, med sjanger, tekststed og begrunnelse. Kan rettes og velges bort i samtalen. | Versjonert, privat lagring med innsyn, samtykke, deaktivering og sletting. |
| academic-writing, humanizer, academic-critic | En felles skriveflyt for disposisjon, faglig revisjon, språkvask og prioriterte tilbakemeldinger. | Skill ut fagspesifikke vurderingskriterier når variasjonen tilsier det. |
| research-integrity | Dagens forskningsreferanse og en enkel protokoll for kildebelegg. | Kontroller referanseeksistens, støttegrad, krysshenvisninger og APA 7 med egne prøver. |
| learning-coach, exam-preparation | Eksisterende veiledning og lærerrespons. | Teach-back, oppgavebank, graderte hint og repetisjon basert på faktisk respons. |
| presentation-engine, office-integration | Arkitektur og valg av verktøy er kartlagt. | Velg én installert og autorisert produsent, valider resultatet og prøv frakoblet alternativ. |
| quality-assurance | Faglig sammenligning før levering, lokalt tekstvern for valgte uttrykk, syntetiske oppgaver på norsk og engelsk. | Office-format, gjengivelse og flere menneskevurderte tekster. |

### Hvordan informasjonen skal flyte

1. Koordinatoren leser oppgaven og brukerens valgte kilder. Den velger veiledning, forslag eller revisjon og avklarer bare opplysninger som endrer leveransen.
2. Skriveflyten henter stilgrunnlag fra samme sjanger og språk når det finnes. Lærerrespons og vurderingskriterier følger oppgaven. Faglige påstander følges tilbake til kilden.
3. Redaktøren gjennomgår utkastet, sammenligner faglig mening og kontrollerer valgte uforanderlige uttrykk. Endringer som krever bedre belegg merkes. Brukeren velger hvilke endringer som passer.
4. I en senere profilversjon kan en uttrykkelig godkjent preferanse få ny versjon. Prosjektkrav får egen kontekst med utløp. En foreslått endring, et avvist løsningsforslag og et faglig faktum har ulike formål og skal holdes adskilt.

### Runtime og verktøy

Codex kan bruke prosjektets eksisterende mappestruktur. For en annen Agent Skills-vert peker man vertens dokumenterte skill-oppdagelse på den indre `academic-skill`-mappen. En vert uten støtte for automatisk oppdagelse kan få inngangen og de aktuelle referansene som tekst. Det kreves ingen MCP-tjeneste eller API-nøkkel for piloten. Den valgfrie eksaktkontrollen bruker Python-standardbiblioteket. I et miljø uten Python sammenligner redaktøren uttrykkene i teksten. Samtalevertens egen historikk og lagringspolicy ligger utenfor denne mappen.

## 3. Prioriterte faser og godkjenningsprøver

| Fase | Endring og begrunnelse | Prøve før utvidelse |
|---|---|---|
| 1. Kartlegging og førmåling | Lås kildeversjonen, les alle filer, registrer sju eksterne prosjekter og lag syntetiske oppgaver. | Kontroller Git-hasher, lisensgrunnlag og at samme oppgaver kan brukes før og etter. |
| 2. Første lokale pilot | Gjør eksisterende skill til koordinator. Legg til sjangeravgrenset stilgrunnlag, tre redaktørmoduser og vern av faglige uttrykk i én tekstflyt. | To språk, flere sjangre, målform, årsaksforbehold, sitater, tall, kildebelegg og bruk uten Office. |
| 3. Personlig akademisk skriving | Bygg privat profillager utenfor prosjektet. Foreslå en endring med begrunnelse, vis differanse og lagre først ved godkjenning. Test akademisk tekst, refleksjon, presentasjon og generell kommunikasjon. | Innsyn, redigering, deaktivering, sletting av historikk, samtidige oppdateringer og sammenligning av samme oppgave med og uten profil. Utvid faglig revisjon med vurderingsrubrikker. |
| 4. Kilder, læring og eksamen | Bygg på påstand–kilde-protokollen. Skill eksistens fra faktisk støtte, sjekk referanselisten begge veier og vurder oppgavens APA-krav. Legg til gjenhenting, teach-back og øvingsøkter med gradvis hjelp. | Prøv kilde som finnes men motsier påstanden, bare sammendrag, manglende referanse, blandede funn, feilaktig elevsvar og tilpasset ny prøve. |
| 5. Office og presentasjoner | Bruk godkjent installert verktøy for ønsket format. Vurder OfficeCLI etter versjonskontroll. Lever redigerbar kopi med ett hovedpoeng per lysbilde, forståelige enheter, kildemerking og lesbar typografi. | Åpne DOCX/XLSX/PPTX i en uavhengig leser. Sammenlign tekst, dataverdier og kilder. Render sider/lysbilder og sjekk avskjæring og kontrast. Logg hva miljøet faktisk kunne kontrollere. |
| 6. Regresjon og utrulling | Gjenta testpakken på kort og lang tekst, begge språk og i målvert. Gjennomgå tilgangsgrenser og filetterslep fra avsluttede oppgaver. | Dokumenter forbedringer og regresjoner per oppgave. Mål aktiverte referanser, svartid og brukerens kvalitetsvurdering før ytelsespåstander. |

Neste prioritet etter piloten er et godkjennbart profilutkast fra to ulike oppgaver. Ved konflikt mellom brukerens avviste formuleringer og et sjangerkrav skal utkastet vise konflikten og la brukeren velge. Først deretter bør profilen få varig lagring. Denne rekkefølgen lar oss teste verdien av profilen før personlige data får lengre levetid.

Kilde- og lisensbeslutninger står i [kilderegisteret](Kilderegister.md). Utførte prøver og gjenværende usikkerhet står i [testrapporten](Testresultater.md).
