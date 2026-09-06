#!/usr/bin/env python3
"""Generator voor totemtattoo.nl. Alleen standaardbibliotheek.

Gebruik: python3 build.py   -> schrijft dist/
"""
import os, shutil, html

BASE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(BASE, "dist")

SITE = "Totem Tattoo"
DOMAIN = "https://totemtattoo.nl"
EMAIL = "info@totemtattoo.nl"
TODAY = "2026-08-30"

NAV = [
    ("Spijt", "/spijt/"),
    ("Symboliek", "/symboliek/"),
    ("Stijlen", "/stijlen/"),
    ("Opties", "/opties/"),
    ("Steden", "/amsterdam/"),
    ("Verhalen", "/verhalen/"),
    ("Contact", "/contact/"),
]

CSS = """
:root{
  --paper:#f7f4ef; --paper-2:#efe9e0; --ink:#14120f; --ink-2:#4a453e;
  --rule:#d9d1c5; --accent:#8a2f24; --accent-2:#b8563f; --max:1180px;
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
  font:17px/1.7 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif}
img{max-width:100%;height:auto}
a{color:var(--accent);text-underline-offset:3px}
a:hover{color:var(--accent-2)}
.wrap{max-width:var(--max);margin:0 auto;padding:0 26px}
.masthead{border-bottom:1px solid var(--rule);background:var(--paper)}
.masthead-in{display:flex;align-items:baseline;justify-content:space-between;gap:24px;padding:22px 0 16px}
.wordmark{font-size:23px;letter-spacing:.16em;text-transform:uppercase;text-decoration:none;color:var(--ink);font-weight:600}
.wordmark span{color:var(--accent)}
.tagline{font:12.5px/1.4 ui-sans-serif,system-ui,"Segoe UI",sans-serif;letter-spacing:.14em;
  text-transform:uppercase;color:var(--ink-2)}
nav.bar{border-bottom:1px solid var(--rule);background:var(--paper)}
nav.bar ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:26px}
nav.bar a{display:block;padding:11px 0;text-decoration:none;color:var(--ink);
  font:12.5px/1 ui-sans-serif,system-ui,"Segoe UI",sans-serif;letter-spacing:.14em;text-transform:uppercase}
nav.bar a:hover{color:var(--accent)}
main{padding:38px 0 0}
h1{font-size:clamp(30px,4.6vw,46px);line-height:1.1;margin:0 0 18px;font-weight:600;letter-spacing:-.01em}
h2{font-size:26px;line-height:1.2;margin:40px 0 12px;font-weight:600}
h3{font-size:19px;margin:26px 0 6px;font-weight:600}
p{margin:0 0 15px}
.intro{font-size:20px;line-height:1.6;color:var(--ink-2);margin:0 0 26px;max-width:62ch}
.kicker{font:12px/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.2em;text-transform:uppercase;
  color:var(--accent);margin:0 0 14px}
ul,ol{margin:0 0 16px;padding-left:20px}
li{margin:6px 0}
.hero{border-bottom:1px solid var(--rule);padding:48px 0 40px;background:
  linear-gradient(180deg,var(--paper) 0%,var(--paper-2) 100%)}
.hero h1{max-width:18ch}
.hero .intro{max-width:56ch}
.split{display:grid;grid-template-columns:minmax(0,1fr) 280px;gap:56px;align-items:start;padding-bottom:20px}
.index{position:sticky;top:22px;border-top:2px solid var(--ink);padding-top:12px}
.index h2{font:12px/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.18em;text-transform:uppercase;
  margin:0 0 10px;color:var(--ink-2)}
.index ul{list-style:none;margin:0;padding:0}
.index li{border-bottom:1px solid var(--rule);margin:0}
.index a{display:block;padding:9px 0;text-decoration:none;color:var(--ink);font-size:15.5px}
.index a:hover{color:var(--accent)}
.rows{border-top:1px solid var(--rule);margin:22px 0 26px}
.row{display:grid;grid-template-columns:52px minmax(0,1fr);gap:20px;border-bottom:1px solid var(--rule);
  padding:18px 0}
.row .n{font:13px/1.4 ui-sans-serif,system-ui,sans-serif;letter-spacing:.12em;color:var(--accent)}
.row h3{margin:0 0 4px}
.row p{margin:0;color:var(--ink-2);font-size:16px}
.row a{text-decoration:none}
.row a:hover h3{color:var(--accent)}
.pull{border-left:3px solid var(--accent);padding:4px 0 4px 20px;margin:26px 0;font-size:19px;
  line-height:1.55;color:var(--ink)}
.plain{background:var(--paper-2);border:1px solid var(--rule);padding:18px 22px;margin:26px 0}
.plain p:last-child{margin-bottom:0}
table{width:100%;border-collapse:collapse;margin:0 0 22px;font-size:16px}
th,td{text-align:left;padding:11px 14px 11px 0;border-bottom:1px solid var(--rule);vertical-align:top}
th{font:12px/1.4 ui-sans-serif,system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:30px}
.card{border-top:2px solid var(--ink);padding-top:14px}
.card h3{margin:0 0 6px}
.card p{font-size:16px;color:var(--ink-2)}
.steps{counter-reset:s;list-style:none;padding:0;margin:22px 0}
.steps li{counter-increment:s;position:relative;padding:0 0 16px 46px;border-bottom:1px solid var(--rule);margin:0 0 16px}
.steps li:before{content:counter(s,decimal-leading-zero);position:absolute;left:0;top:2px;
  font:13px/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.1em;color:var(--accent)}
.crumbs{font:12px/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;
  color:var(--ink-2);padding:18px 0 0}
.crumbs a{color:var(--ink-2);text-decoration:none}
.crumbs a:hover{color:var(--accent)}
.meta{font:12.5px/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;
  color:var(--ink-2);margin:0 0 16px}
.cta{border-top:2px solid var(--ink);border-bottom:1px solid var(--rule);padding:22px 0;margin:34px 0}
.cta p{margin:0 0 8px}
.cta a.go{font:13px/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;
  text-decoration:none;border-bottom:2px solid var(--accent);padding-bottom:4px;display:inline-block}
footer.foot{border-top:1px solid var(--rule);margin-top:56px;padding:34px 0 40px;background:var(--paper-2);
  font-size:15.5px}
.foot-cols{display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:34px}
.foot-cols h2{font:12px/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.18em;text-transform:uppercase;
  margin:0 0 10px;color:var(--ink-2)}
.foot-cols ul{list-style:none;padding:0;margin:0}
.foot-cols li{padding:3px 0}
.foot-cols a{color:var(--ink);text-decoration:none}
.foot-cols a:hover{color:var(--accent)}
.fine{border-top:1px solid var(--rule);margin-top:26px;padding-top:14px;
  font:12.5px/1.6 ui-sans-serif,system-ui,sans-serif;color:var(--ink-2)}
@media(max-width:900px){
  .split,.two,.foot-cols{grid-template-columns:1fr;gap:30px}
  .index{position:static;border-top:1px solid var(--rule)}
  .masthead-in{flex-direction:column;align-items:flex-start;gap:6px}
}
"""

def nav_html():
    return "\n".join(f'<li><a href="{h}">{l}</a></li>' for l, h in NAV)

INDEXBOX = """
<aside>
  <div class="index">
    <h2>Vestigingen</h2>
    <ul>
      <li><a href="/amsterdam/">Amsterdam</a></li>
      <li><a href="/den-haag/">Den Haag</a></li>
      <li><a href="/rotterdam/">Rotterdam</a></li>
    </ul>
  </div>
  <div class="index" style="margin-top:26px">
    <h2>Veelgelezen</h2>
    <ul>
      <li><a href="/spijt/">Waarom spijt ontstaat</a></li>
      <li><a href="/opties/vervagen/">Vervagen voor nieuw werk</a></li>
      <li><a href="/opties/laseren/">Hoe laseren werkt</a></li>
      <li><a href="/opties/sessies/">Aantal sessies</a></li>
      <li><a href="/veelgestelde-vragen/">Veelgestelde vragen</a></li>
    </ul>
  </div>
</aside>
"""

def page_html(p):
    slug = p["slug"]
    canonical = DOMAIN + ("/" if slug == "" else f"/{slug}/")
    crumbs = ""
    if slug not in ("", "404"):
        crumbs = ('<div class="wrap crumbs"><a href="/">Totem Tattoo</a> / '
                  + html.escape(p.get("crumb", p["h1"])) + "</div>")
    body = p["body"]
    inner = body if p.get("full") else f"""
<div class="wrap">
  <div class="split">
    <article>
      <p class="kicker">{html.escape(p.get("kicker", "Totem Tattoo"))}</p>
      <h1>{p["h1"]}</h1>
      {body}
    </article>
    {INDEXBOX}
  </div>
</div>"""
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p["title"])}</title>
<meta name="description" content="{html.escape(p["desc"])}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(p["title"])}">
<meta property="og:description" content="{html.escape(p["desc"])}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta name="robots" content="index,follow">
<link rel="alternate" type="application/rss+xml" title="{SITE} verhalen" href="/feed.xml">
<link rel="stylesheet" href="/assets/totem.css">
{p.get("schema", "")}
</head>
<body>
<header class="masthead">
  <div class="wrap masthead-in">
    <a class="wordmark" href="/">Totem<span>.</span>Tattoo</a>
    <p class="tagline">Over inkt, spijt en wat er daarna mogelijk is</p>
  </div>
</header>
<nav class="bar"><div class="wrap"><ul>
{nav_html()}
</ul></div></nav>
{crumbs}
<main>
{inner}
</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot-cols">
      <div>
        <h2>Totem Tattoo</h2>
        <p>Achtergrond over tattoos, waarom er spijt ontstaat en wat er daarna te doen valt. De behandelingen worden uitgevoerd door de klinieken van Tattoo No More in Amsterdam, Den Haag en Rotterdam.</p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <h2>Onderwerpen</h2>
        <ul>
          <li><a href="/spijt/">Spijt</a></li>
          <li><a href="/symboliek/">Symboliek</a></li>
          <li><a href="/stijlen/">Stijlen</a></li>
          <li><a href="/opties/">Opties</a></li>
          <li><a href="/verhalen/">Verhalen</a></li>
        </ul>
      </div>
      <div>
        <h2>Praktisch</h2>
        <ul>
          <li><a href="/amsterdam/">Amsterdam</a></li>
          <li><a href="/den-haag/">Den Haag</a></li>
          <li><a href="/rotterdam/">Rotterdam</a></li>
          <li><a href="/veelgestelde-vragen/">Veelgestelde vragen</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/privacybeleid/">Privacybeleid</a></li>
          <li><a href="/cookiebeleid/">Cookiebeleid</a></li>
        </ul>
      </div>
    </div>
    <p class="fine">Bij twijfel over huid, littekens of medicijngebruik geldt het oordeel van een arts.</p>
  </div>
</footer>
</body>
</html>
"""

def write(path, content):
    full = os.path.join(DIST, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)

def build():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    write("assets/totem.css", CSS.strip() + "\n")

    from pages_home import PAGES as HOME
    from pages_spijt import PAGES as SPIJT
    from pages_opties import PAGES as OPTIES
    from pages_steden import PAGES as STEDEN
    from pages_rest import PAGES as REST, VERHALEN
    pages = HOME + SPIJT + OPTIES + STEDEN + REST

    seen = set()
    for p in pages:
        if p["slug"] in seen:
            raise SystemExit("dubbele slug: " + p["slug"])
        seen.add(p["slug"])
        target = "index.html" if p["slug"] == "" else (
            "404.html" if p["slug"] == "404" else f'{p["slug"]}/index.html')
        write(target, page_html(p))

    urls = []
    for p in pages:
        if p["slug"] == "404":
            continue
        loc = DOMAIN + ("/" if p["slug"] == "" else f'/{p["slug"]}/')
        prio = "1.0" if p["slug"] == "" else ("0.9" if p["slug"] in ("amsterdam", "den-haag", "rotterdam") else "0.7")
        urls.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority></url>")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "\n".join(urls) + "\n</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    items = []
    for v in VERHALEN:
        link = f'{DOMAIN}/verhalen/{v["slug"]}/'
        items.append(f"""  <item>
    <title>{html.escape(v["title"])}</title>
    <link>{link}</link>
    <guid>{link}</guid>
    <pubDate>{v["rfc"]}</pubDate>
    <description>{html.escape(v["desc"])}</description>
  </item>""")
    write("feed.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>{SITE}</title>
  <link>{DOMAIN}/verhalen/</link>
  <description>Achtergrond over tattoos, spijt en verwijdering.</description>
  <language>nl-nl</language>
{chr(10).join(items)}
</channel>
</rss>
""")
    write("_headers", "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    print(f"{len(pages)} pagina's gebouwd in dist/")

if __name__ == "__main__":
    build()
