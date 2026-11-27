# Mekanikk, kamera og nivå

## Inndata og bevegelse

- Definer handlinger som `hopp`, `bruk` og `pause` i spillets inndatasystem. Koble hver handling til enhetene prosjektet støtter. Bestem om handlingen skal gjentas mens den holdes, utføres én gang ved trykk eller fullføres ved slipp. Ved analog styring, prøv dødsonen rundt null og diagonaler med samme maksfart som langs én akse.
- Registrer korte trykk slik at fysikken kan konsumere dem én gang ved neste steg. La faste fysikksteg håndtere krefter, bevegelse og kollisjon. Oppdater bildet når motoren tegner en ny ramme. Sjekk enhetene til bevegelsesfunksjonen. Noen funksjoner tar hastighet per sekund og anvender tidssteget selv, mens andre tar forflytning per steg.
- I et plattformspill kan et tidsvindu etter avsatskanten gi spilleren litt hoppemargin (*coyote time*). Et annet vindu kan huske hoppetrykk rett før landing (*jump buffer*). Tøm buffer når hoppet utføres. Test trykk like før og etter begge grensene og se at ett trykk gir ett hopp.
- Gi menyer og spill egne inndatakontekster når de deler taster. Sjekk om bytte av fokus, pause eller frakobling av kontroller skal nullstille en handling som holdes inne.

## Kollisjon og fysikk

Velg hva som skal være solid og hva som bare registrerer overlapp, som et målområde. Gi spiller, omgivelser og utløserområder tydelige lag og masker. For en figur som skal følge direkte styring, vurder motorens karakterkontroller. For ting som skal reagere på krefter og støt, bruk et dynamisk legeme og hold kreftene i den delen av koden motoren bruker til fysikk.

Tegn kollisjonsformene i en avgrenset testscene. Prøv gulv, vegg, skråning, bevegelig plattform og en tynn hindring i relevant hastighet. Sjekk målestokk, lag og tidssteg ved hakk eller gjennomslag. Bruk sveip eller kontinuerlig kollisjon der fart og form tilsier det, og mål kostnaden. Gi kollisjonsresultatet en egnet visuell eller auditiv tilbakemelding.

## Kamera og respons

Velg hva spilleren trenger å se før en handling. Bruk en dødsone for små bevegelser og gi plass i spillerens retning der det hjelper orienteringen. Ved myk kamerafølging kan du bruke vekten `1 - exp(-k * delta)`, der `k` styrer hvor raskt kameraet tar igjen målet. Bruk visningsflatens størrelse til å holde hele utsnittet innenfor banen. Tilbakestill kameratilstanden når figuren teleporteres eller scenen lastes på nytt.

Knytt lyd, animasjon, vibrasjon eller partikler til en bestemt spillhendelse. Bruk sterkere signaler for viktigere hendelser. Test at en hendelse fortsatt er lesbar med lyd av og skjermristing redusert. Spesifiser hvilke deler av simuleringen som eventuelt skal pauses ved et kort effektstopp, og behold responsen i menyen. Prøv samme handling med ulik bildefrekvens og be en spiller beskrive hva de oppfattet.

## Nivådesign og generering

1. Bygg nivået med enkle former først. Innholdet kan introdusere en regel trygt, kreve at spilleren bruker den, og så kombinere den med en ny omstendighet. Plasser mål og landemerker der spilleren kan oppdage dem fra relevante ruter.
2. Gå hovedruta og minst én alternativ rute. Se hvor det er lett å misforstå retning eller fare, og hvor omstarten plasserer spilleren. Bruk en tegning av hopp- eller synsrekkevidde hvis det kan forklare en feil.
3. For prosedyregenerering, lag kartdata fra et lagret frø og avgrens tilfeldighetsvalgene. Skill beregningen fra instansiering av scener. Sjekk sammenheng, lovlig start og at mål og nødvendige nøkler faktisk kan nås. Ved kart med porter, kontroller rekkefølgen på nøkler og porter i tillegg til vanlig stisøk.
4. Kjør både et kjent problemfrø og et utvalg nye frø. Logg frø og generatorversjon når en regel brytes. Sett et maksimum for antall forsøk og et definert resultat hvis generatoren ikke finner et gyldig kart.
