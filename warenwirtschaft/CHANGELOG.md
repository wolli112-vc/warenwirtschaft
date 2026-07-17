# Changelog

## 1.1.0 - 2026-07-17
- **Einkaufslisten-Integration**: Wenn ein Eintrag auf 0 gesetzt wird, erscheint ein Dialog zur Übernahme in die Einkaufsliste
- **Neuer API-Endpunkt** `POST /api/to-shopping-list`: Schreibt direkt in die Einkaufsliste-JSON mit File-Locking
- **File-Locking** hinzugefügt, um gleichzeitige Schreibzugriffe auf die Einkaufsliste zu verhindern
- Auto-Refresh pausiert automatisch während des Dialogs

## 1.0.10 - 2026-07-17
- **Einträge mit 0 bleiben stehen**: Der `−`-Button setzt die Anzahl auf 0, löscht den Eintrag aber nicht mehr automatisch
- **Löschen nur über ✕**: Einträge können nur noch explizit über den roten ✕-Button entfernt werden
- **Farbcodierung nach Anzahl**: Zeilen mit Anzahl **0** werden rot hinterlegt, Zeilen mit Anzahl **1** orange
- Inline-Edit erlaubt jetzt ebenfalls den Wert 0

## 1.0.9 - 2026-07-13
- **Inline-Edit**: Alle Einträge sind jetzt jederzeit direkt editierbar per Klick auf Anzahl, Produkt, Kategorie oder Verfallsdatum
- **Löschen-Button**: Jede Zeile hat jetzt einen ✕-Button zum direkten Löschen
- **Auto-Refresh**: Daten werden alle 10 Sekunden aktualisiert, pausiert während man editiert
- **Aktualisieren-Button**: 🔄-Button zum manuellen Neuladen
- **Leere-Zustand-Anzeige**: Anzeige "Keine Einträge vorhanden" wenn die Liste leer ist
- "Alles löschen"-Funktion entfernt (bei Inventar-Tracking nicht sinnvoll)

## 1.0.7 - 2026-06-24
- **Kritischer Fix**: Berechtigung `map: share:rw` hinzugefügt – sonst hat das Add-on keinen Zugriff auf den Host-Ordner `/share`
- Daten werden jetzt wirklich außerhalb des Containers gespeichert und überleben Deinstallationen

## 1.0.6 - 2026-06-24
- **Datenspeicherung** umgestellt auf `/share/inventory_manager/inventory.json`
- Daten überleben jetzt **auch bei Deinstallation** des Add-ons (neuinstallation + Updates)
- Automatische **Migration** vorhandener Daten aus `/data` nach `/share` beim ersten Start
- Der Schieber "App Daten ebenfalls entfernen" wirkt sich nicht mehr auf die Inventardaten aus

## 1.0.5 - 2026-06-24
- Neue Spalte **Kategorie** hinzugefügt
- Kategorien sind **frei eingebbar** (Textfeld) mit Vorschlägen aus bestehenden Kategorien (Datalist)
- Produkte werden nach **Kategorie gruppiert** und sortiert angezeigt
- Kategorie-Gruppen sind visuell hervorgehoben (blaue Header-Zeile)
- Suche erweitert: Filtert jetzt auch nach Kategorie
- Neue API-Endpunkte: `GET /api/categories` für Kategorie-Vorschläge

## 1.0.4 - 2026-06-24
- Stabiles Release mit persistenter Datenhaltung, Ingress-Support und Funktions-Update
- JSON-Daten werden unter `/data/inventory.json` gespeichert
- Relative API-Pfade für korrekte Ingress-Funktionalität
- Visuelle Warnung bei Verfallsdaten (rot/gelb)
- Suchfunktion über Produktliste
- Direkte Mengensteuerung per `+`/`-` Buttons

## 1.0.3 - 2026-06-24
- Aktualisierung von app.py in app, config.yaml

## 1.0.2 - 2026-06-24
- Aktualisierung von index.html in app

## 1.0.1 - 2026-06-24
- Aktualisierung von build.yaml config.yaml Dockerfile

## 1.0 – 2026-06-24
- Erstveröffentlichung des Add-Ons
