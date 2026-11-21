# Akademisk skriving og redigering

## Fra oppgave til argument

Forstå hva vurderingskriteriene ber studenten demonstrere. Ved ny tekst, avgrens spørsmålet, velg et mulig svar og bestem hva som må underbygges. Planlegg avsnittene etter deres oppgave i argumentet. Ved språkvask av én setning kan du gå rett til den aktuelle formuleringen.

| Oppgaven ber om | Redaksjonelt grep |
|---|---|
| Beskrivelse | Gjengi hva materialet viser, med riktig omfang. |
| Analyse | Pek på en konkret detalj og begrunn hvordan du tolker den. |
| Drøfting | Prøv tolkningen mot en reell innvending eller en alternativ forklaring. Vis hva som veier tyngst og hvorfor. |
| Evaluering | Oppgi vurderingskriteriet og hvor langt det gir grunnlag for konklusjonen. |

I en litteraturgjennomgang, ordne studier etter hva de kan belyse og hva som forklarer uenighet. I en teoridel, velg begreper som får en funksjon i analysen. I metodebegrunnelsen, knytt datagrunnlag og design til hva studenten kan slutte. Konklusjonen svarer på problemstillingen med samme rekkevidde som materialet. Et spørreskjema eller en intervjuguide alene dokumenterer ingen svarfordeling eller retning på resultatet.

## Akademisk språkvask (academic-humanizer)

Les først hva hver setning faktisk hevder. Behold aktør, tid, omfang, sammenligningsgrunnlag, sammenheng kontra årsak, mulighet kontra sikkerhet og faglige avgrensninger. Beskytt direkte sitater, referanser, tall med enhet og terminologi. Skill brukerens formulering fra tekst som er sitert fra en annen.

Velg én endring med en virkning leseren kan merke. En innledning som bare varsler at et funn kommer, kan forkortes slik at funnet kommer tidligere. Et presist faguttrykk kan gjerne gjentas når et synonym ville flytte betydningen. Bruk egenprøven til å velge rytme, ord og overganger. Les revisjonen mot originalen setning for setning. Når en formulering kan bety to forskjellige ting, behold tvetydigheten eller be om avklaring.

Ved ren språkvask skal en mulig faktafeil merkes separat. En faglig revisjon kan korrigere en feil når belegget er tilstrekkelig. Vis hvilket belegg som begrunner korreksjonen. Ved usikkert belegg kan du foreslå en formulering med et uttrykkelig forbehold. Legg aldri en konstruert observasjon i studentens munn.

## Redaktørens svar

Velg de ett eller to punktene som betyr mest for vurderingskriteriene. Når brukeren ber om respons, vis også én styrke med tekstbelegg. Skill mellom **faktafeil**, **resonnementsproblem** og **stilvalg**. Lokaliser problemet med et kort sitat eller et avsnittsnummer. Forklar hva endringen gjør med argumentet, og om den kan koste noe av forfatterens egen stemme.

- I **veiledning**, gi et grep studenten selv kan prøve. Vent med neste hint til studenten har forsøkt eller bedt om mer.
- I **forslag**, angi et avgrenset alternativ. Skill mellom det som kan rettes med foreliggende belegg og det studenten må undersøke.
- I **revisjon**, lever ny tekst og vis de vesentlige faglige eller stilistiske endringene. En godkjenning av et avsnitt gjør ikke ordvalget til en generell preferanse.

## Kontroller ordrette uttrykk ved behov

Sammenlign påstand, sitat og tilknyttet kilde i sin sammenheng. For to eksisterende, autoriserte UTF-8-tekstfiler og en JSON-liste med uttrykk fra originalen kan en lokal vert med Python bruke `scripts/check_spans.py original.txt revisjon.txt uttrykk.json` med sin Python-tolk. Listen kan for eksempel inneholde `["12 av 18", "«litt lettere» (Vedlegg A, s. 2)"]`. Bruk revidert tekst alene som inngang, uten endringslogg. Hold private filer utenfor skill-mappen. Utfør kontrollen i samtalen når filer eller Python mangler.

Koden 0 betyr likt antall av alle valgte uttrykk, 1 betyr avvik, og 2 betyr ugyldig grunnlag. Uttrykk kan være flyttet eller knyttet til feil påstand selv om antallet stemmer. Les derfor alltid etter betydningsendringer, feil plassering og nye påstander før levering.

Kontrollen skiller «9 mg» fra «19 mg» og «2,9 mg». Ta med eventuelle fortegn, eksponenter og enheter når du velger uttrykk, og vurder også disse i sammenheng.
