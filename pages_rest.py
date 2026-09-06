# -*- coding: utf-8 -*-
"""Verhalen, vragen en juridische pagina's."""

VERHALEN = [
    {"slug": "waarom-de-eerste-tattoo-zelden-de-laatste-is",
     "title": "Waarom de eerste tattoo zelden de laatste is",
     "date": "24 augustus 2026",
     "rfc": "Mon, 24 Aug 2026 09:00:00 +0200",
     "desc": "De meeste mensen blijven niet bij een. Wat dat betekent voor plaatsing, stijlkeuze en de kans dat er later iets weg moet.",
     "body": """
<p class="intro">Wie een eerste tattoo laat zetten, denkt zelden aan de tweede. Toch bepaalt die eerste keuze hoeveel ruimte er later overblijft.</p>

<h2>Het losse begin</h2>
<p>De eerste tattoo staat meestal op zichzelf: een motief op de onderarm, de schouder of het scheenbeen, zonder plan voor wat eromheen komt. Wie het daarbij laat, heeft geen probleem. Wie doorgaat, merkt dat losse stukken zich slecht laten verbinden. Verschillende stijlen, formaten en zwartingen naast elkaar oogt eerder als een verzameling dan als een geheel.</p>

<h2>Wat dat met spijt te maken heeft</h2>
<p>Een groot deel van de spijt gaat niet over het werk zelf maar over de plek die het inneemt. De tattoo staat precies waar later een groter stuk had moeten komen, of het formaat past niet bij wat er daarna bij kwam. Dat is een van de redenen waarom vervagen zo vaak de oplossing is: niet omdat het werk slecht is, maar omdat het in de weg zit. Zie <a href="/opties/vervagen/">vervagen</a>.</p>

<h2>Wat vooraf helpt</h2>
<ul>
  <li>Bedenk of het bij een blijft. Zo niet, kies dan een plek die zich laat uitbreiden.</li>
  <li>Kies een stijl die zich houdt. Zie <a href="/stijlen/">stijlen</a>.</li>
  <li>Zet niets impulsief op een plek die altijd zichtbaar is. Zie <a href="/spijt/plaatsing/">plaatsing</a>.</li>
  <li>Laat de betekenis van een motief natrekken als het uit een andere cultuur komt. Zie <a href="/symboliek/">symboliek</a>.</li>
</ul>

<p>Wie al verder is en vastloopt, vindt de routes bij <a href="/opties/">opties</a>.</p>
"""},
    {"slug": "inkt-en-de-europese-regels",
     "title": "Inkt en de Europese regels",
     "date": "12 augustus 2026",
     "rfc": "Wed, 12 Aug 2026 09:00:00 +0200",
     "desc": "Sinds 2022 gelden onder REACH strengere eisen aan tattoo-inkt in de EU. Wat dat betekent voor werk dat daarvoor is gezet.",
     "body": """
<p class="intro">Sinds januari 2022 gelden in de Europese Unie strengere eisen aan de samenstelling van tattoo-inkt, onder de REACH-verordening voor chemische stoffen. Een deel van de eerder gebruikte pigmenten mag sindsdien niet meer.</p>

<h2>Waarom dat uitmaakt bij verwijdering</h2>
<p>Inkt is geen gestandaardiseerd product. Twee tattoos die er even zwart uitzien kunnen anders reageren, doordat de pigmentmix per fabrikant en per serie verschilt. Wie werk van voor 2022 laat weghalen, heeft pigment in de huid uit een periode met andere samenstellingen dan nu op de markt zijn. Dat verklaart mede waarom het aantal sessies pas na twee of drie behandelingen echt in te schatten valt.</p>

<h2>De lastige kleuren blijven lastig</h2>
<p>Groen, turquoise en geel vragen ongeacht de regelgeving de meeste sessies. Wit pigment bevat vaak titaandioxide, dat onder laserlicht donker kan verkleuren. Bij zulke kleuren hoort een testplekje voordat een heel vlak wordt aangepakt. Zie <a href="/opties/kleuren/">kleur en laser</a>.</p>

<h2>Wat mee te nemen naar een intake</h2>
<p>Wanneer en waar het werk is gezet, helpt de behandelaar bij de inschatting. Bij werk uit het buitenland of van thuiszetters is de herkomst van de inkt vaak onbekend, wat de bandbreedte ruimer maakt. Zie <a href="/opties/sessies/">aantal sessies</a>.</p>
"""},
    {"slug": "spijt-van-tattoo-en-de-stichting",
     "title": "Tattoos die niet vrijwillig zijn gezet",
     "date": "30 juli 2026",
     "rfc": "Thu, 30 Jul 2026 09:00:00 +0200",
     "desc": "Niet elke tattoo is uit vrije keuze gezet. Over merktekens, dwang en het werk van Stichting Spijt van Tattoo.",
     "body": """
<p class="intro">Het grootste deel van de tattoospijt gaat over smaak en tijd. Een kleiner deel gaat over iets anders: tekens die niet vrijwillig zijn gezet.</p>

<h2>Merktekens</h2>
<p>Er bestaan tattoos die iemand aan een groep of aan een persoon binden. Bij uitbuiting worden ze gebruikt als eigendomsteken, in gangverband als bewijs van lidmaatschap. Wie daar uit stapt, draagt het teken nog. Zolang het zichtbaar is, blijft het verleden meepraten in sollicitaties, in de rechtszaal en op straat.</p>

<h2>Wat de stichting doet</h2>
<p>Stichting Spijt van Tattoo richt zich op deze groep. Een van de behandelaars van Tattoo No More draait daar sinds 2018 wekelijks een dag mee, om dit soort tekens weg te halen. Het gaat vaak om zwart werk op zichtbare plekken, precies het soort pigment dat goed op laser reageert, maar ook om trajecten die langer duren doordat er eerder amateuristisch overheen is gewerkt.</p>

<div class="pull">Bij dit werk is het doel zelden een cover-up. Wat weg moet, moet echt weg.</div>

<h2>Waarom het traject anders loopt</h2>
<p>De aanpak verschilt technisch niet van ander laserwerk: dezelfde apparatuur, dezelfde intervallen, dezelfde nazorg. Het verschil zit in de urgentie en in de begeleiding eromheen. Wat er praktisch bij komt kijken, staat bij <a href="/opties/laseren/">hoe laseren werkt</a> en <a href="/opties/nazorg/">nazorg</a>.</p>
"""},
]

def verhalen_index():
    rows = []
    for i, v in enumerate(VERHALEN, 1):
        rows.append(f"""<div class="row"><div class="n">{i:02d}</div><div>
  <p class="meta">{v["date"]}</p>
  <a href="/verhalen/{v["slug"]}/"><h3>{v["title"]}</h3></a>
  <p>{v["desc"]}</p>
</div></div>""")
    return ('<p class="intro">Langere stukken over inkt, keuzes en wat er daarna gebeurt.</p>\n'
            '<div class="rows">\n' + "\n".join(rows) + "\n</div>")

FAQ = """
<p class="intro">De vragen die bij intakes het vaakst terugkomen, kort beantwoord.</p>

<h2>Over het resultaat</h2>
<p><strong>Gaat een tattoo er echt helemaal af?</strong><br>
Bij ongeveer zeventig procent van de klanten verdwijnt de tattoo binnen acht tot twaalf sessies volledig. Bij zwaar, donker of eerder behandeld werk kan een lichte schaduw achterblijven. Daarom volgt bij de intake een inschatting en geen belofte.</p>

<p><strong>Kunnen alle kleuren weg?</strong><br>
Zwart en donkerblauw reageren het beste. Groen, turquoise en geel vragen meer sessies en zijn niet altijd volledig te verwijderen. Wit kan donker verkleuren. Zie <a href="/opties/kleuren/">kleur en laser</a>.</p>

<p><strong>Kan het bij een donkere huid?</strong><br>
Ja, met aangepaste instellingen en meer tijd tussen de sessies. Het risico is daar niet het litteken maar de pigmentverschuiving. Zie <a href="/opties/huidtype/">huidtype en laser</a>.</p>

<h2>Over het traject</h2>
<p><strong>Hoeveel sessies zijn nodig?</strong><br>
Meestal acht tot twaalf. Bepalend zijn huidtype, kleur, diepte, leeftijd van het werk, de plek op het lichaam en de kwaliteit van de inkt. Zie <a href="/opties/sessies/">aantal sessies</a>.</p>

<p><strong>Hoeveel tijd zit er tussen twee sessies?</strong><br>
Meerdere weken. Het lichaam voert de opgebroken inkt eerst af via het lymfestelsel. Zie <a href="/opties/wachttijd/">wachttijd</a>.</p>

<p><strong>Hoe lang duurt een sessie?</strong><br>
Het laseren zelf duurt vijf tot vijftien minuten. Met koelen en nabespreken is een afspraak doorgaans binnen een halfuur klaar.</p>

<p><strong>Kan een tattoo alleen vervaagd worden voor een cover-up?</strong><br>
Dat gebeurt vaak. Drie tot vijf sessies zijn meestal genoeg om een artiest ruimte te geven. Zie <a href="/opties/vervagen/">vervagen</a>.</p>

<h2>Over de behandeling</h2>
<p><strong>Doet het pijn?</strong><br>
Het meest gehoorde beeld is een elastiekje dat tegen de huid schiet. Ribben, enkels en vingers zijn gevoeliger dan schouder of bovenarm. Verdovende creme kan een uur van tevoren op.</p>

<p><strong>Blijven er littekens achter?</strong><br>
Zelden door de laser zelf. Krabben, korstjes lostrekken en zon op verse huid zijn de grootste oorzaken. Zie <a href="/opties/risicos/">risico's</a>.</p>

<p><strong>Werkt het ook op permanente make-up?</strong><br>
Ja, wenkbrauwen, eyeliner en lipcontouren worden behandeld, met een testplekje vooraf omdat die pigmenten kunnen omslaan. Zie <a href="/opties/permanente-makeup/">permanente make-up</a>.</p>

<p><strong>Worden alle tattoos behandeld?</strong><br>
Nee. Werk groter dan A5, eerder behandelde tattoos en bepaalde kleurpigmenten vallen af of worden apart beoordeeld.</p>

<h2>Praktisch</h2>
<p><strong>Waar zitten de klinieken?</strong><br>
<a href="/amsterdam/">Amsterdam, Bilderdijkstraat 77</a>, <a href="/den-haag/">Den Haag, Schuifmaat 16</a> en <a href="/rotterdam/">Rotterdam, Oudedijk 400</a>.</p>

<p><strong>Hoe wordt een afspraak gemaakt?</strong><br>
Via de kliniek zelf, op <a href="https://tattoonomore.nl/">tattoonomore.nl</a>.</p>
"""

CONTACT = """
<p class="intro">Totem Tattoo is een informatieve site. Afspraken lopen via de kliniek.</p>

<h2>Over deze site</h2>
<p>Opmerkingen, correcties of aanvullingen kunnen naar <a href="mailto:info@totemtattoo.nl">info@totemtattoo.nl</a>. Er staat bewust geen formulier op de site; e-mail komt direct aan.</p>

<h2>Een afspraak maken</h2>
<table>
  <tr><th>Vestiging</th><th>Adres</th><th>E-mail</th></tr>
  <tr><td>Amsterdam</td><td>Bilderdijkstraat 77</td><td>liselotte@tattoonomore.nl</td></tr>
  <tr><td>Den Haag</td><td>Schuifmaat 16, unit 10</td><td>deniz@tattoonomore.nl</td></tr>
  <tr><td>Rotterdam</td><td>Oudedijk 400</td><td>info@tattoonomore.nl</td></tr>
</table>
<p>Het afsprakensysteem staat op <a href="https://tattoonomore.nl/">https://tattoonomore.nl/</a>.</p>

<h2>Medische vragen</h2>
<p>Bij huidaandoeningen, eerdere littekenvorming, zwangerschap, medicijngebruik dat de huid lichtgevoelig maakt of twijfel over een moedervlek in het gebied geldt eerst het oordeel van een huisarts of dermatoloog.</p>
"""

PRIVACY = """
<p class="intro">Deze site verzamelt zo min mogelijk gegevens. Hieronder staat wat er wel gebeurt.</p>

<h2>Wat er wordt verwerkt</h2>
<p>Er is geen contactformulier, geen inlogfunctie en geen nieuwsbrief. Er worden geen accounts aangemaakt en niets opgeslagen dat tot een persoon te herleiden is, behalve wanneer iemand zelf een e-mail stuurt.</p>

<h2>E-mail</h2>
<p>Berichten aan info@totemtattoo.nl worden bewaard zolang dat nodig is om de vraag te beantwoorden en daarna verwijderd. Ze worden niet voor andere doeleinden gebruikt en niet aan derden verstrekt.</p>

<h2>Serverlogs</h2>
<p>De hostingpartij houdt technische logbestanden bij om de site beschikbaar en veilig te houden. Daarin staan onder meer opgevraagde adressen, tijdstip en browsergegevens. Die gegevens worden niet aan personen gekoppeld en niet voor analyse of advertenties gebruikt.</p>

<h2>Externe links</h2>
<p>Deze site verwijst naar andere websites. Daar geldt het privacybeleid van die partij.</p>

<h2>Rechten</h2>
<p>Inzage of verwijdering kan opgevraagd worden via info@totemtattoo.nl. Klachten over de omgang met persoonsgegevens kunnen naar de Autoriteit Persoonsgegevens via https://autoriteitpersoonsgegevens.nl.</p>
"""

COOKIES = """
<p class="intro">Totem Tattoo plaatst geen cookies voor analyse, advertenties of profilering.</p>

<h2>Welke cookies er zijn</h2>
<p>Geen. Er staat geen statistiekpakket op de site, geen advertentienetwerk en geen socialemediaknop die meekijkt. Daarom verschijnt er ook geen cookiemelding: er valt niets te weigeren.</p>

<h2>Technisch noodzakelijke gegevens</h2>
<p>De hostingpartij kan technische gegevens verwerken die nodig zijn om de site te tonen en misbruik af te vangen. Dat gebeurt zonder cookies op het apparaat van de bezoeker.</p>

<h2>Externe links</h2>
<p>Wie doorklikt naar een andere website komt in een omgeving met een eigen cookiebeleid.</p>

<h2>Vragen</h2>
<p>Vragen over dit beleid kunnen naar info@totemtattoo.nl.</p>
"""

NOTFOUND = """
<div class="wrap">
  <p class="kicker">404</p>
  <h1>Deze pagina bestaat niet</h1>
  <p class="intro">Mogelijk is de pagina verplaatst of klopt het adres niet.</p>
  <div class="rows">
    <div class="row"><div class="n">01</div><div><a href="/spijt/"><h3>Waarom spijt ontstaat</h3></a><p>De vijf oorzaken die steeds terugkomen.</p></div></div>
    <div class="row"><div class="n">02</div><div><a href="/opties/"><h3>Opties</h3></a><p>Aanpassen, vervagen of laten verwijderen.</p></div></div>
    <div class="row"><div class="n">03</div><div><a href="/amsterdam/"><h3>Vestigingen</h3></a><p>Amsterdam, Den Haag en Rotterdam.</p></div></div>
  </div>
</div>
"""

PAGES = [
    {"slug": "verhalen", "crumb": "Verhalen", "kicker": "Achtergrond",
     "h1": "Verhalen",
     "title": "Verhalen over inkt en spijt | Totem Tattoo",
     "desc": "Langere stukken over de eerste tattoo, de Europese regels voor inkt en tattoos die niet vrijwillig zijn gezet.",
     "body": verhalen_index()},
    {"slug": "veelgestelde-vragen", "crumb": "Veelgestelde vragen", "kicker": "Vragen",
     "h1": "Veelgestelde vragen",
     "title": "Veelgestelde vragen over tattooverwijdering | Totem Tattoo",
     "desc": "Resultaat, aantal sessies, pijn, kleuren, huidtype en permanente make-up: de vragen die bij intakes het vaakst terugkomen.",
     "body": FAQ},
    {"slug": "contact", "crumb": "Contact", "kicker": "Praktisch",
     "h1": "Contact",
     "title": "Contact | Totem Tattoo",
     "desc": "Contactgegevens van Totem Tattoo en de e-mailadressen van de vestigingen in Amsterdam, Den Haag en Rotterdam.",
     "body": CONTACT},
    {"slug": "privacybeleid", "crumb": "Privacybeleid", "kicker": "Praktisch",
     "h1": "Privacybeleid",
     "title": "Privacybeleid | Totem Tattoo",
     "desc": "Welke gegevens Totem Tattoo verwerkt, hoe lang e-mail wordt bewaard en welke rechten bezoekers hebben.",
     "body": PRIVACY},
    {"slug": "cookiebeleid", "crumb": "Cookiebeleid", "kicker": "Praktisch",
     "h1": "Cookiebeleid",
     "title": "Cookiebeleid | Totem Tattoo",
     "desc": "Totem Tattoo plaatst geen tracking- of analysecookies. Wat er wel gebeurt en wat geldt bij doorklikken naar andere sites.",
     "body": COOKIES},
    {"slug": "404", "full": True, "h1": "Deze pagina bestaat niet",
     "title": "Pagina niet gevonden | Totem Tattoo",
     "desc": "Deze pagina bestaat niet of is verplaatst.",
     "body": NOTFOUND},
]

for v in VERHALEN:
    PAGES.append({
        "slug": f'verhalen/{v["slug"]}', "crumb": v["title"], "kicker": "Verhaal",
        "h1": v["title"],
        "title": f'{v["title"]} | Totem Tattoo',
        "desc": v["desc"],
        "body": f'<p class="meta">{v["date"]}</p>' + v["body"] +
                '<p><a href="/verhalen/">Terug naar de verhalen</a></p>',
    })
