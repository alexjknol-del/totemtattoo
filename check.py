#!/usr/bin/env python3
"""Controle op dist/: kapotte interne links, dubbele meta, em-dashes, tweede
persoon, wij-vorm, dummytekst, kostenvermeldingen en ankerteksten."""
import os, re, sys, html

BASE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(BASE, "dist")
problems = []

files = []
for root, _, names in os.walk(DIST):
    for n in names:
        if n.endswith(".html"):
            files.append(os.path.join(root, n))

def rel(p):
    return os.path.relpath(p, DIST)

def text_only(h):
    h = re.sub(r"<script.*?</script>", " ", h, flags=re.S)
    h = re.sub(r"<style.*?</style>", " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", " ", h)
    return html.unescape(h)

titles, descs = {}, {}
targets = set()
for f in files:
    r = rel(f)
    if r == "404.html":
        continue
    d = os.path.dirname(r)
    targets.add("/" if d == "" else "/" + d.replace(os.sep, "/") + "/")

SECOND = r"\b(je|jij|jouw|jullie|uw|u|zich uw)\b"
WE = r"\b(wij|we|ons|onze)\b"
DUMMY = r"(lorem ipsum|TODO|TBD|xxx|placeholder|voorbeeldtekst|\[invullen\])"
KOSTEN = r"\b(euro|prijs|prijzen|tarief|tarieven|kosten|geldterug|vasteprijs|betaald|gratis|goedkoop)\b"

for f in files:
    src = open(f, encoding="utf-8").read()
    r = rel(f)
    body = text_only(src)
    body_words = re.sub(r"https?://\S+|\S+\.(nl|com|be|org)\S*", " ", body)

    m = re.search(r"<title>(.*?)</title>", src, re.S)
    t = m.group(1).strip() if m else ""
    if not t:
        problems.append(f"{r}: geen title")
    titles.setdefault(t, []).append(r)

    m = re.search(r'<meta name="description" content="(.*?)"', src, re.S)
    d = m.group(1).strip() if m else ""
    if not d:
        problems.append(f"{r}: geen meta description")
    elif len(d) > 175:
        problems.append(f"{r}: meta description te lang ({len(d)})")
    descs.setdefault(d, []).append(r)

    if len(re.findall(r"<h1", src)) != 1:
        problems.append(f"{r}: aantal h1 is {len(re.findall(r'<h1', src))}")

    if "—" in src or "–" in src:
        problems.append(f"{r}: em- of en-dash gevonden")

    for w in set(x.lower() for x in re.findall(SECOND, body_words, re.I)):
        problems.append(f"{r}: tweede persoon '{w}'")
    for w in set(x.lower() for x in re.findall(WE, body_words, re.I)):
        problems.append(f"{r}: wij-vorm '{w}'")
    for w in set(x.lower() for x in re.findall(DUMMY, body_words, re.I)):
        problems.append(f"{r}: dummytekst '{w}'")
    for w in set(x.lower() for x in re.findall(KOSTEN, body_words, re.I)):
        problems.append(f"{r}: kostenwoord '{w}'")

    # interne links
    for href in re.findall(r'href="([^"]+)"', src):
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if href.startswith("/assets/") or href in ("/feed.xml", "/sitemap.xml", "/robots.txt"):
            continue
        if href not in targets:
            problems.append(f"{r}: kapotte interne link {href}")

    # ankerteksten uitgaande links
    for m2 in re.finditer(r'<a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>', src, re.S):
        url, anchor = m2.group(1), text_only(m2.group(2)).strip()
        host = re.sub(r"^https?://(www\.)?", "", url).split("/")[0]
        brand = host.split(".")[0]
        ok = (anchor.startswith("http") or anchor == host or
              brand.lower() in anchor.lower().replace(" ", "") or
              anchor.lower() in ("tattoo no more", "tattoonomore"))
        if not ok:
            problems.append(f"{r}: ankertekst uitgaande link '{anchor}' naar {url}")

for t, fs in titles.items():
    if len(fs) > 1:
        problems.append(f"dubbele title '{t}' in {', '.join(fs)}")
for d, fs in descs.items():
    if len(fs) > 1:
        problems.append(f"dubbele description in {', '.join(fs)}")

print(f"{len(files)} pagina's gecontroleerd")
if problems:
    for p in problems:
        print(" - " + p)
    sys.exit(1)
print("geen problemen gevonden")
