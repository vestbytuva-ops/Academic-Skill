# Visuelle arbeidsmåter

Bruk språket i oppgaven. Finn ut hva resultatet skal vise og hvilket filformat brukeren trenger. Kjør et medfølgende skript via stien til skillmappen og lagre resultatet i brukerens arbeidsmappe. Lever kildefilen når oppgaven krever at diagrammet kan redigeres. Åpne og kontroller visningen når verktøyene tillater det.

## Pikselkunst og sprites

Velg et motiv, pikselmål, en palett og ønsket bakgrunn. Bruk en lokal referanse fra brukeren eller et originalt utkast. Med Python og Pillow kan pikselverktøyet lage et PNG-ikon, samle like store ruter i et PNG-spriteark eller lage en GIF-løkke. Sjekk silhuett og gjennomsiktighet i faktisk størrelse. Ved animasjon, kontroller rutenes rekkefølge, festepunkt og siste overgang. Bruk en tilgjengelig bildeeditor hvis Pillow mangler. [Pikselveiledning og kommandoer](pikselkunst.md) · [Pikselverktøy](../scripts/pixel_art.py)

## Redigerbare draw.io-diagrammer

Trekk ut trinn, aktører og forbindelser fra materialet. Bruk korte handlingsfraser i prosessnoder, spørsmål i beslutninger og tydelige vilkår på pilene ut av hver beslutning. Merk antakelser som påvirker diagrammet.

Lag en JSON-modell med tittel, noder og piler som i eksemplet. Bruk Python til å lage en redigerbar `.drawio`-fil fra modellen. Kjør fra skillmappen og sett inn egne stier til modell og utfil. [JSON-eksempel](../assets/kildearbeid.json) · [Draw.io-generator](../scripts/make_drawio.py)

```sh
python scripts/make_drawio.py assets/kildearbeid.json kildearbeid.drawio
```

Ved endring av en eksisterende fil, arbeid på en kopi og bevar sider, posisjoner, stiler og koblinger som skal videreføres. Bruk editoren ved flere sider, lag eller svømmebaner. Åpne filen i draw.io når det er mulig. Kontroller ellers XML-strukturen, piler og node-ID-er, og oppgi hva som er visuelt kontrollert.

## UML i PlantUML eller Mermaid

Avgrens systemet og velg diagramtype etter spørsmålet. Skriv en redigerbar `.puml`- eller `.mmd`-fil. Kontroller navn, pilretning, multiplisitet eller meldingsrekkefølge mot oppgaven. [UML-notasjon](uml-notasjon.md) · [Klassediagram](../assets/klassediagram.puml) · [Sekvensdiagram](../assets/innlevering-sekvens.puml) · [Tilstandsdiagram](../assets/utkast-tilstand.mmd)

Ved ønsket SVG eller PNG, bruk den lokale PlantUML-eksporten med Java og en tilgjengelig PlantUML-JAR, eller en Mermaid-renderer for Mermaid. Lever diagramkilden også når en renderer mangler. [PlantUML-eksport](../scripts/render_plantuml.py)
