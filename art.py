# -*- coding: utf-8 -*-
"""Eigen SVG-illustraties voor totemtattoo.nl. Geen externe bestanden, alles inline."""
import random

INK = "#14120f"
INK2 = "#4a453e"
RULE = "#d9d1c5"
ACC = "#8a2f24"
ACC2 = "#b8563f"
PAPER = "#f7f4ef"
PAPER2 = "#efe9e0"


def fig(svg, caption="", cls=""):
    c = f'<figcaption>{caption}</figcaption>' if caption else ""
    k = f"fig {cls}".strip()
    return f'<figure class="{k}">{svg}{c}</figure>'


def _dots(seed, x0, x1, y0, y1, n, r0, r1, opa0, opa1, color=INK):
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        t = rnd.random()
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * rnd.random()
        r = r0 + (r1 - r0) * rnd.random()
        o = opa0 + (opa1 - opa0) * t
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{color}" opacity="{o:.2f}"/>')
    return "".join(out)


def totem():
    """Verticale totem met vijf panelen, voor de home."""
    panels = []
    y = 14
    h = 74
    motifs = [
        # maan
        f'<path d="M0,-19 a19,19 0 1,0 13,32 a23,23 0 1,1 -13,-32 z" fill="{INK}"/>',
        # oog
        f'<path d="M-24,0 q24,-19 48,0 q-24,19 -48,0 z" fill="none" stroke="{INK}" stroke-width="2.2"/>'
        f'<circle cx="0" cy="0" r="6.5" fill="{ACC}"/>',
        # golf
        f'<path d="M-26,6 q9,-14 18,0 t18,0 t18,0" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>'
        f'<path d="M-26,-8 q9,-14 18,0 t18,0 t18,0" fill="none" stroke="{ACC}" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>',
        # pijl
        f'<path d="M0,-20 L0,20 M0,-20 l-9,12 M0,-20 l9,12" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>'
        f'<path d="M-13,6 L13,6" stroke="{ACC}" stroke-width="2.4" stroke-linecap="round"/>',
        # kop, hoekig
        f'<path d="M-21,-8 L-16,-22 L-6,-14 L6,-14 L16,-22 L21,-8 L12,12 L0,20 L-12,12 z" fill="none" '
        f'stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>'
        f'<path d="M-9,-3 L-4,-3 M4,-3 L9,-3" stroke="{ACC}" stroke-width="3.2" stroke-linecap="round"/>'
        f'<path d="M0,4 L-3,9 L3,9 z" fill="{INK}"/>',
    ]
    for i, m in enumerate(motifs):
        panels.append(
            f'<g transform="translate(78,{y + h / 2:.0f})">'
            f'<rect x="-64" y="-{h/2-4:.0f}" width="128" height="{h-8}" fill="{PAPER2}" stroke="{RULE}"/>'
            f'{m}</g>')
        y += h
    fading = _dots(7, 176, 300, 20, 386, 110, 0.7, 2.6, 0.85, 0.05)
    return (f'<svg viewBox="0 0 310 400" role="img" aria-label="Totem van vijf tattoomotieven, '
            f'rechts pigment dat naar rechts toe verdwijnt" xmlns="http://www.w3.org/2000/svg">'
            f'<rect x="70" y="8" width="16" height="384" fill="none"/>'
            f'{"".join(panels)}'
            f'<line x1="14" y1="8" x2="14" y2="392" stroke="{RULE}" stroke-width="1"/>'
            f'<line x1="160" y1="8" x2="160" y2="392" stroke="{RULE}" stroke-width="1"/>'
            f'{fading}</svg>')


def vervagen():
    """Pigment dat in vier stappen uiteenvalt."""
    stages = []
    for i in range(4):
        x = 40 + i * 150
        seed = 11 + i
        n = [1, 26, 60, 90][i]
        if i == 0:
            body = f'<ellipse cx="{x}" cy="96" rx="44" ry="30" fill="{INK}"/>'
        else:
            spread = 16 + i * 12
            opa = [0, .75, .45, .22][i]
            body = _dots(seed, x - 44 - i * 4, x + 44 + i * 4, 96 - spread, 96 + spread, n,
                         0.8, 3.4 - i * 0.6, opa, opa * .6)
        stages.append(body)
        stages.append(f'<text x="{x}" y="162" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif" '
                      f'font-size="12" letter-spacing="1.6" fill="{INK2}">{["START","SESSIE 3","SESSIE 6","SESSIE 10"][i]}</text>')
        if i < 3:
            ax = x + 66
            stages.append(f'<path d="M{ax},96 l26,0 m-7,-5 l7,5 l-7,5" fill="none" stroke="{ACC}" '
                          f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')
    return (f'<svg viewBox="0 0 620 180" role="img" aria-label="Een inktvlek die in vier stappen '
            f'uiteenvalt in steeds kleinere deeltjes" xmlns="http://www.w3.org/2000/svg">'
            f'<line x1="0" y1="18" x2="620" y2="18" stroke="{RULE}"/>{"".join(stages)}</svg>')


def laser():
    """Doorsnede van de huid met puls, pigment en afvoer."""
    grains = _dots(3, 150, 470, 150, 176, 34, 1.4, 3.2, .9, .9)
    small = _dots(9, 150, 470, 118, 150, 40, 0.6, 1.5, .55, .2)
    return f'''<svg viewBox="0 0 620 250" role="img" aria-label="Doorsnede van de huid: een laserpuls die pigment in de lederhuid opbreekt" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="60" width="620" height="30" fill="{PAPER2}"/>
<rect x="0" y="90" width="620" height="110" fill="{PAPER2}" opacity=".55"/>
<line x1="0" y1="60" x2="620" y2="60" stroke="{INK}" stroke-width="1.4"/>
<line x1="0" y1="90" x2="620" y2="90" stroke="{RULE}"/>
<line x1="0" y1="200" x2="620" y2="200" stroke="{RULE}"/>
<text x="8" y="78" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11.5" letter-spacing="1.6" fill="{INK2}">OPPERHUID</text>
<text x="8" y="107" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11.5" letter-spacing="1.6" fill="{INK2}">LEDERHUID</text>
<text x="8" y="219" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11.5" letter-spacing="1.6" fill="{INK2}">ONDERHUID</text>
<path d="M300,4 L300,146" stroke="{ACC}" stroke-width="2.4" stroke-linecap="round"/>
<path d="M288,132 L300,148 L312,132" fill="none" stroke="{ACC}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M276,150 L300,110 L324,150 z" fill="{ACC}" opacity=".14"/>
<circle cx="300" cy="152" r="14" fill="none" stroke="{ACC}" stroke-width="1.6" opacity=".7"/>
<circle cx="300" cy="152" r="24" fill="none" stroke="{ACC}" stroke-width="1.2" opacity=".35"/>
{grains}{small}
<path d="M478,160 q46,-22 84,-44 m-15,0 l15,0 l-4,14" fill="none" stroke="{INK2}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
<text x="492" y="98" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11.5" letter-spacing="1.4" fill="{INK2}">AFVOER</text>
</svg>'''


def sessies():
    """Twaalf sessies, pigment loopt terug."""
    bars = []
    for i in range(12):
        x = 22 + i * 48
        o = max(0.06, 0.92 - i * 0.078)
        bars.append(f'<rect x="{x}" y="{20 + (1-o)*70:.0f}" width="30" height="{max(6,o*90):.0f}" fill="{INK}" opacity="{o:.2f}"/>')
        bars.append(f'<text x="{x+15}" y="130" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif" '
                    f'font-size="11" fill="{INK2}">{i+1}</text>')
    return (f'<svg viewBox="0 0 620 145" role="img" aria-label="Twaalf staven die per sessie lichter worden" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(bars)}'
            f'<line x1="14" y1="114" x2="606" y2="114" stroke="{INK}" stroke-width="1.2"/></svg>')


def stijlen():
    """Drie stijlpanelen naast elkaar."""
    return f'''<svg viewBox="0 0 620 210" role="img" aria-label="Drie panelen: fijn lijnwerk, zwartwerk en kleurwerk" xmlns="http://www.w3.org/2000/svg">
<rect x="4" y="4" width="196" height="160" fill="{PAPER2}" stroke="{RULE}"/>
<rect x="212" y="4" width="196" height="160" fill="{PAPER2}" stroke="{RULE}"/>
<rect x="420" y="4" width="196" height="160" fill="{PAPER2}" stroke="{RULE}"/>
<path d="M40,120 q30,-84 62,-46 q26,31 58,-30" fill="none" stroke="{INK}" stroke-width="1" stroke-linecap="round"/>
<circle cx="102" cy="74" r="20" fill="none" stroke="{INK}" stroke-width="0.9"/>
<circle cx="102" cy="74" r="34" fill="none" stroke="{INK}" stroke-width="0.7" opacity=".6"/>
<path d="M250,132 L310,26 L370,132 z" fill="{INK}"/>
<path d="M282,132 L310,84 L338,132 z" fill="{PAPER2}"/>
<circle cx="310" cy="46" r="7" fill="{PAPER2}"/>
<circle cx="492" cy="76" r="42" fill="{ACC}" opacity=".72"/>
<circle cx="546" cy="96" r="34" fill="{INK}" opacity=".62"/>
<circle cx="516" cy="112" r="24" fill="{ACC2}" opacity=".7"/>
<text x="102" y="192" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif" font-size="12" letter-spacing="1.8" fill="{INK2}">FIJN LIJNWERK</text>
<text x="310" y="192" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif" font-size="12" letter-spacing="1.8" fill="{INK2}">ZWARTWERK</text>
<text x="518" y="192" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif" font-size="12" letter-spacing="1.8" fill="{INK2}">KLEURWERK</text>
</svg>'''


def symbolen():
    """Zes motieftegels."""
    tiles = [
        ("MAAN", f'<path d="M4,-18 a18,18 0 1,0 12,30 a22,22 0 1,1 -12,-30 z" fill="{INK}"/>'),
        ("WOLF", f'<path d="M-18,-12 L-12,-22 L-4,-14 L4,-14 L12,-22 L18,-12 L12,14 L0,22 L-12,14 z" fill="none" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/><path d="M-7,-2 h4 M3,-2 h4" stroke="{ACC}" stroke-width="2.6" stroke-linecap="round"/>'),
        ("ANKER", f'<path d="M0,-16 L0,18 M-14,6 q14,16 28,0 M-10,-6 h20" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/><circle cx="0" cy="-19" r="4.5" fill="none" stroke="{INK}" stroke-width="2.2"/>'),
        ("ROOS", f'<circle cx="0" cy="0" r="6" fill="none" stroke="{ACC}" stroke-width="2"/><path d="M0,-14 a14,14 0 0,1 12,20 a16,16 0 0,1 -26,2 a13,13 0 0,1 8,-21" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>'),
        ("TEKST", f'<path d="M-20,8 q8,-22 18,-2 t14,-6" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/><path d="M-20,16 h40" stroke="{RULE}" stroke-width="2"/>'),
        ("TRIBAL", f'<path d="M-20,14 q10,-30 20,-6 q6,-20 20,-8 q-14,4 -18,16 q-8,-12 -22,-2 z" fill="{INK}"/>'),
    ]
    out = []
    for i, (label, m) in enumerate(tiles):
        x = 8 + i * 101
        out.append(f'<rect x="{x}" y="6" width="93" height="94" fill="{PAPER2}" stroke="{RULE}"/>'
                   f'<g transform="translate({x + 46},53)">{m}</g>'
                   f'<text x="{x + 46}" y="124" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif" '
                   f'font-size="11" letter-spacing="1.6" fill="{INK2}">{label}</text>')
    return (f'<svg viewBox="0 0 620 136" role="img" aria-label="Zes veelgekozen tattoomotieven als tegels" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(out)}</svg>')


def plaatsing():
    """Silhouet met plekken die opvallen."""
    marks = [(150, 96, "HALS"), (206, 168, "ONDERARM"), (96, 168, "HAND"), (150, 250, "BOVENBEEN")]
    m = []
    for x, y, label in marks:
        m.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{ACC}" opacity=".9"/>'
                 f'<circle cx="{x}" cy="{y}" r="14" fill="none" stroke="{ACC}" stroke-width="1" opacity=".5"/>')
    return f'''<svg viewBox="0 0 300 330" role="img" aria-label="Silhouet met de plekken die het meest opvallen" xmlns="http://www.w3.org/2000/svg">
<circle cx="150" cy="46" r="26" fill="none" stroke="{INK}" stroke-width="1.6"/>
<path d="M150,72 L150,88" stroke="{INK}" stroke-width="1.6"/>
<path d="M108,92 q42,-14 84,0 l14,86 l-20,6 l-8,-56 l0,170 l-24,0 l-6,-104 l-6,104 l-24,0 l0,-170 l-8,56 l-20,-6 z"
      fill="{PAPER2}" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"/>
{"".join(m)}
<text x="240" y="100" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11" letter-spacing="1.4" fill="{INK2}">HALS</text>
<text x="240" y="172" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11" letter-spacing="1.4" fill="{INK2}">ARM</text>
<text x="18" y="172" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11" letter-spacing="1.4" fill="{INK2}">HAND</text>
<text x="228" y="254" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11" letter-spacing="1.4" fill="{INK2}">BEEN</text>
</svg>'''


def kaart():
    """Schematische kaart met drie vestigingen."""
    pts = [(180, 60, "AMSTERDAM"), (92, 190, "DEN HAAG"), (196, 216, "ROTTERDAM")]
    g = []
    for x, y, label in pts:
        g.append(f'<circle cx="{x}" cy="{y}" r="8" fill="{ACC}"/>'
                 f'<circle cx="{x}" cy="{y}" r="17" fill="none" stroke="{ACC}" stroke-width="1" opacity=".45"/>'
                 f'<text x="{x + 26}" y="{y + 4}" font-family="ui-sans-serif,system-ui,sans-serif" font-size="12.5" '
                 f'letter-spacing="1.6" fill="{INK}">{label}</text>')
    return f'''<svg viewBox="0 0 420 280" role="img" aria-label="Schematische kaart met Amsterdam, Den Haag en Rotterdam" xmlns="http://www.w3.org/2000/svg">
<path d="M40,30 q26,52 6,96 q-18,40 22,72 q34,28 96,52" fill="none" stroke="{RULE}" stroke-width="2"/>
<path d="M60,26 q40,60 44,120 q4,54 60,110" fill="none" stroke="{RULE}" stroke-width="1"/>
<path d="M180,60 L92,190 L196,216" fill="none" stroke="{INK}" stroke-width="1.2" stroke-dasharray="4 5"/>
{"".join(g)}
<text x="18" y="266" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11" letter-spacing="1.6" fill="{INK2}">RANDSTAD, SCHEMATISCH</text>
</svg>'''


def huidtypen():
    """Zes huidtinten van licht naar donker."""
    tones = ["#f3ded0", "#ecd0b6", "#dcb185", "#c08e5f", "#8d5c36", "#5a3823"]
    out = []
    for i, t in enumerate(tones):
        x = 8 + i * 101
        out.append(f'<rect x="{x}" y="8" width="93" height="58" fill="{t}" stroke="{RULE}"/>'
                   f'<text x="{x + 46}" y="88" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif" '
                   f'font-size="11" letter-spacing="1.6" fill="{INK2}">TYPE {["I","II","III","IV","V","VI"][i]}</text>')
    return (f'<svg viewBox="0 0 620 100" role="img" aria-label="Zes huidtinten van licht naar donker" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(out)}</svg>')


def nazorg():
    """Drie nazorgpunten."""
    return f'''<svg viewBox="0 0 620 150" role="img" aria-label="Drie nazorgpunten: geen fel zonlicht, koelen en de plek droog houden" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(104,58)">
<circle cx="0" cy="0" r="20" fill="none" stroke="{ACC}" stroke-width="2"/>
<g stroke="{ACC}" stroke-width="2" stroke-linecap="round">
<path d="M0,-32 v-9"/><path d="M0,32 v9"/><path d="M-32,0 h-9"/><path d="M32,0 h9"/>
<path d="M-23,-23 l-6,-6"/><path d="M23,23 l6,6"/><path d="M23,-23 l6,-6"/><path d="M-23,23 l-6,6"/>
</g>
<path d="M-34,34 L34,-34" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"/>
</g>
<g transform="translate(310,58)">
<path d="M0,-32 q22,26 22,40 a22,22 0 0,1 -44,0 q0,-14 22,-40 z" fill="none" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
<path d="M-9,10 a9,9 0 0,0 9,9" fill="none" stroke="{ACC}" stroke-width="2" stroke-linecap="round"/>
</g>
<g transform="translate(516,58)">
<rect x="-34" y="-16" width="68" height="32" rx="16" fill="none" stroke="{INK}" stroke-width="2" transform="rotate(-30)"/>
<g fill="{ACC}"><circle cx="-8" cy="-4" r="2.4"/><circle cx="0" cy="2" r="2.4"/><circle cx="8" cy="-2" r="2.4"/><circle cx="-2" cy="-10" r="2.4"/></g>
</g>
<text x="104" y="128" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif" font-size="12" letter-spacing="1.6" fill="{INK2}">GEEN FEL ZONLICHT</text>
<text x="310" y="128" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif" font-size="12" letter-spacing="1.6" fill="{INK2}">KOELEN EN RUST</text>
<text x="516" y="128" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif" font-size="12" letter-spacing="1.6" fill="{INK2}">AFDEKKEN</text>
</svg>'''


def naam():
    """Een naam met een band die er doorheen vervaagt."""
    dots = _dots(21, 150, 470, 66, 106, 120, 0.8, 2.4, .8, .12, ACC)
    return f'''<svg viewBox="0 0 620 160" role="img" aria-label="Een naam in schrijfletters waar het pigment doorheen wegvalt" xmlns="http://www.w3.org/2000/svg">
<text x="60" y="102" font-family="Iowan Old Style,Palatino,Georgia,serif" font-style="italic" font-size="62" fill="{INK}" opacity=".85">Amber</text>
<rect x="150" y="52" width="320" height="66" fill="{PAPER}" opacity=".82"/>
{dots}
<line x1="60" y1="132" x2="560" y2="132" stroke="{RULE}"/>
<text x="60" y="152" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11.5" letter-spacing="1.6" fill="{INK2}">KLEIN VLAK, KORT TRAJECT</text>
</svg>'''


def tijdlijn():
    """Traject over de maanden."""
    out = []
    for i in range(8):
        x = 40 + i * 76
        out.append(f'<circle cx="{x}" cy="60" r="9" fill="{PAPER}" stroke="{ACC}" stroke-width="2"/>'
                   f'<text x="{x}" y="96" text-anchor="middle" font-family="ui-sans-serif,system-ui,sans-serif" '
                   f'font-size="11" letter-spacing="1.2" fill="{INK2}">{["MND 0","MND 2","MND 4","MND 6","MND 8","MND 10","MND 12","MND 14"][i]}</text>')
    return (f'<svg viewBox="0 0 620 110" role="img" aria-label="Tijdlijn met sessies verspreid over ruim een jaar" '
            f'xmlns="http://www.w3.org/2000/svg"><line x1="40" y1="60" x2="572" y2="60" stroke="{RULE}" stroke-width="2"/>'
            f'{"".join(out)}</svg>')


def kleuren():
    """Kleuren en hoe goed ze reageren."""
    rows = [("Zwart en donkerblauw", .95, INK), ("Rood", .7, "#a5322a"),
            ("Groen", .45, "#2f5d3a"), ("Geel en pastel", .25, "#c9a227")]
    out = []
    for i, (label, w, c) in enumerate(rows):
        y = 16 + i * 34
        out.append(f'<text x="0" y="{y + 14}" font-family="ui-sans-serif,system-ui,sans-serif" font-size="12.5" fill="{INK}">{label}</text>'
                   f'<rect x="220" y="{y + 2}" width="380" height="14" fill="{PAPER2}" stroke="{RULE}"/>'
                   f'<rect x="220" y="{y + 2}" width="{380 * w:.0f}" height="14" fill="{c}"/>')
    return (f'<svg viewBox="0 0 620 160" role="img" aria-label="Staven die tonen hoe goed inktkleuren op de laser reageren" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(out)}'
            f'<text x="220" y="156" font-family="ui-sans-serif,system-ui,sans-serif" font-size="11" letter-spacing="1.4" '
            f'fill="{INK2}">REAGEERT GOED  →</text></svg>')


def ornament():
    return (f'<svg viewBox="0 0 620 22" role="presentation" xmlns="http://www.w3.org/2000/svg">'
            f'<line x1="0" y1="11" x2="270" y2="11" stroke="{RULE}"/>'
            f'<line x1="350" y1="11" x2="620" y2="11" stroke="{RULE}"/>'
            f'<path d="M292,11 q9,-9 18,0 t18,0" fill="none" stroke="{ACC}" stroke-width="1.6" stroke-linecap="round"/>'
            f'</svg>')
