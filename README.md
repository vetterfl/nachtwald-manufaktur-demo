# Nachtwald Manufaktur – Demo-Website (Orgon-Akkumulatoren & Orgonit)

Statische, deutschsprachige Demo-Website im Stil eines esoterischen Shops rund um
Orgon-Akkumulatoren, Orgonit-Objekte und Ritualzubehör. **Reine Demo** – keine echten
Produkte, Bestellungen, Zahlungen oder Firmendaten.

## Inhalt

- `index.html` – Startseite / Hero
- `shop.html` – Produktübersicht (6 Demo-Produkte)
- `produkt-*.html` – 6 Produktdetailseiten
- `idee.html` – Historische Einordnung zu Wilhelm Reich & Orgon-Theorie
- `material.html` – Material- und Pflegeübersicht aller Produkte
- `faq.html` – FAQ mit Evidenz-/Wirkungs-Hinweis (Akkordeon)
- `ueber-uns.html` – Fiktive Markengeschichte
- `kontakt.html` – Platzhalter-Kontakt-, Versand- & Rückgabeinfos + Demo-Formular
- `404.html` – Fehlerseite (wird von GitHub Pages automatisch verwendet)
- `css/style.css`, `js/main.js` – Styles & kleine UI-Interaktionen (Mobilmenü, FAQ-Akkordeon, Demo-Warenkorb-Toast, Demo-Formular)
- `assets/favicon.svg`
- `build.py` – Generator-Skript, aus dem alle HTML-Seiten erzeugt werden (gemeinsames Header/Footer/Nav-Template)

Alle internen Links/Pfade (`href`, `src`) sind **relativ** (kein führender `/`), damit die
Seite unverändert unter einem GitHub-Pages-Repository-Unterpfad funktioniert, z. B.
`https://<user>.github.io/<repo>/`.

## Veröffentlichung auf GitHub Pages

1. Dateien dieses Verzeichnisses in ein GitHub-Repository einchecken (Inhalt direkt im
   Root oder z. B. unter `/docs` – je nach Pages-Einstellung).
2. Im Repository: **Settings → Pages → Source**: Branch (z. B. `main`) und Ordner (`/root`
   oder `/docs`) wählen.
3. Da alle Pfade relativ sind, ist **keine Anpassung von `<base>`-Tag oder Pfaden nötig** –
   die Seite funktioniert sowohl unter `https://<user>.github.io/` (User-Page) als auch
   unter `https://<user>.github.io/<repo>/` (Projekt-Page mit Unterpfad).
4. Optional: Build-Skript erneut ausführen, falls Inhalte angepasst werden:
   `python3 build.py`

## Durchgeführte Tests (lokal, Subpath-Simulation `/demo-repo/`)

- **Statische Prüfung:** Python-Skript validiert, dass alle `href`/`src`-Pfade relativ sind
  und auf existierende Dateien zeigen (keine absoluten `/`-Pfade, die unter einem
  Repository-Unterpfad brechen würden) → **OK, 0 Fehler** über alle 14 HTML-Seiten.
- **HTML-Parsing:** `html.parser` über alle 14 Seiten ohne Parse-Fehler.
- **Lokaler Server-Test unter simuliertem Unterpfad** (`python3 -m http.server`, Seite unter
  `/demo-repo/` kopiert, um ein GitHub-Pages-Projekt-Repo nachzubilden):
  - Alle 14 Seiten laden (Status 200), Titel korrekt, CSS/JS laden unter dem Unterpfad ohne
    404 (per `performance.getEntriesByType('resource')` verifiziert).
  - Navigation (Desktop) getestet: Klick auf „Shop“ führt korrekt zu `shop.html`,
    aktiver Menüpunkt wird hervorgehoben.
  - Produktdetailseite getestet (`produkt-2-pyramide.html`): Breadcrumb, Fakten-Grid,
    Demo-Preis-Badge, Pager zu vorherigem/nächstem Produkt.
  - Demo-Warenkorb-Button getestet: Klick zeigt Toast „… zum Demo-Warenkorb hinzugefügt.
    Dies ist keine echte Bestellung.“ – keine echte Funktionalität.
  - FAQ-Akkordeon getestet: Klick öffnet/schliesst Antwort, Inhalt zeigt klaren
    Nicht-Beleg-Hinweis.
  - Mobile Ansicht (390×844, Device-Emulation) getestet: Hamburger-Menü öffnet/schliesst
    korrekt, Navigation per Klick funktioniert, Inhalte reflowen einspaltig.
  - 404-Verhalten geprüft: `404.html` direkt aufrufbar und korrekt gerendert.
  - Nicht vorhandene URL liefert (im lokalen Testserver) einen Fehler; auf GitHub Pages
    übernimmt `404.html` automatisch diese Rolle.
- **Rechtliche/ethische Vorgaben geprüft:** Demo-Badge auf allen Seiten sichtbar,
  Orgon/Orgonit durchgehend als historische/spirituelle Idee bzw. persönliche Überzeugung
  gekennzeichnet, keine Heil-/Diagnose-/Präventionsversprechen, FAQ mit explizitem
  „nicht belegt“-Hinweis, Kontakt-/Versand-/Rückgabedaten ausdrücklich als Platzhalter
  markiert.

## Bekannte Demo-Einschränkungen (bewusst)

- Warenkorb, Checkout und Kontaktformular sind **nicht funktional** (reine UI-Demo).
- Produktbilder sind dekorative SVG-Rosetten statt Fotos (keine Bildrechte/Abhängigkeiten
  nötig).
- Google-Fonts-Einbindung (Cormorant Garamond / Jost) erfordert Internetzugriff beim
  Seitenaufruf; es ist ein System-Serif/Sans-Fallback definiert, falls die Fonts nicht
  laden.
