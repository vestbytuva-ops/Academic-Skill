# Sluttkontroll

1. Sammenhold leveransen med oppgaveteksten, kriteriene og brukerens bestilling. Prioriter avvik som kan endre svaret, resultatet eller vurderingen.
2. Ved revisjon, sammenlign originalen og den reviderte teksten. Kontroller hvem som gjør hva, tid, omfang, negasjoner, usikkerhet, tall med enhet, sitater og tilknyttede kildehenvisninger. Sjekk betydningen også når ordlyden er lik.
3. Sjekk at tekst, tabeller og presentasjon viser samme funn. Merk hvilke opplysninger som trenger kilde eller materiale du mangler.
4. Gi sted, betydning og ett neste grep for hvert viktig avvik. Rett det du har grunnlag for når brukeren ba om ferdig revisjon. Begrunn faglige rettelser.

## Tell ordrette uttrykk

Bruk `scripts/sjekk_uttrykk.py` når du har tilgang til begge autoriserte tekstversjoner i UTF-8, brukeren vil bevare konkrete uttrykk, og det er nyttig å sammenligne antallet. Velg ordrette strenger fra originalen. Ta med sitatets kilde, fortegn, eksponent eller enhet når den hører sammen med uttrykket. Legg strengene i en JSON-liste, for eksempel `["12 av 18", "«litt lettere» (Vedlegg A, s. 2)"]`.

I Claude.ai kan opplastede originaler og uttrykkslister ligge i `/mnt/user-data/uploads/`, og en bestilt revisjon du har laget kan ligge i `/mnt/user-data/outputs/`. Bruk de faktiske stiene. Hold private filer utenfor skillmappen. Legg bare revidert tekst i revisjonsfilen, uten endringslogg. Lag eventuell midlertidig uttrykksliste utenfor både skillmappen og utmappen. I Claude Code, bruk lokale filstier.

Kjør fra skillmappen med stiene til de tre filene.

```sh
python3 scripts/sjekk_uttrykk.py \
  /mnt/user-data/uploads/original.txt \
  /mnt/user-data/outputs/revisjon.txt \
  /mnt/user-data/uploads/uttrykk.json
```

| Avslutningskode | Utskrift og betydning |
| --- | --- |
| 0 | `BESTÅTT` betyr likt antall for alle valgte uttrykk. |
| 1 | `FEIL indeks=0 antall_original=2 antall_revisjon=1` viser et eksempel på avvik. Indeksen teller fra null i JSON-listen. |
| 2 | `FEIL` betyr ugyldig grunnlag. Ved enkelte feil følger indeks, for eksempel `FEIL indeks=0 antall_original=0` når uttrykket mangler i originalen. |

Like antall sier bare noe om de valgte uttrykkene. Les sitatet sammen med påstanden og kilden for å oppdage flytting, kontekstbytte eller endret mening.

## Sammenlign manuelt ved manglende kodekjøring

Hvis kodekjøring eller Python mangler, si at du sammenligner uttrykkene manuelt. Bruk de tilgjengelige tekstversjonene og tell de samme bokstavelige tegnrekkene, også overlappende treff. Bevar mellomrom, tegn, store og små bokstaver og linjeskift så langt de er synlige. Ved siffer i begynnelsen eller slutten, se om tilstøtende sifre eller et desimalskilletegn mellom sifre gjør treffet til del av et større tall. «9 mg» er et annet uttrykk enn «19 mg» eller «2,9 mg», og «2,9 mg» skiller seg fra «29 mg».

Oppgi hvilke uttrykk som mangler i originalen og hvilke som har endret antall. Oppgi kontrollens avgrensning når en tekst, et tegn eller et linjeskift ikke kan leses sikkert. Vurder meningen i sammenheng også ved manuell kontroll.
