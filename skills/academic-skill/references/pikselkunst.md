# Fra referanse til sprite

Velg tre trekk som må kunne gjenkjennes på den ferdige størrelsen. Til et mikroskopikon kan det være okularet, armen og sokkelen. Se først på silhuetten, og bruk deretter farger for å skille delene. Klipp ut motivet i en bildeeditor dersom referansen har en bakgrunn som skal forsvinne. Verktøyet leser alfakanalen og lar en ugjennomsiktig bakgrunn følge med som del av bildet.

Sett en fargegrense som passer størrelsen. Begynn med 6–12 farger for et lite ikon. Samle skygger i sammenhengende flater. Legg inn et lite felt med vekselvis lyse og mørke piksler hvis to fargeflater trenger en mykere overgang. Se på ikonet mot både lys og mørk bakgrunn.

## Bevegelse

Skisser start, utslag og retur. Bestem hva som holder seg fast mellom rutene. En gående figur kan ha et underlag ved samme y-koordinat, mens en roterende viser trenger et fast sentrum. Behold samme lerretsmål i hver rute. Tegn bevegelige deler separat når det gir bedre kontroll over skjøtene.

Se gjennom rutene ved siden av hverandre og spill av GIF-en. Kontroller at avstanden mellom nøkkelpositurene passer tempoet, og at siste rute går naturlig over i den første. En ekstra kopi av startruta på slutten gir en pause i løkka.

## Lokale kommandoer

Kjør fra skill-mappen med Python og Pillow. `sprite` tilpasser motivet proporsjonalt, sentrerer det og bruker heldekkende eller gjennomsiktige piksler. `sheet` legger like store ruter fra venstre mot høyre. `gif` lager en løkke med samme varighet per bilderute, avrundet til GIF-formatets 10 ms.

```sh
python scripts/pixel_art.py sprite referanse.png ikon.png --width 32 --height 32 --colors 8
python scripts/pixel_art.py sheet ruter.png steg-1.png steg-2.png steg-3.png
python scripts/pixel_art.py gif bevegelse.gif steg-1.png steg-2.png steg-3.png --duration-ms 120
```
