# Academic Skill

Vil du bruke Academic Skill i alle dine lokale Codex-prosjekter, følg [installasjonsveiledningen](README.md#installer-for-alle-lokale-prosjekter). Der finner du både meldingen til `$skill-installer` og en ZIP-fil med bare skillen.

Vil du prøve skillen i dette prosjektet, kan du bruke **Code → Download ZIP** på GitHub. Pakk ut prosjektarkivet og åpne mappen som inneholder denne filen i Codex. Da finner Codex skillen under `.agents/skills/academic-skill`. Har du allerede klonet prosjektet, kan du hente siste versjon med `git pull --ff-only`.

**Prøv i en ny prosjektsamtale** med for eksempel denne bestillingen:

> Bruk $academic-skill. Jeg vil ha forslag til en metodesetning. Jeg skrev «Intervjuene viste hva alle studentene mente», men jeg intervjuet bare to studenter. Gi meg ett alternativ og forklar hva det endrer.

For å prøve personlig stil, legg til noen få setninger du selv har skrevet, oppgi om de er fra en rapport, refleksjon, presentasjon eller melding, og si hvilke trekk du vil bevare. Du kan be om å se stilobservasjonene, rette dem eller slå dem av i samtalen. Piloten bruker skriveprøven i den aktuelle oppgaven og oppretter ingen profilfil. Ta hensyn til historikkinnstillingene i appen du velger.

**Dette følger med**

- [Skill-en som agenten leser](.agents/skills/academic-skill/SKILL.md). Den viderefører originalens norske skriveveiledning og legger til egne arbeidsmåter for veiledning, forslag og revisjon.
- [Arkitektur og prioritert plan](docs/Arkitektur-og-plan.md). Her ser du dagens funksjoner og rekkefølgen for varig stilprofil, eksamensøving og Office-produksjon.
- [Kilderegister](docs/Kilderegister.md) med undersøkte filer, revisjoner, lisenser og beslutninger for alle sju tredjepartsprosjekter.
- [Testresultater](docs/Testresultater.md) med før- og etterprøver, begrensninger og kommando for å gjenta de lokale testene.

Hvis verten ikke finner skill-en automatisk, kan du be den åpne hovedfilen på stien over. I en ren tekstchat kan du dele hovedfilen og referansen den velger for oppgaven. Skriveflyten kan brukes uten Python og Office. Den valgfrie kontrollen av ordrette tekstuttrykk kan kjøres med Python 3.
