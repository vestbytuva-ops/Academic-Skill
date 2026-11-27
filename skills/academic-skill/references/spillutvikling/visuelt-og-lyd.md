# Grafikk, grensesnitt og lyd i spill

## Fra visuell retning til ferdige spillressurser

1. Finn en representativ spillsituasjon og noter kamera, målestokk eller pikselmål, palett, lysretning og hvilke objekter som må kunne leses raskt. Bruk en prøverute, figur eller skjerm som referanse før du produserer en serie.
2. Lag en enkel ressursliste med ID, funksjon, filformat, størrelse og eventuell attribusjon. Velg dimensjoner, festepunkt og rutenett for animasjon før varianter lages. Skill redigerbar kilde fra eksportert fil, og gi hver variant et navn som kan kobles til bruk i prosjektet.
3. For pikselkunst, bruk [pikselveiledningen](../pikselkunst.md) til å lage originalgrafikk, sette sammen jevnstore bilderuter og kontrollere gjennomsiktighet. Behold samme ankerpunkt gjennom animasjonen. Prøv nærmeste-nabo-filtrering og heltallsskalering når skarpe piksler er ønsket. På et atlas, se etter farge fra nabofelt i kanter. For 3D, sjekk måleenheter, opp-akse, pivoter, normaler, materiale, kollisjon og eventuell rigg.
4. Importer en liten serie og prøv den i scenen. Se etter alfa, silhuett, forskjøvet animasjon og lesbarhet mot både lys og mørk bakgrunn. Bruk importreglene i prosjektet for komprimering, fargerom og mipmaps. Behold sporet til rettighetshaver, lisens og kreditering for materiale som bygges inn.

## Menyer og HUD

Start med informasjonen spilleren trenger før neste valg. Vis helsenivå, mål og varsler i en fast rekkefølge og gi kritisk tilstand et lesbart signal utover farge. Lag en komplett sløyfe fra åpning via valg til retur. Sørg for synlig fokus og et forutsigbart tilbakegrep med hver støttet inndataenhet. Kontroller minste skjermstørrelse, bredt format, sikker skjermsone og lang oversatt tekst. Prøv også pause og omstart når en meny er åpen.

## Shadere og effekter

Identifiser motorens renderpipeline og målenhet før du velger shaderformat. Avklar om effekten bruker UV-, kamera- eller verdenskoordinater. Sett verdier som utvikleren skal kunne justere, som farge og styrke, i materialparametre. Kontroller fargerom og blandemodus, særlig for overganger med alfa. Se effekten med minimums- og maksimumsverdier, i bevegelse og i eksport på målplattformen. Profilér transparente flater og etterbehandling i en scene med representativ mengde grafikk.

## Lyd og musikk

Knytt spillhendelsen til lydtriggeren med klar regel for når den får spille om igjen. Bruk separate bussnivåer for musikk, effekter og stemme hvis prosjektet har disse valgene. Avgrens antall samtidige lyder og prøv romlig avstand for lydkilder som ligger i banen. Kontroller volumendringer, overganger, en hel musikkløkke, fravær av klipping og hva som skjer etter pause eller omstart. Bruk synlig respons for kritiske hendelser som også skal kunne oppfattes med lyd av. I nettspill, prøv første lyd etter en brukerhandling og gjenopptak etter fanebytte.
