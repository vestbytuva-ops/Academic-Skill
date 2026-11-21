# Testresultater fra den lokale piloten

**21. november 2026.** Originalversjonen oppfylte 20 av 21 kriterier i sju syntetiske skriveoppgaver. Piloten oppfylte 21 av 21. Forskjellen gjaldt én engelsk metodeformulering. Utvalget er for lite til å si at piloten generelt skriver bedre. Resultater, kildegrunnlag og kontroll av leveransen kan undersøkes hver for seg.

## Fase 1 · Utgangspunkt og sammenligning

De tre originalfilene ble hentet fra samme [Git-revisjon](https://github.com/vestbytuva-ops/Academic-Skill/tree/97db0255ddfb924a25ec0f408087f101bea530fe). Filstørrelse og Git-objekt for hver lokal original ble kontrollert mot det fullstendige filtreet. Forskningsveiledningen og Codex' visningsmetadata har fortsatt identiske Git-objekter etter endringen. Originalen hadde ingen automatisk testpakke.

Én agentkjøring brukte originalen og én brukte piloten. De mottok de samme sju bestillingene med egne, fiktive skriveprøver. Hver kjøring behandlet bestillingene som separate oppgaver i samme økt. Begge hadde tilgang til de respektive lokale instruksjonene, uten Office, nettsøk eller andre kilder. En tredje modellkjøring fikk svarpar med variert rekkefølge per oppgave og uten versjonsnavn. Den vurderte tre avtalte kriterier per oppgave. Dette er en modellvurdert stikkprøve. Ingen lærer eller fagperson har gitt poengene.

| Oppgave | Original | Pilot | Hva viste svarene? |
|---|---:|---:|---|
| Språkvask, bokmål | 3/3 | 3/3 | Begge beholdt «litt lettere», 12 av 18, sidehenvisningen og forbeholdet om årsak. |
| Metodekritikk, engelsk | 2/3 | 3/3 | Begge påpekte spranget til «caused» og «everyone». Originalen antok at skjemaet spurte om selvtillit. Piloten beskrev når og hvordan undersøkelsen ble gjort. Den ekstra antakelsen gjorde originalens forslag betinget av mer dokumentasjon. |
| Lærerrespons, nynorsk | 3/3 | 3/3 | Begge ba eleven prøve selv. Piloten ba om én mulig forskjell mellom skolene som kunne utfordre generaliseringen. |
| Kildesjekk mot vedlegg, bokmål | 3/3 | 3/3 | Begge skilte støttet, motsagt og uavklart. Piloten fanget også opp at det ikke var påvist noen økning å forklare. |
| Rapport og medstudentmelding, engelsk | 3/3 | 3/3 | Begge skiftet sjanger. Originalen lå tettere på ordlyden i skriveprøvene, men tilskrev forfatteren en personlig opptelling. Piloten beholdt tall og anonymitet, men rapporten ble mer omstendelig. |
| Profilutkast, bokmål | 3/3 | 3/3 | Begge skilte brukerpreferanse, lokalt jeg-krav og lærerkommentar. Piloten viste egne felt for grunnlag, rekkevidde og status. |
| Instruksjon inne i et direkte sitat | 3/3 | 3/3 | Begge gjenga sitatet som tekst, beholdt henvisningen og leverte bare tekstforslaget. |

**Begrensning i før- og ettermålingen.** Poengforskjellen avhenger av om man godtar en antakelse om spørreskjemaets innhold. Ingen av svarene påsto at respondentene faktisk fikk mer selvtillit. Ingen rad gikk ned i poeng, men den lengre engelske rapporten viser en kostnad som poengsummen ikke fanger opp. Eksempelmaterialet gir ikke grunnlag for å måle faktisk læring, forfattergjenkjenning eller ytelse på lange tekster.

**Kontroll av stil alene.** Vi holdt metodesetning, språk, sjanger og fakta faste og endret bare stilgrunnlaget. Begge versjoner skrev «Jeg brukte samme intervjuguide i begge intervjuene» med den personlige profilen og «Begge intervjuene ble gjennomført med samme intervjuguide» med den upersonlige. Begge beholdt usikkerheten om sammenlignbarhet. Uten profil beholdt begge jeg-formen fra originalen. Dette viser påvirkning i denne prøven. Evnen fantes også før endringen.

[Sju oppgaver](../tests/cases.json) · [Vurderingsnøkkel](../tests/Vurderingsnokkel.md) · [Kontrollert stilprøve](../tests/stilkontrast.json) · [Fullstendige svar og poeng](../tests/provesvar.json)

## Fase 2 · Teknisk kontroll

Skill-inngangen ble godkjent av den installerte skill-validatoren. Hovedfilen ble redusert fra 4 522 til 3 971 byte. Detaljene om stil og redigering åpnes når oppgaven krever dem. Byteforskjellen måler bare tekstmengden i inngangen. Faktisk tokenbruk, tidsbruk og automatisk oppdagelse i en ny installasjon er ikke målt.

Alle **15 automatiske kommandolinjetester** av den lokale tekstkontrollen besto på Python 3.12.4. Prøvene bruker midlertidige, syntetiske filer og sjekker returkoder og hva som vises ved feil. De dekker norsk og engelsk, gjentakelser, sitater, henvisninger, måltall, Unicode, UTF-8 med signatur, linjeskift, feilaktige inndata og fravær av privat tekst og filstier i meldinger. Kontrollen skiller for eksempel «9 mg» fra «2,9 mg». Endret fortegn, flytting av sitater og endret betydning trenger også en faglig gjennomgang.

**Brukerens kontroll over profilen.** I en separat samtaleprøve fikk brukeren se grunnlaget, godkjente ett trekk, rettet et annet og ba til slutt om sletting og deaktivering. Første svar var uklart om ett gjenværende trekk. Veiledningen for deaktivering ble derfor presisert etter de sju sammenligningsoppgavene. [Samtaleprøven og omprøven](../tests/profilsamtale.md)

**Delingspakken.** ZIP-filen bygges fra en liste over 17 gjennomgåtte prosjektfiler. Ved sluttkontroll pakkes den ut på nytt, hver fil sammenlignes byte for byte med prosjektmappen, og relative dokumentlenker kontrolleres. Testpakken kjøres fra den utpakkede kopien. Alle skriveeksempler og prøvesvar som følger med, er syntetiske.

Kjør testene fra prosjektmappen med en lokal Python 3-tolk:

```text
python -B -m unittest discover -s tests -v
```

Skriveprøvene kan gjentas ved å gi hver bestilling til skill-en i en ny samtale. Bruk de tilhørende kriteriene og vurder hele svar, også der både før- og etterversjonen får full uttelling. Bruk nye faglige tekster før større endringer godtas.

## Gjenstående arbeid

Neste fase bør prøve stilpreferanser over tid og på tvers av fag med frivillig delte eller syntetiske eksempler. Privat profillager, sletting fra et slikt lager, automatisert APA-kontroll, quizplanlegging og Office-produksjon tilhører senere faser. Ingen Office-fil er produsert eller visuelt kontrollert i denne piloten. Kildeklassifisering ble prøvd mot den delte øvingskilden. Kontroll mot en ekstern publikasjon krever en egen prøve med autorisert tilgang.
