# 1. Aufgabe: Testplan

## Testobjekt (System unter Test):

**Webshop: https://grocerymate.masterschool.com/**


---

## Testplan

**Erstelle deinen eigenen Testplan für die neuen Funktionen des Webshops!**

**Der Testplan sollte enthalten:**

1. Analyse des Produkts
2. Entwurf der Teststrategie
3. Definition der Testziele
4. Festlegung der Testkriterien (z. B. Abnahmekriterien, Abbruchkriterien, Fortsetzungskriterien)
5. Ressourcenplanung
6. Planung der Testumgebung
7. Zeitplan und Aufwandsschätzung
8. Festlegung der Testliefergegenstände (Test-Deliverables)

Nutze deine **Anforderungen** aus den vorherigen Aufgaben als Grundlage für den Testplan.

---

## Bewertungskriterien

### Testplan

Der Testplan sollte folgende Informationen enthalten:

1. Zielsetzung (Testziele)
2. Nutzerbasis (Zielgruppen)
3. Produktfunktionen
4. Testumfang (Scope)
5. Testarten (z. B. funktionale Tests, nicht-funktionale Tests, Regressionstests, Abnahmetests)


_____________________________________________________________________________________________________________________

# Testplan für MarketMate - Webshop

## 1. Produktanalyse

**Zielsetzung:**
Das Hauptziel des Webshops ist die Erweiterung durch neue Funktionen sowie die Gewährleistung der reibungslosen Funktionalität von einem Bewertungssystem der Produkte, einer Altersverifikation alkoholischer Produkte und einem Gratisversand ab einem Bestellwert von 20 Euro. 

**Zielgruppe:**
Der Webshop richtet sich an Neukunden und bestehende Kunden, die online Lebensmittel und Artikel für den täglichen Gebrauch einkaufen. 


**Hardware- und Software-Spezifikationen:**

- **Hardwareanforderungen:**
    - Geräte: PCs, Laptops, Smartphones, Tablets
    - Mindestanforderungen: 4 GB RAM, 2 GHz Prozessor
      
- **Softwareanforderungen:**
    - Betriebssysteme: Windows, macOS, Android, iOS
    - Browser: Chrome, Firefox, Safari, Edge
    - Abhängigkeiten: Backend-Dienste, Drittanbieter-Werbedienste, Zahlungsschnittstellen
    

**Funktionalitäten:**

- Registrierung und Login
- Produktsuche
- Produkt Kategorien
- Filter nach Preis
- Favoriten
- Warenkorb
- Kontakt
- Home / Startseite
- Bewertungen abgeben mit Sternen und Text
- Altersverifikation für Alkohol (ab 18 Jahre)
- Gratisversandkosten und Versandkosten
  

## 2. Teststrategie entwerfen

**Testumfang:**

- **Im Umfang enthalten:**
    - Registrierung & Login
    - Produktsuche / Filter / Kategorien
    - Altersverifikation für alkoholische Produkte 
    - gratis Versandkosten ab einem Bestellwert von 20 Euro
    - 5-Sterne-Bewertungssystem und Bewertung mit Text(max. 300 Wörter)
  
- **Außerhalb des Umfangs:**
    - Zahlung
    - Lieferung
    

**Testarten:**

- Funktionstests
- Regressionstests
- Performanztests
- Sicherheitstests
- Usability-Tests

**Risiken und Probleme:**

- **Entwicklungsverzögerungen**
    - Maßnahme: Pufferzeit einplanen
- **Fehlende Testdaten**
    - Maßnahme: Erzeugung von Mock-Daten
- **Ressourcenengpässe**
    - Maßnahme: Ersatzressourcen identifizieren
    

**Testlogistik:**

- Testmanager: Jane Smith
- QA Engineer (Funktion & Regression): John Doe
- QA Engineer (Performanz & Sicherheit): Alice Johnson
- QA Engineer (Usability): Robert Brown
- Endnutzer für Abnahmetests (UAT): Maria Garcia

## 3. Testziele definieren

**Ziele:**

- **Funktionalität:** Neue und bestehende Features funktionieren wie spezifiziert
- **GUI:** Oberfläche ist benutzerfreundlich und konsistent
- **Performanz:** System funktioniert unter erwarteter Last
- **Sicherheit:** Mögliche Schwachstellen erkennen und beheben
- **Usability:** Plattform ist nutzerfreundlich und barrierefrei

**Erwartete Ergebnisse:**

- Alle Features erfüllen die Spezifikationen
- Benutzeroberfläche ist fehlerfrei und reagiert schnell
- Leistung bleibt innerhalb der Zielwerte
- Sicherheitsrisiken sind beseitigt
- Nutzer finden sich problemlos zurecht
- Verifikation für alkoholische Produkte ist fehlerfrei
- Usability ist barrierefrei und nutzerfreundlich
- Bewertungssystem funktioniert fehlerfrei
- Versandkosten kostenlos ab einem Bestellwert von 20 Euro 
- Versandkosten enthalten 5 Euro ab einem Bestellwert unter 20 Euro 
  

## 4. Testkriterien definieren

**Aussetzungskriterien:**

- Kritische Fehler, die das Testen blockieren
- Ausfall der Testumgebung oder Ressourcenmangel
  

**Abnahmekriterien (Exit Criteria):**

- Alle geplanten Testfälle wurden durchgeführt
- Ausführungsquote: min. 95 % der Testfälle ausgeführt
- Bestehensquote: min. 90 % der ausgeführten Testfälle bestanden
- Kritische und hochpriorisierte Fehler wurden behoben und geschlossen
- Keine offenen Fehler der Schwere 1 oder 2
- Performanzkennzahlen erfüllt
- Sicherheitsprobleme gelöst
- UAT abgeschlossen und freigegeben
  

## 5. Ressourcenplanung

- **Personal:** QA-Team, Entwicklungsteam, Endnutzer für UAT
- **Hardware:** PCs, Laptops, Tablets, Smartphones
- **Software:** Browser (Chrome, Firefox, Safari, Edge), Betriebssysteme (Windows, macOS, Android, iOS)
- **Infrastruktur:** Testumgebungen, Automatisierungstools, Performanztools


## 6. Testumgebung planen

- Realgeräte mit echten Betriebssystemen und Browsern
- Umgebungen:
  - Entwicklung (DEV)
  - Test (TEST)
  - Abnahme (ACC)
  - Produktion (PROD)


## 7. Zeitplan und Aufwandsschätzung

| Aktivität | Start | Ende | Umgebung | Verantwortlich | Aufwand |
| --- | --- | --- | --- | --- | --- |
| Testplanung | 13.05.2026 | 17.05.2026 | Alle | Testmanager | 20 Std. |
| Testfalldesign | 18.05.2026 | 27.05.2026 | Alle | QA-Team | 40 Std. |
| Unittest | 28.05.2026 | 08.06.2026 | DEV | Entwicklerteam | 60 Std. |
| Integrationstest | 09.06.2026 | 13.06.2026 | TEST | QA-Team | 30 Std. |
| Systemtest | 14.06.2026 | 23.06.2026 | TEST | QA-Team | 80 Std. |
| Regressions-Test | 24.06.2026 | 28.06.2026 | TEST | QA-Team | 40 Std. |
| Performanztest | 29.06.2026 | 01.07.2026 | TEST | QA-Team | 20 Std. |
| Sicherheitstest | 02.07.2024 | 04.07.2024 | TEST | QA-Team | 20 Std. |
| Abnahmetest (UAT) | 05.07.2024 | 13.07.2024 | ACC | Endnutzer | 50 Std. |
| Produktionsfreigabe | 14.07.2024 | 14.07.2024 | PROD | DevOps-Team | 10 Std. |


## 8. Testartefakte (Test-Deliverables)

- Testplandokument
- Testfälle und Testscripte
- Testdaten
- Testberichte
- Fehlerberichte
- Abnahmeprotokoll (UAT-Signoff)


