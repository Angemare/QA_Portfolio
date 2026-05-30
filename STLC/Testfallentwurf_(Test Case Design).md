# Testfallentwurf

### **Webshop: https://grocerymate.masterschool.com/**

---


### Testfallentwurf

- Die Testfälle sollen die **drei neuen Funktionen** prüfen.
- Pro Funktion müssen mindestens **3 Testfälle** entworfen werden.
- Falls eine **Testentwurfs-Technik** anwendbar ist, muss sie angegeben werden.
- Außerdem muss ergänzt werden, **welche Testfälle automatisiert** würden – und **warum**.


____________________________________________________________________________________________________

### **1. Bewertungssystem für Produkte**

Testfälle: 

1. Grenzwertanalyse
   - Testfall: Überprüfung der maximalen Texteingabe von 500 Wörter.
       - Eingabe: Text mit 500 Wörtern
       - Erwartetes Ergebnis: Text wird erfolgreich gespeichert und ist auf der Bewertungsseite              sichtbar
    
2. Grenzwertanalyse
   - Testfall: Überprüfung der Texteingabe mit mehr als 500 Wörter.
       - Eingabe: Text mit 501 Wörtern
       - Erwartetes Ergebnis: Fehlermeldung: "Text darf maximal 500 Wörter enthalten"

3. Äquivalenzklassenbildung:
   - Testfall: Überprüfung der Texteingabe mit weniger als 500 Zeichen
     - Eingabe: Text mit 250 Wörter
     - Erwartetes Ergebnis: Text wird gespeichert und ist auf der Bewertungsseite sichtbar

4. Fehlermessen:
  - Testfall: Überprüfung des Bewertungssystems ohne Text
    - Eingabe: Textfeld bleibt leer, Sterne Bewertung abgeben
    - Erwartetes Ergebnis: Sterne Bewertung wird ohne Texteingabe gespeichert und angezeigt

5. Fehlermessen:
   - Testfall: Überprüfung des Bewertungssystems ohne die 5-Sterne-Bewertung
     - Eingabe: keine 5-Sterne-Bewertung abgeben, nur Textbewertung
     - Erwartetes Ergebnis: Fehlermeldung: "Bitte gebe eine 5-Sterne-Bewertung ab"
    
6. Fehlermessen:
   - Testfall: Überprüfung der automatischen Angabe des Datums bei der Abgabe einer Bewertung
     - Eingabe: Bewertung abgeben
     - Erwartetes Ergebnis: das Datum am Tag der Bewertungsabgabe wird angezeigt

7. Anwendungsfalltest:
   - Testfall: Überprüfung der durchschnittlichen Sterne Bewertungen und Anzahl der Bewertungen bei Abgabe/Entfernen
     - Eingabe: Bewertung abgeben/entfernen
     - Erwartetes Ergebnis: Die durchschnittliche Bewertungszahl passt sich, je nach Abgabe/Entfernen, korrekt an.

____________________________________________________________________________________________________

### **2. Altersverifikation für alkoholische Produkte**

Testfälle: 

1. Fehlermessen:
   - Testfall: Überprüfen, dass alle Formate (DD-MM-YYYY, DD.MM.YYYY, DD/MM/YYYY oder DDMMYYYY) bei der Eingabe des Datums funktionieren
     - Eingabe: Datum mit folgenden Formaten: DD-MM-YYYY, DD.MM.YYYY, DD/MM/YYYY oder DDMMYYYY
     - Erwartetes Ergebnis: alle Formate funktionieren | Zugriff zum Webshop

2. Grenzwertanalyse:
   - Testfall: Der Endnutzer ist heute 18 Jahre alt geworden
     - Eingabe: Datum von heute vor 18 Jahren eingeben
     - Erwartetes Ergebnis: Der Endnutzer hat Zugriff auf alkoholische Produkte

3. Grenzwertanalyse:
   - Testfall: Der Endnutzer ist jünger als 18 Jahre alt
     - Eingabe: Alterseingabe jünger als 18 Jahre alt eingeben
     - Erwartetes Ergebnis: Fehlermeldung: "Kein Zugriff auf alkoholische Produkte"

4. Anwendungsfalltest:
  - Testfall: Überprüfung des Aufrufens der URL mit alkholischen Produkten im Browser
    - Eingabe: Öffnen einer URL mit alkholischen Produkten im Browser
    - Erwartetes Ergebnis: leeres Bild - keine Vorschau von Alkohol zu sehen

5. Anwendungsfalltest:
  - Testfall: Neue Eingabe des Alters bei falscher Eingabe
    - Eingabe: falsches Datum eingeben, Schließen und neu Öffnen des Webshops
    - Erwartetes Ergebnis: Pop-Up Fenster mit Altersverifikation öffnet sich erneut

____________________________________________________________________________________________________

### **3. Änderungen bei den Versandkosten**

Testfälle:

1. Grenzwertanalyse:
   - Testfall: Überprüfung der Versandkosten bei einem Bestellwert unter 20 Euro.
     - Eingabe: Bestellwert unter 20 Euro in den Warenkorb legen
     - Erwartetes Ergebnis: 5 Euro Versandkosten

2. Grenzwertanalyse:
   - Testfall: Überprüfung der Versandkosten bei einem Bestellwert von genau 20 Euro.
     -  Eingabe: Bestellwert von 20 Euro in den Warenkorb legen
     -  Erwartetes Ergebnis: Gratisversand

3. Grenzwertanalyse:
   - Testfall: Überprüfung der Versandkosten bei einem Bestellwert über 20 Euro.
     - Eingabe: Bestellwert über 20 Euro in den Warenkorb legen
     - Erwartetes Ergebnis: Gratisversand

4. Anwendungsfalltest:
   - Tesfall: Überprüfung, ob sich bei Änderung des Bestellwertes (über 20 Euro) die Versandkosten im Warenkorb anpassen. 
     - Eingabe: Entfernen von Artikel aus dem Warenkorb -> Bestellwert unter 20 Euro
     - Erwartetes Ergebnis: Versandkosten 5 Euro

5. Anwendungsfalltest:
   - Testfall: Überprüfung der Angabe des Differenzwertes bis zum Gratisversand.
     - Eingabe: Bestellwert 18 Euro
     - Erwartetes Ergebnis: Es fehlen noch 2 Euro bis zum Gratisversand


____________________________________________________________________________________________________




