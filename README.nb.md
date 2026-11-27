# Academic Skill

[English](README.md) · [Installasjon for hver agent](docs/Compatibility.md) · [Testresultater](docs/Validation.md)

Academic Skill er én ferdighet for skole- og studiearbeid på norsk og engelsk. Velg `academic-skill` og skriv hva du trenger. Den kan kombinere arbeidsmåtene i samme oppgave, for eksempel sjekke om en kilde støtter konklusjonen din og hjelpe deg med å presentere resultatet muntlig.

## Installer i Codex

Fra denne lokale utgaven kan du kjøre `npx skills add . --skill academic-skill -a codex --copy -y` i repoets rot. For å installere i et annet prosjekt kan du erstatte punktumet med den absolutte stien til denne mappen. Med Node.js og npm kan du også installere versjonen som ligger på GitHubs standardgren:

```sh
npx skills add https://github.com/vestbytuva-ops/Academic-Skill --skill academic-skill -a codex --copy -y
```

Legg til `-g` hvis du vil bruke den i alle prosjektene dine. Åpne en ny Codex-chat og velg **Academic Skill** med `$academic-skill`. Har du en lokal versjon, kan du bytte ut nettadressen med stien til prosjektmappen. [Andre plattformer og oppgradering fra versjon 3](docs/Compatibility.md)

## Hva kan du be om?

| Oppgave | Hva du kan få hjelp med | Veiledning |
| --- | --- | --- |
| Forstå oppgaven | Tolk verbene i oppgaveteksten og gjør vurderingskriterier om til konkrete handlinger. | [Oppgaveforståelse](skills/academic-skill/references/oppgaveforstaelse.md) · [Norsk skole](skills/academic-skill/references/norsk-skole.md) |
| Beholde egen stemme | Finn trekk i egne skriveprøver og velg hva du vil ta vare på. | [Personlig skrivestemme](skills/academic-skill/references/personlig-stemme.md) |
| Skrive fagtekst | Lag en disposisjon, begrunn et argument og vurder en innvending. | [Akademisk skriving](skills/academic-skill/references/skriving.md) · [Engelsk fagspråk](skills/academic-skill/references/english.md) |
| Språkvaske | Gjør et avsnitt tydeligere og behold meningen, sitatene og forbeholdene. | [Språkvask](skills/academic-skill/references/sprakvask.md) |
| Få tilbakemelding | Finn tekststedene der utkastet oppfyller et kriterium eller trenger mer arbeid. | [Tekstkritikk](skills/academic-skill/references/kritikk.md) |
| Kontrollere kilder | Sjekk påstander mot kildene og forklar hva som står uavklart. | [Kildekontroll](skills/academic-skill/references/kildekontroll.md) |
| Lære et begrep | Få et eksempel og en oppgave du kan prøve selv. | [Læringsveiledning](skills/academic-skill/references/laering-og-eksamen.md) |
| Øve til eksamen | Tren muntlig med ett spørsmål om gangen eller lag øvingskort fra notatene. | [Eksamensøving](skills/academic-skill/references/laering-og-eksamen.md) |
| Forberede en presentasjon | Fordel taletiden, velg lysbilder og knytt talepunktene til belegget. | [Presentasjoner](skills/academic-skill/references/presentasjoner.md) |
| Arbeide med Office | Behandle et celleutdrag, et Word-dokument eller en presentasjon med tilgjengelige verktøy. | [Office-filer](skills/academic-skill/references/office-filer.md) |
| Kontrollere sluttproduktet | Sjekk at tall, sitater og henvisninger stemmer og at oppgaven er besvart. | [Sluttkontroll](skills/academic-skill/references/sluttkontroll.md) |

> Vi har fire minutter. Hjelp meg å sjekke hva undersøkelsen viser og lage en disposisjon med talepunkter.

## Visuelle arbeidsmåter

Velg `$academic-skill` i Codex eller `/academic-skill` ved egen skillinstallasjon i Claude Code. Be om et pikselikon, et redigerbart draw.io-diagram eller UML i PlantUML eller Mermaid. Standardinstallasjonen og begge Claude-pakkene inneholder skript og eksempler. [Visuell arbeidsflyt](skills/academic-skill/references/visuelle-arbeidsmater.md)

> Gjør metodenotatene mine om til et redigerbart flytskjema i draw.io. Vis hva som skjer når en kilde må sjekkes nærmere.

Du kan også installere hver prototype for seg. [Visuelle ferdigheter](labs/README.md)

## Spillutvikling

Bruk samme Academic Skill-kommando til å planlegge, bygge eller teste et eget spill. Skillen velger veiledning etter motor og oppgave, fra styring, nivåer, grafikk og lyd til lagring, flerspiller og utgivelse. Den dekker tolv motorer og rammeverk, blant annet Godot, Unity, Unreal Engine, Roblox og Phaser. [Spillveiledning](skills/academic-skill/references/spillutvikling/arbeidsflyt.md) · [Spillmotorer](skills/academic-skill/references/spillutvikling/motorer.md)

> Bruk `$academic-skill` til å bygge én spillbar bane i Godot-prosjektet mitt. Bruk de eksisterende kontrollene og sjekk at jeg kan starte på nytt etter et fall.

## Bygg filer til Claude

Kjør `python tools/build.py` fra prosjektmappen. Velg `dist/academic-skill.zip` i **Upload a skill** eller `dist/academic-skill-claude-plugin.zip` i **Upload a plugin**. Begge inneholder én ferdighet med alle arbeidsmåtene. Flytt de ferdige filene til en mappe ved siden av repoet før du pakker prosjektmappen i Windows. [Bygging og testing](README.md#build-and-validate) · [Utgivelse](docs/Release.md)
