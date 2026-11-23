# Endringslogg

## November 2026 · 3.0.0 · Samling for flere agenter

- Gjeninnførte alle elleve spesialistene som selvstendige skills. Hovedskillen kan fortsatt brukes alene og kombinerer arbeidsmåter.
- Flyttet kilden fra den tidligere Claude-mappen til `skills/`. Beholdt evaloppgavene, fagreferansene og den norske uttrykkskontrollen. Samlet språk, personvern, arbeidsform og kildebruk i ett felles arbeidsgrunnlag. La til konkrete eksempler for VG1, VG2 og VG3.
- Det stabile navnet `humanizer` vises som **Academic Copyediting**. Veiledningen handler om språkvask med mening, sitater og forbehold i behold.
- La til det portable OpenAI-manifestet, klientmetadata og markedsplassfiler for Codex og Claude Code. Byggingen gir en plugin med alle tolv, en hovedpakke og elleve enkeltpakker. Hver enkeltpakke har ressursene den trenger.
- Erstattet testkravet om én Claude-skill med kontroll av alle navn, YAML, relative filstier, offisielt skjema, pakkefiler og installasjoner. Beholdt alle de 17 eksisterende testene for uttrykkskontrollen.
- La til installasjon og feilsøking på begge språk, evaloppgaver for alle tolv og krav til kataloginnsending. Den gamle Claude-utgaven og de tidligere resultatene er dokumentert nedenfor. [Testresultater for samlingen](docs/Validation.md) · [Plattformer](docs/Compatibility.md)

## 22. november 2026 · Academic Skill for Claude

Omarbeidet fra revisjon `3992ac0`.

### 1. Engelsk og norsk

- La til [engelsk akademisk skriving](skills/academic-skill/references/english.md) med sjangerbegreper, APA, MLA, Chicago og Harvard, samt eksempler på falske venner, artikler, preposisjoner og ordrette formuleringer.
- Flyttet læreplan, norske skolesjangre og oppslag i NDLA, Udir og Ordbøkene til [norsk skole](skills/academic-skill/references/norsk-skole.md). Hovedfilen gir språkreglene. Leseruten for norsk skole krever en norskspråklig bestilling om norsk grunnskole, videregående eller læreplan.
- La inn eksempler på begge språk i README. Sitater beholdes på originalspråket, også når oppgaven og kildene er på ulike språk.

### 2. Claude-pakking

- Flyttet skillen til `.claude/skills/academic-skill/` og fjernet de tolv klientspesifikke metadatafilene. Fjernet de elleve separate installasjonsvalgene og det tilhørende samlingsarkivet.
- Samlet de to README-ene og de to startguidene i én README med norsk først. Fjernet de gamle installasjonsinstruksjonene og kommandoene. Claude.ai-veiledningen viser aktivering under Innstillinger → Funksjoner og opplasting under Tilpass → Skills. [Installasjonsveiledningen for Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- Oppdaterte arkitekturnotatet til den nye mappestrukturen. Markerte pilotens testresultater som historiske og beholdt prøveoppgaver, prøvesvar og kilderegister. Git-lenkene til gamle undersøkte filer peker til faste revisjoner.

### 3. Arbeidsmåter og utløsning

[Hovedfilen](skills/academic-skill/SKILL.md) velger språk, veiledning, forslag eller produksjon og åpner relevante referanser. Beskrivelsen bruker konkrete triggere på begge språk og avgrenser generell koding, småprat og forretningstekst. Den ligger under 200 tegn for å passe den dokumenterte grensen ved opplasting til Claude.ai. [Krav til metadata](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

| Tidligere innhold | Hvor arbeidsmåten ligger nå |
| --- | --- |
| Oppgaveforståelse, kriterier og faglig avgrensning | `oppgaveforstaelse.md` |
| Disposisjon, analyse, drøfting og faglig revisjon | `skriving.md` |
| Språkvask og bevaring av mening | `sprakvask.md` |
| Kritikk, lærerrespons og fagfellevurdering | `kritikk.md` |
| Forskningsveiledning, metode, analyse og kildekontroll | `kildekontroll.md` |
| Læringsveiledning og eksamensøving | `laering-og-eksamen.md` |
| Presentasjoner og Office-materiale fra samme tidligere referanse | `presentasjoner.md` og `office-filer.md` |
| Faglig sluttkontroll og kontroll av valgte ordrette uttrykk | `sluttkontroll.md` |
| Personlig stil og styring av arbeidsprofilen | `personlig-stemme.md` |

Samlet gjentatte regler om kildegrunnlag, tekst i vedlegg og personvern i hovedfilen. Beholdt påstandsvise merkelapper, kontroll av faktisk belegg og synlig usikkerhet. Forkortet det lange JSON-eksemplet for stilprofil til et teksteksempel med samme felt. Tok ut den gamle planen om et varig profillager, i tråd med at profilen gjelder den aktuelle oppgaven.

### 4. Språkvask

Ga arbeidsmåten navnet språkvask på norsk og copyediting på engelsk. Samlet formålet, avgrensningen mot omgåelse av KI-detektorer og oppgavens regler for bruk og opplysning om KI i hovedfilen. Beholdt skillet mellom språkvask og faglig korrigering. I språkgjennomgangen byttet jeg blant annet «Runtime og verktøy» til «Kjøring og verktøy» og «Skjelne mellom» til «Skill mellom».

### 5. Tekstkontroll

Flyttet `sjekk_uttrykk.py` byte for byte og tilpasset teststien. De eksisterende 17 testene omfatter allerede æ, ø, å, kommatall og forskjellen mellom «2,9 mg» og «29 mg». Sluttkontrollen beskriver inndata, Claude-stiene, `BESTÅTT`, `FEIL` og avslutningskodene 0, 1 og 2. Den manuelle reserven teller de samme bokstavelige strengene, gjør kontrollens avgrensning synlig og bevarer kontrollen av betydning i sammenheng.

### 6. Validering

[Evalsettet](skills/academic-skill/evals/evals.json) har seks akademiske bestillinger på norsk, én av dem på nynorsk, tre med forventet svar på engelsk og én salgstekst utenfor fagområdet. I første gjennomgang fikk separate agenter de samme ti bestillingene med og uten skillen. De fikk verken fasit eller eksterne kilder. Med skillen valgte agentene å bruke den i ni faglige tilfeller og lot være ved salgsteksten.

| Eval | Observert i første gjennomgang |
| --- | --- |
| 1. Vurderingskriterier | Begge gjorde de tre kriteriene konkrete og ga ett første steg uten å tillegge kildene funn. |
| 2. Språkvask på nynorsk | Begge bevarte forholdstallet, sitatet og årsaksforbeholdet. Begge delte opp det ordrette uttrykket «12 av 18». |
| 3. Kildehenvisning | Begge fant riktig belegg og avviste årsaksslutningen. Med skillen fikk påstandene de tre merkelappene, og svaret oppga side 4 og manglende sammenligningsgrunnlag for økning. |
| 4. Quiz | Begge stilte ett anvendt spørsmål og ventet med fasit. |
| 5. Presentasjon | Begge fordelte fire minutter på tre lysbilder, skilte visning fra tale og holdt funnet til respondentene. |
| 6. Hel oppgave | Begge ga en disposisjon innenfor lærerens regler. Skillen åpnet først skolereferansen selv om nivået var uoppgitt. |
| 7. Excel-utdrag | Begge fant en gjennomsnittsendring på +0,5 poeng for to komplette par. Med skillen oppga svaret også arket, celleområdet og at grunnlaget var et innlimt utdrag. |
| 8. Engelsk språkvask | Begge rettet de oppgitte feilene og beholdt forbeholdene. Svaret uten skillen hadde først en mer idiomatisk innledning. |
| 9. Blandet språk | Begge svarte på engelsk, beholdt nynorsksitatet og brukte APA-henvisningen med de oppgitte feltene. |
| 10. Utenfor fagområdet | Begge leverte to setninger til salgse-posten. Agenten med tilgang til skillen brukte ingen fagreferanser. |

**Omprøve.** Presiserte at språkvask holder talluttrykk samlet, at skolereferansen krever kjent relevant skolekontekst, og at engelske innledninger kan åpne med et konkret verb. En ny agent beholdt «12 av 18» i oppgave 2, brukte bare oppgaveforståelse og skriving i oppgave 6 og åpnet med «This report examines whether …» i oppgave 8. For quiz, presentasjon og den tospråklige sitatoppgaven var det ingen tydelig kvalitetsforskjell i disse svarparene.

**Teknisk kontroll.** Pakketesten sjekker ett arkiv med `academic-skill/` i roten, nødvendige referanser og evaler, og sammenligner innholdet med kildemappen. Hele testsuiten ble kjørt med `python -m unittest discover -s tests`. 20 tester besto, fordelt på 17 skripttester og tre pakketester. Kontrollerte 32 interne og 48 eksterne lenker.

**Avgrensning.** Evalene er stikkprøver fra dette miljøet, med ett svar per oppgave og betingelse i første gjennomgang. Valg av skill ble prøvd ut fra beskrivelsen i selve agentkjøringene. Opplasting, automatisk utløsning og faktisk Office-filleveranse i Claude er ikke bekreftet. Excel-oppgaven brukte et innlimt utdrag.
