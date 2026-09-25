# -*- coding: utf-8 -*-
"""Opties en behandeling."""
import art, video

INDEX = f"""
<p class="intro">Van niets doen tot volledig weghalen. Deze pagina's beschrijven wat elke route inhoudt en waar de grenzen liggen.</p>

{art.fig(art.vervagen(), "Van volle tekening naar restpigment, in stappen van enkele sessies.")}


<h2>De routes</h2>
<div class="rows">
  <div class="row"><div class="n">01</div><div><a href="/opties/aanpassen/"><h3>Aanpassen en cover-up</h3></a><p>Wat een artiest kan met bestaand werk, en wanneer dat tegenvalt.</p></div></div>
  <div class="row"><div class="n">02</div><div><a href="/opties/vervagen/"><h3>Vervagen</h3></a><p>Enkele sessies om ruimte te maken voor nieuw werk.</p></div></div>
  <div class="row"><div class="n">03</div><div><a href="/opties/laseren/"><h3>Hoe laseren werkt</h3></a><p>Wat er in de huid gebeurt en hoe een sessie verloopt.</p></div></div>
  <div class="row"><div class="n">04</div><div><a href="/opties/sessies/"><h3>Aantal sessies</h3></a><p>De factoren die bepalen of het zes of achttien keer wordt.</p></div></div>
  <div class="row"><div class="n">05</div><div><a href="/opties/wachttijd/"><h3>Wachttijd tussen sessies</h3></a><p>Waarom er weken tussen zitten en wat er ondertussen gebeurt.</p></div></div>
</div>

<h2>Techniek en huid</h2>
<div class="rows">
  <div class="row"><div class="n">06</div><div><a href="/opties/pico-en-nano/"><h3>Pico- en nanolaser</h3></a><p>Het verschil in pulsduur, en wat marketingbeloftes waard zijn.</p></div></div>
  <div class="row"><div class="n">07</div><div><a href="/opties/huidtype/"><h3>Huidtype en laser</h3></a><p>Waarom donkere huid om lagere instellingen en meer geduld vraagt.</p></div></div>
  <div class="row"><div class="n">08</div><div><a href="/opties/kleuren/"><h3>Kleur en laser</h3></a><p>Zwart gaat het snelst, groen en geel het traagst.</p></div></div>
  <div class="row"><div class="n">09</div><div><a href="/opties/nazorg/"><h3>Nazorg</h3></a><p>De dagen na een sessie bepalen een groot deel van het resultaat.</p></div></div>
  <div class="row"><div class="n">10</div><div><a href="/opties/risicos/"><h3>Risico's</h3></a><p>Blaren, pigmentverschuiving, littekens en wanneer laseren wordt afgeraden.</p></div></div>
  <div class="row"><div class="n">11</div><div><a href="/opties/permanente-makeup/"><h3>Permanente make-up</h3></a><p>Wenkbrauwen, eyeliner en lipcontour vragen een andere aanpak.</p></div></div>
</div>

<div class="plain">
  <p>Niet elk werk komt in aanmerking. Stukken groter dan A5, eerder behandelde tattoos en bepaalde kleurpigmenten worden bij de intake apart beoordeeld of afgewezen, juist omdat de kliniek een resultaatgarantie geeft.</p>
</div>

{video.embed("duur")}
"""

AANPASSEN = f"""
<p class="intro">De snelste route loopt via de tattoo-artiest: bijwerken, aanvullen of er iets nieuws overheen zetten. Dat werkt, zolang het oude werk ruimte laat.</p>

<h2>Wat een artiest kan</h2>
<ul>
  <li>Lijnen aanscherpen en een vervaagd stuk opnieuw zetten.</li>
  <li>Een naam ombouwen tot een motief of een vlak.</li>
  <li>Werk uitbreiden zodat het oude deel opgaat in een groter geheel.</li>
  <li>Een cover-up zetten: nieuw werk dat het oude volledig bedekt.</li>
</ul>

<h2>De beperking van een cover-up</h2>
<p>Een cover-up moet donkerder en dichter zijn dan wat eronder ligt. Hoe zwarter het oude werk, hoe minder keuze de artiest heeft in kleur, formaat en detail. Het gevolg is bekend: het nieuwe ontwerp wordt groter dan bedoeld, en na een paar jaar schemert het oude werk er alsnog doorheen omdat beide lagen anders vervagen.</p>

<div class="pull">Drie tot vijf lasersessies vooraf veranderen de opdracht voor de artiest volledig: van bedekken naar bouwen.</div>

<h2>Volgorde</h2>
<ol class="steps">
  <li>Eerst overleg met de artiest over het nieuwe ontwerp en hoeveel het oude werk in de weg zit.</li>
  <li>Zo nodig lasersessies om te vervagen, met de gebruikelijke weken ertussen. Zie <a href="/opties/vervagen/">vervagen</a>.</li>
  <li>Na de laatste sessie de huid volledig laten herstellen. Reken op minimaal zes tot acht weken voordat er weer getatoeëerd kan worden.</li>
</ol>

<p>Wie twijfelt tussen aanpassen en weghalen, komt meestal uit bij de vraag uit <a href="/spijt/">waarom de spijt ontstond</a>. Zit het in de vorm, dan helpt aanpassen. Zit het in de betekenis, dan zelden.</p>

{video.embed("coveren")}
"""

VERVAGEN = f"""
<p class="intro">Vervagen is geen half werk maar een eigen doel: genoeg pigment weghalen zodat een artiest weer vrij kan ontwerpen.</p>

{art.fig(art.vervagen(), "Vervagen stopt halverwege: genoeg pigment weg om een artiest ruimte te geven.")}


<h2>Wat het inhoudt</h2>
<p>Technisch is het dezelfde behandeling als volledig verwijderen, alleen wordt er eerder gestopt. In plaats van acht tot twaalf sessies gaat het meestal om drie tot vijf. De tattoo is dan nog zichtbaar, maar zoveel lichter dat het nieuwe ontwerp niet meer hoeft te bedekken.</p>

<table>
  <tr><th></th><th>Vervagen</th><th>Volledig weghalen</th></tr>
  <tr><td>Doel</td><td>Ruimte maken voor nieuw werk</td><td>Huid zonder zichtbare inkt</td></tr>
  <tr><td>Sessies</td><td>Meestal drie tot vijf</td><td>Meestal acht tot twaalf</td></tr>
  <tr><td>Doorlooptijd</td><td>Enkele maanden</td><td>Ruim een jaar</td></tr>
  <tr><td>Eindpunt</td><td>Bepaald in overleg met de artiest</td><td>Bepaald door wat de huid loslaat</td></tr>
</table>

<h2>Samen met de artiest</h2>
<p>Het helpt als de artiest vooraf aangeeft welk deel lichter moet. Soms is dat alleen een donker vlak of een naam, en hoeft de rest niet behandeld te worden. De behandelaar richt zich dan op dat gebied, wat het traject kort houdt.</p>

<h2>Wanneer vervagen de logische keuze is</h2>
<ul>
  <li>Zwaar zwart werk waar een cover-up anders nog zwarter zou uitpakken. Zie <a href="/stijlen/blackwork/">blackwork</a>.</li>
  <li>Tribal en oud letterwerk. Zie <a href="/symboliek/tribal-en-maori/">tribal en maori</a>.</li>
  <li>Een tattoo die op zich goed is, maar te groot voor het nieuwe idee.</li>
</ul>

<p>Na de laatste sessie moet de huid volledig herstellen voordat er weer inkt in gaat. Wat daarbij hoort staat bij <a href="/opties/nazorg/">nazorg</a>.</p>
"""

LASEREN = f"""
<p class="intro">Een tattoo zit in de lederhuid, buiten bereik van de natuurlijke vernieuwing van huidcellen. Daarom blijft inkt levenslang zitten, en daarom is er een laser nodig om dat te doorbreken.</p>

{art.fig(art.laser(), "De puls breekt het pigment in de lederhuid. Het lymfestelsel voert de deeltjes daarna af.")}


<h2>Wat er gebeurt</h2>
<p>Pigmentdeeltjes zijn te groot om door het lichaam afgevoerd te worden. Afweercellen kapselen ze in en houden ze op hun plek. De laser stuurt een zeer korte lichtpuls af die vooral door het pigment wordt opgenomen en veel minder door het weefsel eromheen. Het deeltje warmt in een fractie van een seconde op, zet uit en valt in kleinere stukken uiteen.</p>
<p>De laser haalt de inkt dus niet weg. Het lichaam doet dat zelf: de kleinere deeltjes gaan via het lymfestelsel het lichaam uit. Vandaar dat een tattoo na een sessie niet meteen lichter is, maar in de weken erna geleidelijk vervaagt.</p>

<h2>Een sessie van dichtbij</h2>
<ol class="steps">
  <li>De huid wordt gekoeld, wat de pijn verzacht en het weefsel rond het pigment beschermt.</li>
  <li>Golflengte en energie worden ingesteld op de kleur van de inkt en het huidtype.</li>
  <li>Het laseren zelf duurt vijf tot vijftien minuten, afhankelijk van het oppervlak.</li>
  <li>Direct erna kleurt de plek wit. Dat is een gasreactie en trekt binnen ongeveer een halfuur weg.</li>
  <li>Er gaat Alhydran op de huid, dat de plek vochtig houdt tijdens het genezen.</li>
</ol>

<h2>Hoe het voelt</h2>
<p>De meest gebruikte vergelijking is een elastiekje dat tegen de huid schiet: kort en scherp, gevolgd door een warm gevoel als bij zonnebrand. Verdovende creme, zoals <a href="https://tktxtattoos.de/" rel="noopener" target="_blank">TKTX</a>, kan een uur van tevoren op, ongeveer een millimeter dik en afgedekt met folie. Te dun smeren of niet afdekken maakt het effect klein.</p>

<h2>Waarom niet in een keer</h2>
<p>Per sessie wordt een deel van het pigment opgebroken. Wat overblijft ligt dieper of werd afgeschermd door de laag erboven. Pas als de eerste laag is afgevoerd, komt de laser bij de volgende. Zie <a href="/opties/sessies/">aantal sessies</a> en <a href="/opties/wachttijd/">wachttijd</a>.</p>

{video.embed("pijn")}
"""

PICONANO = f"""
<p class="intro">Het verschil tussen een nanolaser en een picolaser zit in de duur van de puls. Die duur bepaalt of pigment vooral door warmte of vooral door druk uiteenvalt.</p>

<h2>Twee soorten pulsen</h2>
<table>
  <tr><th></th><th>Nanolaser</th><th>Picolaser</th></tr>
  <tr><td>Pulsduur</td><td>Miljardsten van een seconde</td><td>Biljoensten van een seconde</td></tr>
  <tr><td>Werking</td><td>Vooral thermisch</td><td>Vooral mechanisch</td></tr>
  <tr><td>Deeltjes na de puls</td><td>Klein</td><td>Kleiner, makkelijker af te voeren</td></tr>
  <tr><td>Warmte in de huid</td><td>Meer</td><td>Minder</td></tr>
  <tr><td>Sterk bij</td><td>Zwart en donkerblauw, dieper pigment</td><td>Lastige kleuren en restanten</td></tr>
</table>

<h2>Waarom beide naast elkaar staan</h2>
<p>Een picolaser is niet in alle gevallen de betere keuze. Diep en zwaar zwart werk reageert vaak prima op een nanolaser, terwijl hardnekkige kleurresten en fijn pigment beter op een picolaser reageren. Klinieken met beide typen kunnen per sessie kiezen; met een enkel apparaat moet alles daarmee opgelost worden.</p>

<div class="pull">Het apparaat is een deel van de uitkomst, niet de hele uitkomst. Instellingen en ervaring wegen minstens even zwaar.</div>

<h2>Wat te vragen bij een vergelijking</h2>
<ul>
  <li>Welke golflengtes zijn beschikbaar, en dus welke kleuren kunnen aangepakt worden.</li>
  <li>Hoeveel ervaring is er met dit huidtype. Zie <a href="/opties/huidtype/">huidtype en laser</a>.</li>
  <li>Wordt er met een testplekje gewerkt bij twijfelachtige pigmenten.</li>
</ul>
<p>De klinieken achter deze site werken met een nanolaser en een picolaser, allebei CE-gecertificeerd voor medisch gebruik.</p>

{video.embed("pijnvrij")}
"""

SESSIES = f"""
<p class="intro">Bij ongeveer zeventig procent van de klanten is de tattoo binnen acht tot twaalf sessies weg. Die bandbreedte komt door zes factoren.</p>

{art.fig(art.sessies(), "Per sessie verdwijnt een deel van het pigment. De eerste sessies leveren het meeste zichtbare verschil.")}


<table>
  <tr><th>Factor</th><th>Effect</th></tr>
  <tr><td>Huidtype</td><td>Lichtere huid verdraagt hogere instellingen en vraagt doorgaans minder sessies</td></tr>
  <tr><td>Diepte van de inkt</td><td>Dieper gezet pigment vraagt meer sessies</td></tr>
  <tr><td>Kleur</td><td>Zwart en donkerblauw gaan het snelst, groen en geel het traagst</td></tr>
  <tr><td>Kwaliteit van de inkt</td><td>De samenstelling verschilt per fabrikant en per serie</td></tr>
  <tr><td>Plek op het lichaam</td><td>Goede doorbloeding versnelt de afvoer van pigment</td></tr>
  <tr><td>Leeftijd van het werk</td><td>Ouder werk is vaak al deels afgebroken en reageert sneller</td></tr>
</table>

<h2>Amateurwerk tegenover professioneel werk</h2>
<p>Thuis gezet werk bevat meestal minder pigment en zit onregelmatiger in de huid. Zulke tattoos verdwijnen vaak in vier tot acht sessies. Strak gezet professioneel werk met veel lagen kan het dubbele vragen.</p>

<h2>Waarom er geen exact getal komt</h2>
<p>Bij de intake volgt een bandbreedte, geen belofte. Pas na twee of drie sessies is te zien hoe huid en pigment reageren, en wordt de inschatting scherper. Wie een deadline heeft, telt terug: tien sessies met intervallen van zes tot acht weken beslaan ruim een jaar.</p>

<div class="pull">De eerste sessies leveren het meest zichtbare verschil op. Het laatste stuk kost de meeste sessies terwijl het op foto's het minst opvalt.</div>

<p>Voorbeelden van afgeronde trajecten staan op <a href="https://tattoonomore.nl/fotos/">https://tattoonomore.nl/fotos/</a>.</p>

{video.embed("aantal")}
"""

PAGES = [
    {"slug": "opties", "crumb": "Opties", "kicker": "Wat er kan",
     "h1": "Wat er mogelijk is",
     "title": "Opties bij tattoospijt: aanpassen, vervagen of verwijderen | Totem Tattoo",
     "desc": "Elf pagina's over wat er kan met werk waar spijt van is: aanpassen, cover-up, vervagen, laserverwijdering, en wat huid, kleur en nazorg daarin betekenen.",
     "body": INDEX},
    {"slug": "opties/aanpassen", "crumb": "Aanpassen en cover-up", "kicker": "Opties",
     "h1": "Aanpassen en cover-up",
     "title": "Tattoo aanpassen of een cover-up laten zetten | Totem Tattoo",
     "desc": "Wat een tattoo-artiest kan met bestaand werk, waarom een cover-up over donker werk tegenvalt en in welke volgorde het traject loopt.",
     "body": AANPASSEN},
    {"slug": "opties/vervagen", "crumb": "Vervagen", "kicker": "Opties",
     "h1": "Vervagen voor nieuw werk",
     "title": "Tattoo laten vervagen voor een cover-up | Totem Tattoo",
     "desc": "Drie tot vijf sessies om genoeg pigment weg te halen zodat een artiest weer vrij kan ontwerpen, met de verschillen tegenover volledig weghalen.",
     "body": VERVAGEN},
    {"slug": "opties/laseren", "crumb": "Hoe laseren werkt", "kicker": "Opties",
     "h1": "Hoe laseren werkt",
     "title": "Hoe het weglaseren van een tattoo werkt | Totem Tattoo",
     "desc": "Wat de laserpuls met pigment doet, waarom het lymfestelsel het werk afmaakt, hoe een sessie verloopt en hoe het aanvoelt.",
     "body": LASEREN},
    {"slug": "opties/pico-en-nano", "crumb": "Pico- en nanolaser", "kicker": "Opties",
     "h1": "Pico- en nanolaser",
     "title": "Picolaser of nanolaser bij tattooverwijdering | Totem Tattoo",
     "desc": "Verschil in pulsduur en werking, wanneer welk type sterker is en welke vragen zinvol zijn bij het vergelijken van klinieken.",
     "body": PICONANO},
    {"slug": "opties/sessies", "crumb": "Aantal sessies", "kicker": "Opties",
     "h1": "Hoeveel sessies het vraagt",
     "title": "Aantal sessies bij tattooverwijdering | Totem Tattoo",
     "desc": "Zes factoren bepalen of een tattoo in zes of achttien sessies weg is, met het verschil tussen amateurwerk en professioneel werk.",
     "body": SESSIES},
]

WACHTTIJD = f"""
<p class="intro">Tussen twee sessies zitten weken. Dat is geen kwestie van agenda maar een voorwaarde voor het resultaat.</p>

{art.fig(art.tijdlijn(), "Een volledig traject loopt vaak over ruim een jaar, omdat het lichaam tussen de sessies tijd nodig heeft.")}


<h2>Wat er in die weken gebeurt</h2>
<p>De laser breekt pigment op, het lymfestelsel voert het af. Dat kost tijd. Wordt er te snel opnieuw gelaserd, dan ligt het oude, kapotgeschoten pigment nog in de huid en neemt dat de energie op die voor de diepere laag bedoeld was. Minder vooruitgang, meer belasting.</p>
<p>Daarnaast moet de huid zelf herstellen. Blaarvorming, korstjes en roodheid horen bij de eerste dagen. Pas als de bovenste laag intact is, kan de volgende puls daar veilig doorheen.</p>

<h2>Wat het interval bepaalt</h2>
<ul>
  <li>Hoe de huid op de vorige sessie reageerde.</li>
  <li>Het huidtype. Bij donkere huid wordt vaak ruimer gepland. Zie <a href="/opties/huidtype/">huidtype en laser</a>.</li>
  <li>De plek op het lichaam: enkels en handen voeren trager af dan romp en bovenarm.</li>
  <li>Hoeveel pigment er nog zit.</li>
</ul>

<h2>Wat de afvoer helpt</h2>
<ol class="steps">
  <li>Voldoende drinken in de dagen na een sessie.</li>
  <li>Bewegen, wat de lymfestroom op gang houdt.</li>
  <li>Niet roken, of minder. Roken vertraagt de afvoer aantoonbaar.</li>
  <li>De plek uit de zon houden, ook onder dunne kleding bij fel licht.</li>
</ol>

<div class="plain">
  <p>Een zonvakantie kost zes weken in het schema: drie weken voor en drie weken na een sessie moet de plek uit de felle zon blijven.</p>
</div>

{video.embed("interval")}
"""

NAZORG = f"""
<p class="intro">Wat er in de dagen na een sessie gebeurt, bepaalt een groot deel van het resultaat. Nazorg is bovendien de voorwaarde voor de garantie die de kliniek geeft.</p>

{art.fig(art.nazorg(), "Drie punten die het genezen sturen: zon vermijden, koelen en de plek afgedekt houden.")}


<h2>De eerste uren</h2>
<p>Direct na het laseren kleurt de huid wit op de behandelde plek. Die gasreactie trekt binnen ongeveer een halfuur weg. Daarna volgen roodheid en zwelling, vergelijkbaar met een lichte zonnebrand. In de kliniek gaat er Alhydran op, dat de plek vochtig houdt tijdens het genezen.</p>

<h2>De eerste dagen</h2>
<ul>
  <li>Zalven volgens de nazorgflyer, meestal enkele keren per dag.</li>
  <li>Blaren en korstjes met rust laten. Niet doorprikken, niet lostrekken.</li>
  <li>Niet krabben. Krabben is de belangrijkste oorzaak van littekens.</li>
  <li>Kort en lauw douchen. Geen sauna, geen bad, geen zwembad en geen zee zolang de huid open is.</li>
  <li>Geen sport dat langs de plek schuurt of veel zweet in de wond brengt.</li>
  <li>De plek uit de zon houden en geen zonnebank tot drie weken na de sessie.</li>
</ul>

<h2>Normaal en niet normaal</h2>
<table>
  <tr><th>Hoort erbij</th><th>Contact opnemen</th></tr>
  <tr><td>Roodheid en zwelling, enkele dagen</td><td>Toenemende pijn en warmte na dag drie</td></tr>
  <tr><td>Blaren die vanzelf indrogen</td><td>Pus, gele afscheiding of koorts</td></tr>
  <tr><td>Korstvorming en jeuk</td><td>Een wond die na twee weken nog open is</td></tr>
  <tr><td>Tijdelijk lichtere huid op de plek</td><td>Blijvende pigmentverandering rondom</td></tr>
</table>

<h2>Waarom de zalf een voorwaarde is</h2>
<p>Een huid die tijdens het genezen uitdroogt, vormt dikkere korsten en herstelt trager. Dat vraagt extra sessies en vergroot de kans op een blijvend zichtbaar plekje. Omdat de kliniek een garantie op het eindresultaat geeft, hoort het gebruik van Alhydran bij de afspraak.</p>
<p>Meer over wat er mis kan gaan bij <a href="/opties/risicos/">risico's</a>.</p>

{video.embed("sporten")}
"""

HUIDTYPE = f"""
<p class="intro">Bij laserverwijdering telt niet alleen de kleur van de inkt, maar ook die van de huid. Melanine neemt namelijk hetzelfde licht op als het pigment.</p>

{art.fig(art.huidtypen(), "Huidtype bepaalt mede welke golflengte en energie gekozen worden.")}


<h2>De indeling van Fitzpatrick</h2>
<table>
  <tr><th>Type</th><th>Kenmerken</th><th>Aandachtspunt</th></tr>
  <tr><td>I</td><td>Zeer licht, verbrandt altijd</td><td>Weinig concurrentie van melanine</td></tr>
  <tr><td>II</td><td>Licht, verbrandt snel</td><td>Ruime marge in instellingen</td></tr>
  <tr><td>III</td><td>Licht getint, verbrandt soms</td><td>Iets voorzichtiger instellen</td></tr>
  <tr><td>IV</td><td>Getint, verbrandt zelden</td><td>Langere intervallen, lagere energie</td></tr>
  <tr><td>V</td><td>Donker getint</td><td>Risico op hypopigmentatie, ervaring vereist</td></tr>
  <tr><td>VI</td><td>Donkerbruin tot zwart</td><td>Behoedzame opbouw, testplek gebruikelijk</td></tr>
</table>

<h2>Waarom donkere huid meer geduld vraagt</h2>
<p>De laser richt zich op pigment, en melanine in de huid is ook pigment. Bij huidtype vier tot zes neemt de huid zelf een deel van de energie op, wat een lichtere of juist donkerdere plek kan geven. Meestal herstelt dat, maar bij te agressieve instellingen kan het blijven. De aanpak is daarom anders: lagere energie per puls, meer sessies, ruimere intervallen en vaak eerst een testplekje.</p>

<div class="pull">Bij een donkere huid is de vraag niet of het kan, maar hoeveel ervaring de behandelaar heeft met huidtype vijf en zes.</div>

<h2>Zon en bruining</h2>
<p>Een gebruinde huid bevat tijdelijk meer melanine en gedraagt zich onder de laser als een donkerder type. Vandaar de regel van drie weken geen zonnebank of felle zon voor en na een sessie, en twee weken geen zelfbruinende creme. Een kliniek die daar niet naar vraagt, slaat een stap over.</p>

{video.embed("iedereen")}
"""

KLEUREN = f"""
<p class="intro">Elke kleur inkt absorbeert licht van een eigen golflengte. Dat verklaart waarom zwart snel weggaat en groen niet.</p>

{art.fig(art.kleuren(), "Zwart en donkerblauw nemen het licht het best op, geel en pastel het minst.")}


<table>
  <tr><th>Kleur</th><th>Reactie op laser</th></tr>
  <tr><td>Zwart</td><td>Neemt vrijwel het hele spectrum op, verdwijnt het snelst</td></tr>
  <tr><td>Donkerblauw</td><td>Vergelijkbaar met zwart</td></tr>
  <tr><td>Rood</td><td>Reageert redelijk op een groene golflengte</td></tr>
  <tr><td>Paars en bruin</td><td>Wisselend, afhankelijk van de pigmentmix</td></tr>
  <tr><td>Groen en turquoise</td><td>Vragen een rode golflengte, meer sessies nodig</td></tr>
  <tr><td>Geel en oranje</td><td>Lastigst, soms niet volledig te verwijderen</td></tr>
  <tr><td>Wit</td><td>Kan donker verkleuren, wordt zelden behandeld</td></tr>
</table>

<h2>Het probleem met wit</h2>
<p>Witte inkt bevat vaak titaandioxide. Onder laserlicht kan dat pigment chemisch omslaan en grijs of zwart worden. Hetzelfde geldt voor lichte huidkleurige pigmenten uit eerdere cover-ups. In die gevallen hoort een testplekje erbij, en soms wordt behandeling afgeraden.</p>

<h2>Inkt is geen standaardproduct</h2>
<p>Twee tattoos die er even zwart uitzien kunnen totaal anders reageren, omdat de samenstelling per fabrikant en per serie verschilt. Sinds januari 2022 gelden in de Europese Unie strengere eisen aan tattoo-inkt onder de REACH-verordening, waardoor een deel van de eerder gebruikte pigmenten van de markt is. Wie ouder werk laat weghalen, heeft dus vaak pigment in de huid uit een periode met andere samenstellingen.</p>

<p>Zie ook <a href="/stijlen/kleurwerk/">kleurwerk</a> en <a href="/opties/pico-en-nano/">pico- en nanolaser</a>.</p>

{video.embed("kleur")}
"""

PMU = f"""
<p class="intro">Wenkbrauwen, eyeliner en lipcontouren zitten minder diep dan een tattoo, maar de pigmenten zijn onvoorspelbaarder.</p>

<h2>Waarom PMU anders is</h2>
<p>Permanente make-up wordt gezet met pigmenten die zijn gemengd om huidtinten te benaderen. Daar zitten vaak ijzeroxides en titaandioxide in. Die stoffen kunnen onder laserlicht chemisch veranderen: een lichtbruine wenkbrauw kan direct na een puls grijs of oranje kleuren. Meestal is dat met verdere sessies weer weg te werken, maar het maakt een testplekje noodzakelijk.</p>

<h2>Per gebied</h2>
<ul>
  <li><strong>Wenkbrauwen.</strong> Het meest behandelde gebied. Vaak liggen er meerdere lagen van eerdere correcties, elk met een eigen pigment.</li>
  <li><strong>Eyeliner.</strong> Vraagt oogbescherming met metalen schaaltjes onder het ooglid, en dus ervaring op deze plek.</li>
  <li><strong>Lipcontour.</strong> Gevoelig gebied met kans op zwelling. Wie last heeft van koortslip bespreekt dat vooraf.</li>
</ul>

<h2>Verloop</h2>
<p>PMU zit doorgaans ondieper dan een tattoo, waardoor het aantal sessies vaak lager ligt. De vlakken zijn klein, dus de sessies zijn kort. Bij oude, vervaagde PMU die alleen nog als schaduw zichtbaar is, kan een korte reeks al genoeg zijn. Bij dik gezet werk in meerdere lagen loopt het op.</p>

<div class="plain">
  <p>Laat geen nieuwe PMU zetten over oud werk zolang dat oude werk nog zichtbaar is. Elke extra laag maakt verwijdering ingewikkelder, omdat de laser dan door meerdere pigmenten tegelijk moet.</p>
</div>

<p>PMU wordt op alle drie de locaties behandeld: <a href="/amsterdam/">Amsterdam</a>, <a href="/den-haag/">Den Haag</a> en <a href="/rotterdam/">Rotterdam</a>.</p>
"""

RISICOS = f"""
<p class="intro">Laserverwijdering is een ingreep op de huid. De meeste reacties horen bij het genezen, een klein deel is te voorkomen en een enkele vraagt een arts.</p>

<h2>Wat bij het proces hoort</h2>
<ul>
  <li>Witte verkleuring direct na de puls, weg binnen ongeveer een halfuur.</li>
  <li>Roodheid en zwelling gedurende enkele dagen.</li>
  <li>Blaren, soms met vocht, die vanzelf indrogen.</li>
  <li>Korstvorming en jeuk in de week erna.</li>
  <li>Tijdelijk lichtere huid op de behandelde plek.</li>
</ul>

<h2>Littekens</h2>
<p>Littekens ontstaan zelden door de laser zelf en meestal door wat erna gebeurt: krabben, korstjes lostrekken, een infectie of zon op verse huid. Wie snel littekenweefsel vormt of eerder keloid heeft gehad, meldt dat bij de intake, zodat er behoedzamer wordt ingesteld. Let op: soms ligt er al littekenweefsel onder de tattoo, van het zetten zelf. Dat komt tevoorschijn zodra de inkt weg is.</p>

<h2>Pigmentverschuiving</h2>
<p>Hypopigmentatie is een lichtere plek, hyperpigmentatie een donkerdere. Beide komen vaker voor bij huidtype vier tot zes en bij een gebruinde huid. Meestal herstelt de huidkleur in de maanden erna. Zie <a href="/opties/huidtype/">huidtype en laser</a>.</p>

<h2>Wanneer laseren wordt afgeraden</h2>
<ul>
  <li>Zwangerschap en borstvoeding, uit voorzorg.</li>
  <li>Medicijnen die de huid lichtgevoelig maken, waaronder bepaalde antibiotica en acnemiddelen.</li>
  <li>Een actieve huidaandoening of ontsteking op de plek zelf.</li>
  <li>Recent gebruik van de zonnebank of een sterk gebruinde huid.</li>
  <li>Een moedervlek binnen het te behandelen gebied. Die wordt niet gelaserd en eerst door een arts beoordeeld.</li>
</ul>

<div class="pull">Een kliniek die vooraf niet vraagt naar medicijnen, huidaandoeningen, zonblootstelling en eerdere behandelingen, slaat een stap over die ertoe doet.</div>

{video.embed("risico") + video.embed("littekens")}
"""

PAGES += [
    {"slug": "opties/wachttijd", "crumb": "Wachttijd", "kicker": "Opties",
     "h1": "Waarom er weken tussen sessies zitten",
     "title": "Wachttijd tussen twee lasersessies | Totem Tattoo",
     "desc": "Het lymfestelsel heeft tijd nodig om opgebroken pigment af te voeren. Wat het interval bepaalt en wat de afvoer versnelt of vertraagt.",
     "body": WACHTTIJD},
    {"slug": "opties/nazorg", "crumb": "Nazorg", "kicker": "Opties",
     "h1": "Nazorg na een sessie",
     "title": "Nazorg na het laseren van een tattoo | Totem Tattoo",
     "desc": "De eerste uren en dagen na een lasersessie, wat normaal is, wanneer contact opnemen en waarom de zalf bij de afspraak hoort.",
     "body": NAZORG},
    {"slug": "opties/huidtype", "crumb": "Huidtype", "kicker": "Opties",
     "h1": "Huidtype en laser",
     "title": "Huidtype bij tattooverwijdering, ook donkere huid | Totem Tattoo",
     "desc": "De indeling van Fitzpatrick, waarom melanine met het pigment concurreert en hoe de aanpak verandert bij huidtype vier tot zes.",
     "body": HUIDTYPE},
    {"slug": "opties/kleuren", "crumb": "Kleur en laser", "kicker": "Opties",
     "h1": "Kleur en laser",
     "title": "Welke tattookleuren gaan weg met laser | Totem Tattoo",
     "desc": "Per kleur wat de laser ermee kan, waarom wit pigment kan verkleuren en wat de Europese inktregels betekenen voor ouder werk.",
     "body": KLEUREN},
    {"slug": "opties/permanente-makeup", "crumb": "Permanente make-up", "kicker": "Opties",
     "h1": "Permanente make-up verwijderen",
     "title": "Permanente make-up laten verwijderen met laser | Totem Tattoo",
     "desc": "Wenkbrauwen, eyeliner en lipcontour: waarom PMU-pigment kan omslaan naar grijs of oranje en wat per gebied geldt.",
     "body": PMU},
    {"slug": "opties/risicos", "crumb": "Risico's", "kicker": "Opties",
     "h1": "Risico's en wanneer het niet kan",
     "title": "Risico's bij laserverwijdering van tattoos | Totem Tattoo",
     "desc": "Blaren, korstjes, littekens en pigmentverschuiving, plus de situaties waarin laseren wordt afgeraden.",
     "body": RISICOS},
]
