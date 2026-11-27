# Unity og Unreal Engine

## Unity

Les `ProjectSettings/ProjectVersion.txt` og pakkelåsen. Start i den faktiske scenen eller prefab-en. Behold `.meta`-filen sammen med en ressurs når du flytter den, slik at referanser fortsetter å peke på samme GUID. Bruk renderpipeline og inndatasystem fra prosjektet.

| Oppgave | Før du regner endringen som ferdig |
| --- | --- |
| C# og prefabs | Sett scenereferanser i serialiserte felt eller via konvensjonen i prosjektet. Bruk `Awake` og `OnEnable` etter hva som skal skje én gang og ved hver aktivering. Koble av lyttere ved tilsvarende avslutning. Test samme prefab i to instanser. |
| `ScriptableObject` | Bruk som delt definisjon for eksempelvis utstyr eller nivåparametere. Opprett eget objekt for verdier som endres per runde eller per figur. Spill to runder og se at definisjonen fortsatt har forventede verdier. |
| Input System | Velg handlingstype og kontrollskjema. Bruk kontekstbytte mellom UI og spill, og gjenbruk prosjektets `InputAction`-oppsett eller `PlayerInput`. Prøv tastatur og kontroller etter oppsettet og sjekk at bindingsendring treffer riktig spiller. |
| Fysikk i 2D eller 3D | Bruk riktige typer for den aktuelle dimensjonen. Registrer input og legg bevegelser og krefter i fysikksteget når et rigidbody skal styre posisjonen. Bruk `CharacterController` etter dens egen bevegelsesmodell i prosjekter som har den. Test kollisjonslag og omstart. |
| Animasjon | Koble logisk tilstand til Animator-parametere og sjekk overgang med og uten eventuell utgangstid. Ha ett tydelig opphav for posisjonsendring med root motion. Prøv avbrudd og ny aktivering. |
| Tilemap i 2D | Sjekk `Grid`, flislag, sorteringsrekkefølge og `TilemapCollider2D`. Følg motorversjonens innstillinger hvis flisformer slås sammen med komposittkollider. Test skråninger, hjørner og nabofelter. |
| NavMesh | Sjekk hvilken navigasjonsflate og agenttype prosjektet bruker. Prøv gyldig og utilgjengelig mål. Sjekk agentstørrelse, hindringer og lenker over brudd i banen. |
| Bygg og størrelse | Bruk prosjektets byggprofil og skript. Sammenlign Build Report før og etter, og se etter store teksturer, lydfiler eller innhold som kommer inn via flere avhengigheter. Kjør bygget på målplattformen etter en endring i import. |

Kjør tilgjengelige Edit Mode-tester for ren logikk og Play Mode-tester når scene, fysikk eller livssyklus avgjør utfallet. Sjekk konsollen og kjør den eksporterte scenen selv. [Unity-manualen](https://docs.unity3d.com/Manual/index.html) · [Unity Test Framework](https://unity.com/how-to/automated-tests-unity-test-framework)

## Unreal Engine

Les `EngineAssociation` og `Config/`. Kartlegg kart, Blueprint-klasse og C++-kode før du flytter ansvar. Bruk `Actor` for det som står i verden, `ActorComponent` for funksjon som kan gjenbrukes og `Pawn` eller `Character` for figurer som styres. La gjeldende `GameMode`, `GameState` og spillerklassene håndtere regler og tilstand etter prosjektets autoritetsmodell.

| Oppgave | Før du regner endringen som ferdig |
| --- | --- |
| C++ og Blueprints | Legg gjenbrukbare regler i prosjektets etablerte lag. Eksponer data og handlinger med riktige refleksjonsmakroer når Blueprints trenger dem. Kompiler berørte Blueprints i editoren, sjekk standardverdier og start kartet etterpå. |
| Enhanced Input | Finn `Input Action`, `Mapping Context`, modifikatorer og triggere. Bruk konteksten for den relevante lokale spilleren, og prøv skifte fra meny til styring og bytte av spillerfigur. |
| Beslutninger hos spillfigurer | Følg prosjektets Behavior Tree og Blackboard eller StateTree. Bruk data og overganger der oppsettet forventer dem, og se at en handling slipper kontrollen når neste oppgave overtar. Test i en scene med en utilgjengelig destinasjon. |
| Niagara | Bruk en systemressurs med emittere for effekten. Eksponer justerbare parametere og velg en klar hendelse som starter og stopper den. Test synlighet, levetid, opprydding og kostnad på målprofilen. |
| Pakking | Bekreft startkart, kart og data som må til under cooking, samt målplattform og nødvendige SDK-er. Bruk prosjektets eksisterende automatisering eller editorprofil. Gå gjennom byggeloggen og start det pakkede spillet fra en egen mappe. |

Bruk Play In Editor til raske kontroller og en separat spillprosess eller pakket utgave når konfigurasjon, nettverk eller innholdslasting påvirker testen. [Dokumentasjon for Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/) · [Enhanced Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine) · [Behavior Trees](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees-in-unreal-engine)
