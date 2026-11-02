#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator fuer die statische Demo-Website 'Nachtwald Manufaktur'.
Erzeugt alle HTML-Seiten aus gemeinsamen Templates (Header/Footer/Nav),
damit Navigation und Fusszeile auf allen Seiten konsistent sind.
Alle Pfade sind RELATIV, damit die Seite unter einem GitHub-Pages
Repository-Unterpfad (z.B. https://user.github.io/repo/) funktioniert.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [
    ("index.html", "Start"),
    ("shop.html", "Shop"),
    ("idee.html", "Die Idee"),
    ("material.html", "Material & Handwerk"),
    ("faq.html", "FAQ"),
    ("ueber-uns.html", "Über uns"),
    ("kontakt.html", "Kontakt"),
]

PRODUCTS = [
    {
        "slug": "produkt-1-schichtbox",
        "name": "Reich'sche Schichtbox – Tischmodell",
        "price": "289,00",
        "short": "Dekoratives Sammlerstück im Stil der historischen Orgon-Akkumulator-Konstruktion.",
        "material": "Abwechselnde Lagen aus Fichtenholz und Stahlwolle, Kupferverkleidung innen, geölte Oberfläche",
        "masse": "49 × 29 × 29 cm, Gewicht ca. 9,2 kg",
        "beschreibung": (
            "Diese Tischmodell-Box ist dem historischen Aufbau eines Orgon-Akkumulators nach "
            "Wilhelm Reich nachempfunden: abwechselnde organische (Holz) und metallische "
            "(Stahlwolle, Kupfer) Schichten in einem schlichten Gehäuse. Sie wird als "
            "<strong>dekoratives Sammler- und Demonstrationsobjekt</strong> verkauft, nicht als "
            "medizinisches oder therapeutisches Gerät."
        ),
        "pflege": "Trocken und staubfrei lagern, Holzoberfläche gelegentlich mit Möbelöl pflegen, keine scharfen Reiniger verwenden.",
    },
    {
        "slug": "produkt-2-pyramide",
        "name": "Orgonit-Pyramide „Sternenklang“",
        "price": "24,90",
        "short": "Kleine Harzpyramide mit Kupferspänen und Bergkristall – Fenster- oder Schreibtischobjekt.",
        "material": "Gussharz, Kupferspäne, facettierter Bergkristall, Metallgrundlage",
        "masse": "Kantenlänge ca. 7 cm, Gewicht ca. 180 g",
        "beschreibung": (
            "Von Hand gegossene Dekopyramide aus Kunstharz mit eingearbeiteten Kupferspänen und "
            "einer kleinen Bergkristallspitze. Viele Anhänger der Orgonit-Idee verbinden solche "
            "Objekte symbolisch mit Ausgleich und Konzentration – das ist eine "
            "<em>persönliche Glaubens- und Deutungsfrage</em>, keine belegte physikalische oder "
            "gesundheitliche Wirkung."
        ),
        "pflege": "Mit weichem, trockenem Tuch abwischen, direkte Sonneneinstrahlung über längere Zeit vermeiden (Harz kann vergilben).",
    },
    {
        "slug": "produkt-3-anhaenger",
        "name": "Taschen-Orgonit Anhänger „Mondphase“",
        "price": "19,90",
        "short": "Kleiner Anhänger mit Amethyst und Messingspänen an einer Lederkordel.",
        "material": "Gussharz, Messingspäne, Amethyst-Trommelstein, Lederkordel (verstellbar)",
        "masse": "Anhänger ca. 2,5 cm, Kordellänge verstellbar bis 70 cm",
        "beschreibung": (
            "Handlicher Anhänger zum Mitnehmen, inspiriert von der Mondphasen-Symbolik. Ein "
            "schönes Alltagsobjekt für alle, die sich für Ritual- und Meditationsaccessoires "
            "interessieren. Es werden <strong>keine</strong> Heil-, Schutz- oder "
            "Energieversprechen gemacht."
        ),
        "pflege": "Nicht dauerhaft mit Wasser in Kontakt bringen, Lederkordel bei Bedarf austauschen (Ersatz separat erhältlich).",
    },
    {
        "slug": "produkt-4-untersetzer",
        "name": "Orgonit-Untersetzer-Set „Wurzelkreis“ (4 Stück)",
        "price": "34,90",
        "short": "Set aus vier Untersetzern mit Kupfereinschlüssen und Rosenquarz-Splittern.",
        "material": "Gussharz, Kupferdraht, Rosenquarz-Splitter, Korkboden",
        "masse": "Durchmesser je 10 cm, Set à 4 Stück",
        "beschreibung": (
            "Diese vier Untersetzer eignen sich für Tassen, Kerzen oder kleine Deko-Objekte und "
            "tragen das charakteristische Orgonit-Muster aus Kupfer und Rosenquarz. Rein "
            "dekorativ und funktional als Untersetzer – ohne Anspruch auf eine messbare "
            "energetische Wirkung."
        ),
        "pflege": "Korkboden trocken halten, Flecken vorsichtig mit feuchtem Tuch entfernen.",
    },
    {
        "slug": "produkt-5-raeucherwerk",
        "name": "Räucherwerk-Set „Waldnacht“",
        "price": "16,90",
        "short": "Harzweihrauch, Palo-Santo-Stäbchen und eine kleine Holzschale für Ritualräume.",
        "material": "Naturharz-Weihrauch, Palo-Santo-Holz, Schale aus Mangoholz",
        "masse": "Schale Ø 9 cm, Inhalt ca. 40 g Räucherwerk",
        "beschreibung": (
            "Ein stimmungsvolles Set für Räucherrituale und ruhige Momente. Räucherwerk kann "
            "Rauch und Geruch erzeugen – bitte für ausreichende Belüftung sorgen und von "
            "brennbaren Materialien fernhalten."
        ),
        "pflege": "Schale nach Gebrauch auskühlen lassen, an einem gut belüfteten, trockenen Ort verwenden.",
    },
    {
        "slug": "produkt-6-journal",
        "name": "Ritual-Journal „Feldnotizen“",
        "price": "22,50",
        "short": "Leinengebundenes Notizbuch für Beobachtungen, Rituale und persönliche Reflexionen.",
        "material": "Leineneinband, 128 Seiten 120g Recyclingpapier, Lesebändchen",
        "masse": "Format A5, 128 Seiten",
        "beschreibung": (
            "Ein schlichtes, hochwertig gebundenes Journal, um eigene Beobachtungen, Gedanken "
            "oder Ritualnotizen festzuhalten. Vorne enthält es eine kurze, neutral gehaltene "
            "Zeitleiste zur Geschichte der Orgon-Theorie zum Nachschlagen."
        ),
        "pflege": "Vor Feuchtigkeit schützen, nicht direkt in praller Sonne lagern (Farbechtheit des Einbands).",
    },
]

FONT_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&'
    'family=Jost:wght@400;500&display=swap" rel="stylesheet">'
)

DEMO_BADGE_HTML = (
    '<div class="demo-banner" role="note">'
    '<span class="demo-banner__dot" aria-hidden="true"></span>'
    'Shop-Demo &ndash; fiktive Marke, keine echten Bestellungen, keine Zahlungsdaten erforderlich.'
    "</div>"
)


def moon_svg():
    return (
        '<svg class="deco-moons" viewBox="0 0 400 60" preserveAspectRatio="xMidYMid meet" '
        'aria-hidden="true" focusable="false">'
        '<g fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.55">'
        '<circle cx="30" cy="30" r="18"/>'
        '<path d="M90 12a18 18 0 0 0 0 36 14 14 0 0 1 0-36z" fill="currentColor" stroke="none"/>'
        '<path d="M150 12a18 18 0 1 0 0 36 13 18 0 0 1 0-36z" fill="currentColor" stroke="none" opacity="0.85"/>'
        '<circle cx="210" cy="30" r="18" fill="currentColor" stroke="none"/>'
        '<path d="M270 12a18 18 0 1 1 0 36 13 18 0 0 0 0-36z" fill="currentColor" stroke="none" opacity="0.85"/>'
        '<path d="M330 12a18 18 0 0 1 0 36 14 14 0 0 0 0-36z" fill="currentColor" stroke="none"/>'
        '<circle cx="390" cy="30" r="18"/>'
        "</g></svg>"
    )


def rosette_svg(cls="deco-rosette"):
    import math
    circles = ""
    for a in range(0, 360, 60):
        cx = 100 + 60 * math.cos(math.radians(a))
        cy = 100 + 60 * math.sin(math.radians(a))
        circles += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="40"/>'
    return (
        f'<svg class="{cls}" viewBox="0 0 200 200" aria-hidden="true" focusable="false">'
        '<g fill="none" stroke="currentColor" stroke-width="1">'
        '<circle cx="100" cy="100" r="80"/>'
        '<circle cx="100" cy="100" r="60"/>'
        '<circle cx="100" cy="100" r="40"/>'
        + circles
        + "</g></svg>"
    )


def page_shell(title, description, active_href, body_html, extra_head="", canonical_rel="."):
    nav_links = "\n".join(
        f'<li><a href="{href}"{" class=\"is-active\" aria-current=\"page\"" if href == active_href else ""}>{label}</a></li>'
        for href, label in NAV_ITEMS
    )
    year = 2026
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Nachtwald Manufaktur (Demo)</title>
<meta name="description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="css/style.css">
{FONT_LINK}
{extra_head}
</head>
<body>
<a class="skip-link" href="#inhalt">Zum Inhalt springen</a>
{DEMO_BADGE_HTML}
<header class="site-header">
  <div class="wrap site-header__bar">
    <a class="brand" href="index.html">
      <span class="brand__mark" aria-hidden="true">&#9790;</span>
      <span class="brand__text">Nachtwald<br><small>Manufaktur</small></span>
    </a>
    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="siteNav">
      <span></span><span></span><span></span>
      <span class="sr-only">Menü öffnen</span>
    </button>
    <nav class="site-nav" id="siteNav" aria-label="Hauptnavigation">
      <ul>
      {nav_links}
      </ul>
    </nav>
  </div>
</header>
<main id="inhalt">
{body_html}
</main>
<footer class="site-footer">
  <div class="wrap site-footer__grid">
    <div>
      <div class="brand brand--footer"><span class="brand__mark" aria-hidden="true">&#9790;</span> Nachtwald Manufaktur</div>
      <p>Fiktive Demo-Marke für Orgon-Akkumulatoren, Orgonit-Objekte und Ritualzubehör. Alle Produkte, Preise und Texte dienen ausschliesslich Demonstrationszwecken.</p>
    </div>
    <div>
      <h2>Navigation</h2>
      <ul class="footer-links">
        {''.join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV_ITEMS)}
      </ul>
    </div>
    <div>
      <h2>Hinweis</h2>
      <p>Diese Website ist eine <strong>nicht-kommerzielle Demo</strong>. Historische und spirituelle Vorstellungen rund um „Orgon“ werden erläutert, aber nicht als belegte Tatsachen oder medizinische Wirkung dargestellt. Weitere Einordnung: <a href="faq.html">FAQ</a>.</p>
    </div>
  </div>
  <div class="wrap site-footer__bottom">
    <p>&copy; {year} Nachtwald Manufaktur (Demo-Projekt). Alle Angaben ohne Gewähr, keine echte Geschäftstätigkeit.</p>
  </div>
</footer>
<script src="js/main.js" defer></script>
</body>
</html>
"""


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("geschrieben:", path)


# ---------------------------------------------------------------- index.html
def build_index():
    product_cards = "\n".join(
        f"""
        <article class="product-card">
          <div class="product-card__media" aria-hidden="true">{rosette_svg('deco-rosette--card')}</div>
          <h3>{p['name']}</h3>
          <p class="product-card__short">{p['short']}</p>
          <p class="product-card__price">{p['price']} &euro;</p>
          <a class="btn btn--ghost" href="{p['slug']}.html">Details ansehen</a>
        </article>"""
        for p in PRODUCTS[:3]
    )
    body = f"""
<section class="hero">
  <div class="wrap hero__inner">
    <div class="hero__text">
      <p class="eyebrow">Demo-Manufaktur &middot; Objekte mit Geschichte</p>
      <h1>Räume für Rituale,<br>Objekte mit Geschichte.</h1>
      <p class="lead">Nachtwald Manufaktur zeigt &ndash; als Demo-Projekt &ndash; wie ein Online-Shop
      rund um Orgon-Akkumulatoren, Orgonit-Objekte und Ritualzubehör aussehen könnte.
      „Orgon“ bezeichnet eine historische, hypothetische Lebensenergie-Idee des Psychoanalytikers
      Wilhelm Reich &ndash; keine anerkannte physikalische Grösse.</p>
      <div class="hero__actions">
        <a class="btn btn--primary" href="shop.html">Shop entdecken</a>
        <a class="btn btn--ghost" href="idee.html">Die Idee verstehen</a>
      </div>
    </div>
    <div class="hero__deco" aria-hidden="true">{rosette_svg('deco-rosette--hero')}</div>
  </div>
  {moon_svg()}
</section>

<section class="section">
  <div class="wrap">
    <h2 class="section__title">Ausgewählte Demo-Produkte</h2>
    <p class="section__intro">Eine kleine Auswahl erfundener Produkte zur Veranschaulichung. Materialangaben
    sind sachlich formuliert, symbolische Bedeutungen klar als Überzeugung gekennzeichnet.</p>
    <div class="product-grid product-grid--preview">
      {product_cards}
    </div>
    <div class="section__cta">
      <a class="btn btn--primary" href="shop.html">Alle Produkte ansehen</a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap two-col">
    <div>
      <h2 class="section__title">Die Idee hinter dem Akkumulator</h2>
      <p>In den 1930er&ndash;1950er Jahren entwickelte der Psychoanalytiker Wilhelm Reich die Vorstellung
      einer universellen Lebensenergie, die er „Orgon“ nannte, und konstruierte Kästen aus
      abwechselnden organischen und metallischen Schichten, um sie angeblich zu sammeln.</p>
      <p>Diese Theorie wird von der etablierten Wissenschaft nicht anerkannt. Wir erzählen die
      Geschichte dieser Idee &ndash; als kulturelles und historisches Phänomen, nicht als
      medizinischen Ratschlag.</p>
      <a class="link-arrow" href="idee.html">Mehr zur Geschichte &rarr;</a>
    </div>
    <div>
      <h2 class="section__title">Material &amp; Handwerk</h2>
      <p>Jedes Demo-Produkt wird mit nachvollziehbaren, prüfbaren Merkmalen beschrieben: verwendete
      Materialien, Masse, Gewicht und Pflegehinweise &ndash; ohne Wirkversprechen.</p>
      <a class="link-arrow" href="material.html">Zu Material &amp; Handwerk &rarr;</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap callout">
    <h2>Wichtiger Hinweis</h2>
    <p>Diese Website ist eine <strong>Demo</strong> ohne reale Produkte, Bestellungen oder Zahlungen.
    Spirituelle und historische Aussagen zu „Orgon“ sind als Überzeugungen bzw. historische
    Einordnung gekennzeichnet und stellen <strong>keine</strong> belegte gesundheitliche Wirkung dar.
    Ausführliche Einordnung siehe <a href="faq.html">FAQ</a>.</p>
  </div>
</section>
"""
    return page_shell(
        "Start",
        "Demo-Website eines Esoterik-Shops rund um Orgon-Akkumulatoren, Orgonit und Ritualzubehör.",
        "index.html",
        body,
    )


# ----------------------------------------------------------------- shop.html
def build_shop():
    cards = "\n".join(
        f"""
        <article class="product-card">
          <div class="product-card__media" aria-hidden="true">{rosette_svg('deco-rosette--card')}</div>
          <h3>{p['name']}</h3>
          <p class="product-card__short">{p['short']}</p>
          <p class="product-card__meta">{p['material']}</p>
          <p class="product-card__price">{p['price']} &euro;</p>
          <div class="product-card__actions">
            <a class="btn btn--ghost" href="{p['slug']}.html">Details ansehen</a>
            <button type="button" class="btn btn--primary btn--cart" data-demo-cart data-product="{p['name']}">In den Warenkorb</button>
          </div>
        </article>"""
        for p in PRODUCTS
    )
    body = f"""
<section class="page-header">
  <div class="wrap">
    <p class="eyebrow">Shop-Demo</p>
    <h1>Alle Demo-Produkte</h1>
    <p class="lead">Sechs erfundene Produkte zur Veranschaulichung. Warenkorb und Checkout sind
    <strong>nicht funktional</strong> &ndash; es werden keine echten Bestellungen entgegengenommen.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="product-grid">
      {cards}
    </div>
  </div>
</section>
<div class="cart-toast" id="cartToast" role="status" aria-live="polite" hidden></div>
"""
    return page_shell(
        "Shop",
        "Übersicht aller Demo-Produkte: Orgon-Akkumulatoren, Orgonit-Objekte und Ritualzubehör.",
        "shop.html",
        body,
    )


# ----------------------------------------------------------- product pages
def build_product(p, prev_p, next_p):
    body = f"""
<section class="section product-detail">
  <div class="wrap">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="index.html">Start</a> &rsaquo; <a href="shop.html">Shop</a> &rsaquo; <span>{p['name']}</span>
    </nav>
    <div class="product-detail__grid">
      <div class="product-detail__media" aria-hidden="true">{rosette_svg('deco-rosette--detail')}</div>
      <div class="product-detail__info">
        <h1>{p['name']}</h1>
        <p class="product-detail__price">{p['price']} &euro; <span class="demo-tag">Demo-Preis</span></p>
        <p class="lead">{p['short']}</p>
        <div class="product-detail__facts">
          <div><span>Material</span><p>{p['material']}</p></div>
          <div><span>Maße</span><p>{p['masse']}</p></div>
        </div>
        <button type="button" class="btn btn--primary btn--cart" data-demo-cart data-product="{p['name']}">In den Warenkorb (Demo)</button>
        <p class="fineprint">Demo-Funktion: Es wird kein echter Kauf ausgelöst, keine Zahlungs- oder Adressdaten werden erhoben.</p>
      </div>
    </div>

    <div class="product-detail__tabs">
      <article>
        <h2>Beschreibung</h2>
        <p>{p['beschreibung']}</p>
      </article>
      <article>
        <h2>Pflegehinweise</h2>
        <p>{p['pflege']}</p>
      </article>
      <article class="callout callout--small">
        <h2>Einordnung</h2>
        <p>Symbolische oder spirituelle Bedeutungen, die manche Anhänger diesem Objekt zuschreiben,
        sind persönliche Überzeugungen. Eine belegte physikalische oder gesundheitliche Wirkung
        besteht nicht. Mehr dazu in den <a href="faq.html">FAQ</a>.</p>
      </article>
    </div>

    <nav class="product-pager" aria-label="Weitere Produkte">
      <a href="{prev_p['slug']}.html">&larr; {prev_p['name']}</a>
      <a href="shop.html">Zur Shop-Übersicht</a>
      <a href="{next_p['slug']}.html">{next_p['name']} &rarr;</a>
    </nav>
  </div>
</section>
<div class="cart-toast" id="cartToast" role="status" aria-live="polite" hidden></div>
"""
    return page_shell(p["name"], p["short"], p["slug"] + ".html", body)


# ------------------------------------------------------------------ idee.html
def build_idee():
    body = """
<section class="page-header">
  <div class="wrap">
    <p class="eyebrow">Hintergrund</p>
    <h1>Die Idee hinter dem Akkumulator</h1>
    <p class="lead">Eine kurze, neutrale historische Einordnung &ndash; kein medizinischer Ratschlag.</p>
  </div>
</section>
<section class="section">
  <div class="wrap prose">
    <p>Der Begriff <strong>„Orgon“</strong> geht auf den österreichisch-amerikanischen Psychoanalytiker
    <strong>Wilhelm Reich</strong> (1897&ndash;1957) zurück. Ab den 1930er Jahren entwickelte Reich die
    Vorstellung einer universellen, angeblich messbaren Lebensenergie, die er als Grundlage für
    biologische und sogar kosmische Vorgänge ansah.</p>
    <p>In den 1940er Jahren baute Reich sogenannte <strong>Orgon-Akkumulatoren</strong>: Kästen aus
    abwechselnden Schichten organischer Materialien (z. B. Holz, Watte) und metallischer Materialien
    (z. B. Stahlwolle, Blech). Die Grundannahme war, dass sich Orgon-Energie in solchen Schichten
    konzentrieren liesse.</p>
    <p>Diese Konstruktionen und die zugrunde liegende Theorie werden von der etablierten Physik und
    Medizin <strong>nicht anerkannt</strong>. US-Behörden untersagten in den 1950er Jahren den Verkauf
    von Orgon-Akkumulatoren mit Gesundheitsversprechen; das Thema bleibt bis heute wissenschaftlich
    umstritten und gilt überwiegend als widerlegt bzw. nicht belegbar.</p>
    <p>Auf dieser Demo-Website wird die Geschichte dieser Idee aus kulturhistorischem Interesse
    erzählt. Produkte, die sich auf „Orgon“ oder „Orgonit“ beziehen, werden als
    <strong>Deko-, Sammler- oder Ritualobjekte</strong> beschrieben &ndash; nicht als Mittel mit
    nachgewiesener physikalischer oder gesundheitlicher Wirkung.</p>
    <h2>Orgonit: eine spätere, inoffizielle Weiterentwicklung</h2>
    <p>„Orgonit“ ist kein Begriff von Wilhelm Reich selbst, sondern eine spätere, informelle
    Weiterentwicklung aus der New-Age- und Esoterik-Szene: ein Gemisch aus Kunstharz, Metallspänen
    und oft Kristallen, das gegossen wird. Auch hierzu existiert keine wissenschaftlich anerkannte
    Wirkungsgrundlage &ndash; es handelt sich um ein Glaubens- und Deko-Konzept.</p>
    <p><a class="link-arrow" href="faq.html">Häufige Fragen &amp; Einordnung ansehen &rarr;</a></p>
  </div>
</section>
"""
    return page_shell(
        "Die Idee",
        "Neutrale historische Einordnung zu Wilhelm Reich, Orgon-Theorie und Orgon-Akkumulatoren.",
        "idee.html",
        body,
    )


# -------------------------------------------------------------- material.html
def build_material():
    rows = "\n".join(
        f"<tr><td>{p['name']}</td><td>{p['material']}</td><td>{p['masse']}</td></tr>" for p in PRODUCTS
    )
    body = f"""
<section class="page-header">
  <div class="wrap">
    <p class="eyebrow">Transparenz</p>
    <h1>Material &amp; Handwerk</h1>
    <p class="lead">Sachliche, prüfbare Angaben zu Materialien und Massen aller Demo-Produkte.</p>
  </div>
</section>
<section class="section">
  <div class="wrap prose">
    <p>Wir legen Wert darauf, Materialien und Verarbeitung so konkret wie möglich zu beschreiben, statt
    vage Wirkungsversprechen zu machen. Die folgende Übersicht fasst alle Demo-Produkte zusammen.</p>
    <div class="table-wrap">
      <table class="data-table">
        <thead><tr><th>Produkt</th><th>Material</th><th>Masse</th></tr></thead>
        <tbody>
        {rows}
        </tbody>
      </table>
    </div>
    <h2>Allgemeine Pflegehinweise</h2>
    <ul>
      <li>Harzobjekte (Orgonit) vor dauerhafter, intensiver Sonneneinstrahlung schützen.</li>
      <li>Holzobjekte trocken lagern und gelegentlich mit Möbelöl pflegen.</li>
      <li>Kordeln und Textilteile nicht dauerhaft nass werden lassen.</li>
      <li>Räucherwerk nur in gut belüfteten Räumen und auf feuerfester Unterlage verwenden.</li>
    </ul>
  </div>
</section>
"""
    return page_shell(
        "Material & Handwerk",
        "Materialien, Masse und Pflegehinweise aller Demo-Produkte im Überblick.",
        "material.html",
        body,
    )


# -------------------------------------------------------------------- faq.html
def build_faq():
    faqs = [
        (
            "Ist eine Wirkung von Orgon-Akkumulatoren oder Orgonit wissenschaftlich belegt?",
            "Nein. Es gibt keine von der etablierten Wissenschaft anerkannte, reproduzierbare "
            "Evidenz für eine physikalische oder gesundheitliche Wirkung von Orgon-Akkumulatoren "
            "oder Orgonit-Objekten. Manche Anhänger verbinden damit persönliche Erfahrungen oder "
            "symbolische Bedeutungen &ndash; das bleibt eine individuelle Überzeugung, keine "
            "belegte Tatsache.",
        ),
        (
            "Können diese Produkte Krankheiten heilen, vorbeugen oder diagnostizieren?",
            "Nein. Wir machen und unterstützen keine Heil-, Diagnose-, Präventions-, "
            "Entgiftungs-, Immunitäts- oder Strahlenschutzversprechen. Diese Produkte sind als "
            "Deko-, Sammler- oder Ritualobjekte gedacht.",
        ),
        (
            "Sollte ich eine medizinische Behandlung durch diese Produkte ersetzen?",
            "Nein, unter keinen Umständen. Bei gesundheitlichen Anliegen sollte stets "
            "qualifiziertes medizinisches Fachpersonal konsultiert werden. Diese Produkte sind "
            "kein Ersatz für Diagnose oder Behandlung.",
        ),
        (
            "Ist dieser Shop echt? Kann ich hier wirklich bestellen?",
            "Nein. Diese gesamte Website ist eine <strong>Demo</strong> zu Design- und "
            "Entwicklungszwecken. „Nachtwald Manufaktur“ ist eine fiktive Marke, es gibt keine "
            "echten Produkte, Bestellungen, Zahlungen oder Lieferungen.",
        ),
        (
            "Warum wird die Geschichte von Wilhelm Reich und Orgon trotzdem erzählt?",
            "Weil sie ein interessantes kulturhistorisches Phänomen ist und erklärt, woher die "
            "verwendeten Begriffe und Formen stammen. Die historische Einordnung erfolgt bewusst "
            "neutral, siehe <a href=\"idee.html\">Die Idee</a>.",
        ),
    ]
    items = "\n".join(
        f"""
        <div class="faq-item">
          <button type="button" class="faq-item__question" aria-expanded="false">
            <span>{q}</span>
            <span class="faq-item__icon" aria-hidden="true">+</span>
          </button>
          <div class="faq-item__answer"><p>{a}</p></div>
        </div>"""
        for q, a in faqs
    )
    body = f"""
<section class="page-header">
  <div class="wrap">
    <p class="eyebrow">Einordnung</p>
    <h1>FAQ &amp; Evidenz-Hinweis</h1>
    <p class="lead">Offene Antworten zu Wirkungsfragen, Belegen und zum Demo-Charakter dieser Seite.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="callout">
      <h2>Kurz gesagt</h2>
      <p>Manche Anhänger verbinden Orgon-Akkumulatoren und Orgonit-Objekte mit persönlichem
      Wohlbefinden oder symbolischer Bedeutung &ndash; eine spezifische physikalische oder
      gesundheitliche Wirkung ist <strong>nicht belegt</strong>. Diese Seite ist zudem eine
      <strong>Demo</strong> ohne reale Geschäftstätigkeit.</p>
    </div>
    <div class="faq-list">
      {items}
    </div>
  </div>
</section>
"""
    return page_shell(
        "FAQ",
        "Häufige Fragen zu Evidenz, Wirkung und zum Demo-Charakter der Website.",
        "faq.html",
        body,
    )


# ---------------------------------------------------------------- ueber-uns.html
def build_ueber_uns():
    body = """
<section class="page-header">
  <div class="wrap">
    <p class="eyebrow">Fiktive Marke</p>
    <h1>Über Nachtwald Manufaktur</h1>
    <p class="lead">Eine erfundene Manufaktur-Geschichte, erzählt für diese Demo-Website.</p>
  </div>
</section>
<section class="section">
  <div class="wrap prose">
    <p><strong>Nachtwald Manufaktur</strong> ist eine fiktive Marke, die ausschliesslich für diese
    Demo-Website erfunden wurde. Es gibt keine echte Werkstatt, kein echtes Team und keine echten
    Bestellungen.</p>
    <p>In der erzählten Demo-Geschichte entstand die Idee in einer kleinen Werkstatt am Waldrand,
    in der Holzobjekte und Harzgüsse von Hand gefertigt werden. Das Sortiment vereint Objekte rund
    um die historische Orgon-Theorie, Orgonit-Deko sowie klassisches Ritual- und
    Meditationszubehör.</p>
    <h2>Unsere (fiktiven) Grundsätze</h2>
    <ul>
      <li>Ehrliche, nachprüfbare Materialangaben statt vager Versprechen.</li>
      <li>Klare Trennung zwischen Symbolik/Überzeugung und belegten Fakten.</li>
      <li>Keine Darstellung gesundheitlicher Wirkungen als Tatsache.</li>
    </ul>
    <p class="fineprint">Alle Angaben zu Team, Werkstatt und Firmengeschichte sind erfundene
    Demo-Inhalte und erheben keinen Anspruch auf Realität.</p>
  </div>
</section>
"""
    return page_shell(
        "Über uns",
        "Fiktive Markengeschichte von Nachtwald Manufaktur für diese Demo-Website.",
        "ueber-uns.html",
        body,
    )


# ------------------------------------------------------------------- kontakt.html
def build_kontakt():
    body = """
<section class="page-header">
  <div class="wrap">
    <p class="eyebrow">Beispieldaten</p>
    <h1>Kontakt, Versand &amp; Rückgabe</h1>
    <p class="lead">Alle folgenden Angaben sind Platzhalter- bzw. Beispieldaten für diese Demo.</p>
  </div>
</section>
<section class="section">
  <div class="wrap two-col">
    <div>
      <h2>Kontakt (Platzhalter)</h2>
      <p>Nachtwald Manufaktur (Demo)<br>
      Musterweg 12, 12345 Musterstadt<br>
      E-Mail: <a href="mailto:demo@nachtwald-manufaktur.example">demo@nachtwald-manufaktur.example</a><br>
      Telefon: 0000 / 000000 (Beispielnummer)</p>
      <p class="fineprint">Diese Kontaktdaten sind frei erfunden und führen zu keiner echten
      Annahmestelle.</p>

      <form class="demo-form" data-demo-form aria-label="Demo-Kontaktformular">
        <h2>Demo-Kontaktformular</h2>
        <label>Name
          <input type="text" name="name" placeholder="Ihr Name" autocomplete="off">
        </label>
        <label>E-Mail
          <input type="email" name="email" placeholder="ihre@email.example" autocomplete="off">
        </label>
        <label>Nachricht
          <textarea name="message" rows="4" placeholder="Ihre Nachricht (wird nicht versendet)"></textarea>
        </label>
        <button type="submit" class="btn btn--primary">Demo-Nachricht senden</button>
        <p class="fineprint">Dieses Formular ist nicht funktional. Es werden keine Daten
        gespeichert oder übertragen.</p>
      </form>
    </div>
    <div>
      <h2>Versand (Beispiel)</h2>
      <p>Versand innerhalb Deutschlands (Beispiel): 2&ndash;4 Werktage, Versandkosten 4,90 &euro;,
      kostenfrei ab 60 &euro; Bestellwert. Es handelt sich um fiktive Beispielwerte.</p>
      <h2>Rückgabe (Beispiel)</h2>
      <p>Beispielhaftes 14-tägiges Rückgaberecht ab (fiktivem) Erhalt der Ware, Ware unbenutzt und
      in Originalverpackung. Da keine echten Bestellungen stattfinden, hat diese Angabe rein
      illustrativen Charakter.</p>
    </div>
  </div>
</section>
<div class="cart-toast" id="cartToast" role="status" aria-live="polite" hidden></div>
"""
    return page_shell(
        "Kontakt",
        "Platzhalter-Kontakt-, Versand- und Rückgabeinformationen für die Demo.",
        "kontakt.html",
        body,
    )


# --------------------------------------------------------------------- 404.html
def build_404():
    body = """
<section class="section" style="padding-top:6rem;padding-bottom:6rem;text-align:center;">
  <div class="wrap">
    <p class="eyebrow">404</p>
    <h1>Diese Seite wurde nicht gefunden</h1>
    <p class="lead">Der gesuchte Pfad existiert in dieser Demo nicht. Zurück zur <a href="index.html">Startseite</a>
    oder zum <a href="shop.html">Shop</a>.</p>
  </div>
</section>
"""
    return page_shell("Seite nicht gefunden", "404 – Seite nicht gefunden.", "", body)


def main():
    write("index.html", build_index())
    write("shop.html", build_shop())
    write("idee.html", build_idee())
    write("material.html", build_material())
    write("faq.html", build_faq())
    write("ueber-uns.html", build_ueber_uns())
    write("kontakt.html", build_kontakt())
    write("404.html", build_404())
    n = len(PRODUCTS)
    for i, p in enumerate(PRODUCTS):
        prev_p = PRODUCTS[(i - 1) % n]
        next_p = PRODUCTS[(i + 1) % n]
        write(p["slug"] + ".html", build_product(p, prev_p, next_p))


if __name__ == "__main__":
    main()
