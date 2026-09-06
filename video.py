# -*- coding: utf-8 -*-
"""Klik-om-te-laden video's van het kanaal Tattoo No More.

Zonder klik staat er geen iframe in de pagina en gaat er geen verzoek naar YouTube.
"""
import html

CHANNEL = "https://www.youtube.com/@tattoonomore2356"

V = {
    "coveren": ("TesJfGWlVIg", "Verwijderen of laten coveren"),
    "sporten": ("nM7UDf_0FYg", "Douchen, zwemmen en sporten na een sessie"),
    "kleur": ("qDtKcBZB4VM", "Gekleurde tattoos verwijderen"),
    "zon": ("hdICPfNnJ9c", "Zonnen en zonnebank tijdens een traject"),
    "beperkingen": ("j80X2VgZkP8", "Beperkingen na het laseren"),
    "risico": ("DNWua9pp1JU", "Risico's van tattooverwijdering"),
    "aantal": ("BGzUcq7nDto", "Hoeveel behandelingen zijn nodig"),
    "pijnvrij": ("-KkYzUMItxM", "Pijnvrij laseren"),
    "interval": ("2W2BBMWzi9g", "Om de hoeveel weken kan er gelaserd worden"),
    "littekens": ("etX7vchToY8", "Littekens en pigmentverlies"),
    "altijd": ("RpLM75NlGOA", "Kan iedereen behandeld worden"),
    "duur": ("dc0PG-TEcdc", "Hoe lang een traject duurt"),
    "pijn": ("hwaYCZWFaFI", "Doet verwijderen pijn"),
    "iedereen": ("FS0UwEvVoqg", "Kan elke tattoo verwijderd worden"),
    "pijnloos": ("7br6QmmDjno", "Pijnloos verwijderen"),
    "sessies": ("ifmbH0Uj6k8", "Aantal behandelingen per tattoo"),
    "consult": ("tAoI9JutGXw", "Videoconsult vooraf"),
    "kies": ("7NNo2clXsPw", "Kiezen voor zekerheid"),
    "telegraaf": ("wFcwMbuiI3E", "De Telegraaf, Dag tattoo hallo baan"),
    "rijnmond": ("aUsBs7_T6UY", "RTV Rijnmond, Dag tattoo hallo baan"),
    "rtl": ("hHTx7s7iW9o", "RTL Nieuws, Dag tattoo hallo baan"),
    "powned": ("0moAfl-qqvY", "PowNed, Dag tattoo hallo baan"),
    "nu": ("Dj0nAegbqKw", "NU.nl, Dag tattoo hallo baan"),
    "jeugdjournaal": ("tx9is73cAi4", "NOS Jeugdjournaal, Dag tattoo hallo baan"),
}

PLAY = ('<svg class="vplay" viewBox="0 0 44 44" aria-hidden="true">'
        '<circle cx="22" cy="22" r="21" fill="none" stroke="#8a2f24" stroke-width="1.6"/>'
        '<path d="M17,13 L32,22 L17,31 z" fill="#8a2f24"/></svg>')


def embed(key, note=True):
    vid, title = V[key]
    t = html.escape(title)
    n = ('<p class="vnote">De video laadt pas na een klik, via youtube-nocookie.com. '
         'Daarvoor gaat er geen verzoek naar YouTube.</p>') if note else ""
    return (f'<div class="vid">'
            f'<p class="vkicker">Video van Tattoo No More</p>'
            f'<button class="vbtn" type="button" data-v="{vid}" data-t="{t}">'
            f'{PLAY}<span class="vtitle">{t}</span></button>'
            f'{n}</div>')


def strip(keys, kop="In de media"):
    """Meerdere video's onder elkaar, zonder losse toelichting per stuk."""
    items = []
    for k in keys:
        vid, title = V[k]
        t = html.escape(title)
        items.append(f'<button class="vbtn" type="button" data-v="{vid}" data-t="{t}">'
                     f'{PLAY}<span class="vtitle">{t}</span></button>')
    return (f'<div class="vid vlist"><p class="vkicker">{html.escape(kop)}</p>'
            + "".join(items)
            + '<p class="vnote">Elke video laadt pas na een klik, via youtube-nocookie.com.</p></div>')


SCRIPT = """
<script>
document.addEventListener('click',function(e){
  var b=e.target.closest('.vbtn'); if(!b) return;
  var f=document.createElement('iframe');
  f.width=560; f.height=315; f.loading='lazy'; f.title=b.dataset.t;
  f.setAttribute('allow','accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
  f.setAttribute('allowfullscreen','');
  f.src='https://www.youtube-nocookie.com/embed/'+b.dataset.v+'?autoplay=1&rel=0';
  var w=document.createElement('div'); w.className='vframe'; w.appendChild(f);
  b.replaceWith(w);
});
</script>
"""
