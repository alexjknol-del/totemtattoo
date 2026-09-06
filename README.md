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
- `pages_home.py` home
- `pages_spijt.py` spijt, symboliek en stijlen
- `pages_opties.py` opties en behandeling
- `pages_steden.py` de drie vestigingen
- `pages_rest.py` verhalen, vragen, juridische pagina's, 404

`check.py` controleert onder meer op kapotte interne links, dubbele meta,
aanspreekvormen, em-dashes en kostenvermeldingen. Op deze site staat bewust
geen enkele prijs of tariefinformatie.

## Deploy

Cloudflare Pages, framework preset None, build command `python3 build.py`,
output directory `dist`, branch `main`. Elke push naar main deployt.
