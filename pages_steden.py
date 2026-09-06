# -*- coding: utf-8 -*-
"""Vestigingen."""

def schema(name, street, postal, city, email):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"MedicalBusiness","name":"Tattoo No More {name}",
"description":"Kliniek voor het weglaseren van tattoos en permanente make-up in {city}.",
"url":"https://tattoonomore.nl/","email":"{email}",
"address":{{"@type":"PostalAddress","streetAddress":"{street}","postalCode":"{postal}","addressLocality":"{city}","addressCountry":"NL"}}}}
</script>"""

AMSTERDAM = """
<p class="intro">De Amsterdamse vestiging zit aan de Bilderdijkstraat 77, in het pand van Gallery Salon Studio's, tussen De Hallen en het Kinkerkwartier. Liselotte Wannijn doet er de intakes en de behandelingen.</p>

<h2>Praktisch</h2>
<table>
  <tr><th>Adres</th><td>Bilderdijkstraat 77, Amsterdam</td></tr>
  <tr><th>Behandelaar</th><td>Liselotte Wannijn</td></tr>
  <tr><th>Contact</th><td>liselotte@tattoonomore.nl</td></tr>
  <tr><th>Tram</th><td>Meerdere haltes op loopafstand</td></tr>
  <tr><th>Auto</th><td>Beperkt straatparkeren, parkeergarage De Hallen op ongeveer vijf minuten lopen</td></tr>
  <tr><th>Fiets</th><td>Stallen voor de deur</td></tr>
  <tr><th>Afspraken</th><td><a href="https://tattoonomore.nl/tattoo-verwijderen-amsterdam/">https://tattoonomore.nl/tattoo-verwijderen-amsterdam/</a></td></tr>
</table>

<h2>De jongste van de drie</h2>
<p>Amsterdam opende in 2026 als derde locatie. Liselotte Wannijn kreeg haar opleiding van de oprichters in Rotterdam en werkte daar mee voordat deze praktijk openging. De opzet is dezelfde als in Rotterdam en Den Haag: een behandelaar per locatie, uitsluitend laserwerk, geen ander aanbod ernaast.</p>

<h2>Wat een eerste bezoek inhoudt</h2>
<ol class="steps">
  <li>De behandelaar bekijkt de tattoo, het huidtype, de kleuren en de diepte van de inkt.</li>
  <li>Het ingekleurde oppervlak wordt opgemeten met een stempel van een vierkante centimeter, dus alleen de plekken waar echt inkt zit.</li>
  <li>Daaruit volgt een inschatting van het aantal sessies en van wat er haalbaar is.</li>
  <li>Niet elk werk wordt aangenomen: stukken groter dan A5, eerder behandelde tattoos en bepaalde kleurpigmenten vallen af of worden apart besproken.</li>
</ol>

<h2>Rond de behandeling</h2>
<ul>
  <li>Drie weken voor en na een sessie geen zonnebank en zo min mogelijk fel zonlicht op de plek.</li>
  <li>Twee weken van tevoren geen zelfbruinende creme.</li>
  <li>Op de dag zelf het gebied scheren.</li>
  <li>Verdovende creme kan een uur van tevoren op, ongeveer een millimeter dik en afgedekt met folie.</li>
  <li>Na afloop gaat er Alhydran op de huid. Zie <a href="/opties/nazorg/">nazorg</a>.</li>
</ul>

<p>Wie in Zuid-Holland woont of werkt, zit dichter bij <a href="/den-haag/">Den Haag</a> of <a href="/rotterdam/">Rotterdam</a>. Een traject loopt over meerdere maanden, dus reistijd telt mee in de keuze.</p>
"""

DENHAAG = """
<p class="intro">Den Haag zit aan de Schuifmaat 16, unit 10, in Benoordenhout aan de rand van Wassenaar. Deniz van Reede opende deze vestiging in 2024.</p>

<h2>Praktisch</h2>
<table>
  <tr><th>Adres</th><td>Schuifmaat 16, unit 10, Den Haag</td></tr>
  <tr><th>Behandelaar</th><td>Deniz van Reede</td></tr>
  <tr><th>Contact</th><td>deniz@tattoonomore.nl</td></tr>
  <tr><th>Auto</th><td>Parkeergelegenheid in de directe omgeving</td></tr>
  <tr><th>Bus</th><td>Halte Laan van Heldenburg, ongeveer een kilometer lopen</td></tr>
  <tr><th>Fiets</th><td>Stalling bij de ingang</td></tr>
  <tr><th>Aankomst</th><td>Aanbellen bij unit 10, daarna de trap op, wachtruimte rechts</td></tr>
  <tr><th>Afspraken</th><td><a href="https://tattoonomore.nl/tattoo-verwijderen-den-haag/">https://tattoonomore.nl/tattoo-verwijderen-den-haag/</a></td></tr>
</table>

<h2>Opgebouwd in uren</h2>
<p>Deniz van Reede liep meer dan 1500 uur onder begeleiding mee voordat de Haagse praktijk zelfstandig openging. Dat tempo is een keuze: de keten groeit per franchise, niet per vestigingsronde, en elke behandelaar begint pas zelfstandig als het werk zit.</p>

<h2>Ook permanente make-up</h2>
<p>Naast tattoos wordt hier permanente make-up behandeld: wenkbrauwen, eyeliner en lipcontouren. Die pigmenten gedragen zich anders dan tattoo-inkt en kunnen bij verkeerde instellingen omslaan naar grijs of oranje, dus een testplekje hoort erbij. Zie <a href="/opties/permanente-makeup/">permanente make-up</a>.</p>

<h2>Vanuit de regio</h2>
<p>Vanuit Delft, Zoetermeer, Leiden en Wassenaar is Den Haag meestal de kortste rit. De locatie ligt vlak bij de A44 en de N44. Wie richting Rotterdam werkt, kan terecht aan de <a href="/rotterdam/">Oudedijk</a>; voor Noord-Holland is er <a href="/amsterdam/">Amsterdam</a>.</p>

<div class="plain">
  <p>Voor de eerste afspraak: drie weken geen zonnebank of felle zon op de plek, twee weken geen zelfbruiner, op de dag zelf scheren. De volledige voorbereiding staat bij <a href="/opties/laseren/">hoe laseren werkt</a>.</p>
</div>
"""

ROTTERDAM = """
<p class="intro">Rotterdam is de oorspronkelijke locatie, aan de Oudedijk 400 in Kralingen. Andy Han behandelt er sinds 2010.</p>

<h2>Praktisch</h2>
<table>
  <tr><th>Adres</th><td>Oudedijk 400, 3061 AX Rotterdam</td></tr>
  <tr><th>Behandelaar</th><td>Andy Han</td></tr>
  <tr><th>Contact</th><td>info@tattoonomore.nl</td></tr>
  <tr><th>Tram</th><td>Tram 7, halte Jericholaan</td></tr>
  <tr><th>Metro</th><td>Metro A, halte Gerdesiaweg, ongeveer tien minuten vanaf het centrum</td></tr>
  <tr><th>Auto</th><td>Parkeren in de omgeving, venstertijden en regels wisselen per straat</td></tr>
  <tr><th>Afspraken</th><td><a href="https://tattoonomore.nl/tattoo-verwijderen-rotterdam/">https://tattoonomore.nl/tattoo-verwijderen-rotterdam/</a></td></tr>
</table>

<h2>Waar het begon</h2>
<p>De praktijk startte eind jaren negentig aan de Pleinweg in Rotterdam-Zuid, in een tattooshop, waar Dex Xaviera samen met haar vader als eersten in Nederland tattoos met laser weghaalden. De begeleiding kwam van plastisch chirurg Etienne Lommen, die met medische laserapparatuur in ziekenhuizen werkte. Die medische lijn zit nog in de werkwijze: instellingen per huidtype, vaste nazorg en geen behandelingen waarvan het resultaat niet is in te schatten.</p>
<p>Vanaf 2010 richtte Dex zich weer op het zetten van tattoos en nam Andy Han het laserwerk over. Sinds 2018 draait hij daarnaast wekelijks een dag mee bij Stichting Spijt van Tattoo, die onder meer gang- en uitbuitingstattoos weghaalt.</p>

<h2>Een ding, en niets anders</h2>
<p>Op alle drie de locaties wordt uitsluitend pigment weggehaald. Geen ontharing, geen huidverbetering, geen tattoos zetten. De apparatuur is daar ook op gekozen: een nanolaser en een picolaser, allebei CE-gecertificeerd voor medisch gebruik. Het verschil staat bij <a href="/opties/pico-en-nano/">pico- en nanolaser</a>.</p>

<h2>Garantie op het eindresultaat</h2>
<p>De kliniek geeft een garantie wanneer een tattoo na afronding van het traject niet volledig verdwenen is. Voorwaarde is dat het nazorgadvies wordt opgevolgd, inclusief het gebruik van Alhydran na elke sessie. Om die reden wordt niet elk werk aangenomen. De voorwaarden staan op <a href="https://tattoonomore.nl/">tattoonomore.nl</a>.</p>

<p>Vanuit Dordrecht, Gouda of Schiedam is Rotterdam meestal het dichtstbij. Voor Haaglanden is er <a href="/den-haag/">Den Haag</a>, voor Noord-Holland <a href="/amsterdam/">Amsterdam</a>.</p>
"""

PAGES = [
    {"slug": "amsterdam", "crumb": "Amsterdam", "kicker": "Vestiging",
     "h1": "Amsterdam, Bilderdijkstraat",
     "title": "Tattoo laten verwijderen in Amsterdam | Totem Tattoo",
     "desc": "De vestiging aan de Bilderdijkstraat 77 in Amsterdam: behandelaar, bereikbaarheid, wat een eerste bezoek inhoudt en de voorbereiding.",
     "body": AMSTERDAM, "schema": schema("Amsterdam", "Bilderdijkstraat 77", "1053 KM", "Amsterdam", "liselotte@tattoonomore.nl")},
    {"slug": "den-haag", "crumb": "Den Haag", "kicker": "Vestiging",
     "h1": "Den Haag, Schuifmaat",
     "title": "Tattoo laten verwijderen in Den Haag | Totem Tattoo",
     "desc": "De vestiging aan de Schuifmaat 16 in Den Haag: behandelaar, bereikbaarheid vanuit de regio en behandeling van permanente make-up.",
     "body": DENHAAG, "schema": schema("Den Haag", "Schuifmaat 16", "2496 XG", "Den Haag", "deniz@tattoonomore.nl")},
    {"slug": "rotterdam", "crumb": "Rotterdam", "kicker": "Vestiging",
     "h1": "Rotterdam, Oudedijk",
     "title": "Tattoo laten verwijderen in Rotterdam | Totem Tattoo",
     "desc": "De oudste laserpraktijk voor tattoos van Nederland, aan de Oudedijk 400 in Kralingen: geschiedenis, werkwijze en garantie op het eindresultaat.",
     "body": ROTTERDAM, "schema": schema("Rotterdam", "Oudedijk 400", "3061 AX", "Rotterdam", "info@tattoonomore.nl")},
]
