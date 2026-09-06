# totemtattoo.nl

Statische site over tattoos, tattoospijt en de opties daarna: aanpassen,
vervagen of laten verwijderen. Verwijst naar de klinieken van Tattoo No More
in Amsterdam, Den Haag en Rotterdam.

## Bouwen

    python3 build.py    # schrijft dist/
    python3 check.py    # controleert dist/

Geen dependencies, alleen de Python-standaardbibliotheek.

## Structuur

- `build.py` opmaak, navigatie, voettekst, sitemap, robots, RSS
- `art.py` eigen SVG-illustraties, inline in de pagina's
- `video.py` video's van het kanaal Tattoo No More, klik-om-te-laden
- `pages_home.py` home
- `pages_spijt.py` spijt, symboliek en stijlen
- `pages_opties.py` opties en behandeling
- `pages_steden.py` de drie vestigingen
- `pages_rest.py` verhalen, vragen, juridische pagina's, 404

`check.py` controleert onder meer op kapotte interne links, dubbele meta,
aanspreekvormen, em-dashes en kostenvermeldingen. Op deze site staat bewust
geen enkele prijs of tariefinformatie.

## Video's

Zonder klik staat er geen iframe in de pagina en gaat er geen verzoek naar
YouTube. Na een klik komt er een iframe naar youtube-nocookie.com.

## Deploy

Cloudflare Pages, project `totemtattoo` in het account van Patricia, direct
upload zonder Git-koppeling. Bijwerken: `python3 build.py`, `dist/` zippen met
de bestanden in de zipwortel en die zip uploaden bij Create deployment.
