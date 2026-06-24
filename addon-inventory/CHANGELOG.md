# Changelog

## 1.0 – 2026-06-24
- Erstveröffentlichung des Add-Ons

## 1.0.1 - 2026-06-24
- Aktualisierung von build.yaml config.yaml Dockerfile

## 1.0.2 - 2026-06-24
- Aktualisierung von index.html in app

## 1.0.3 - 2026-06-24
- Aktualisierung von app.py in app, config.yaml 

## 1.0.4 - 2026-06-24
- Stabiles Release mit persistenter Datenhaltung, Ingress-Support und Funktions-Update
- JSON-Daten werden unter `/data/inventory.json` gespeichert
- Relative API-Pfade für korrekte Ingress-Funktionalität
- Visuelle Warnung bei Verfallsdaten (rot/gelb)
- Suchfunktion über Produktliste
- Direkte Mengensteuerung per `+`/`-` Buttons

## 1.0.5 - 2026-06-24
- Neue Spalte **Kategorie** hinzugefügt
- Kategorien sind **frei eingebbar** (Textfeld) mit Vorschlägen aus bestehenden Kategorien (Datalist)
- Produkte werden nach **Kategorie gruppiert** und sortiert angezeigt
- Kategorie-Gruppen sind visuell hervorgehoben (blaue Header-Zeile)
- Suche erweitert: Filtert jetzt auch nach Kategorie
- Neue API-Endpunkte: `GET /api/categories` für Kategorie-Vorschläge 
