# Anforderungen

Der erste Teil des Projektes ist es, die Anforderungen richtig zu verstehen. ****

1. **Überleg dir Fragen und beantworte sie mithilfe der Webseite.** 
2. **Schreib eine kurze Zusammenfassung aller Informationen, die du gefunden hast.**


### **Die Applikation:**

https://grocerymate.masterschool.com/

Webshop mit folgenden Grundfunktionen:

- Registrierung und Login
- Produktsuche mit Sortierfunktion (z. B. nach Preis), Kategorisierung von Produkten
- Produkte zu Favoriten hinzufügen
- Produkte in den Warenkorb legen
- Bestellabschluss: Eingabe von Rechnungs- und Versandinformationen, Auswahl der Zahlungsmethode, Preisberechnung (Gesamtsumme)

---
## Bewertungsgrundlage

- Mindestens 3 Fragen pro neuem Feature
- Fragen müssen für das Verständnis des Testings relevant sein

## **Neue Funktionen (Features)**

---

### **1. Bewertungssystem für Produkte**

**Ursprünglich vage formulierte Anforderung:**

Nutzer sollen Produkte mit einem 5-Sterne-System bewerten und zusätzlich schriftliches Feedback hinterlassen können.

**Fragen:**
1\. Kann die maximale Anzahl an Wörter überschritten werden? (300 Wörter max.)
2\. Ist es möglich Feedback ohne Text abzugeben?
3\. Wird das aktuelle Datum bei der Abgabe des Feedbacks angegeben ? 
4\. Wird der Kunde aufgefordert eine Bewertung nach Kauf bzw. Erhalt des Produktes abzugeben?

**Detaillierte Anforderungen:**

Der Kunde soll nach Erhalt der Ware die Möglichkeit haben, das gekaufte Produkt mit einem 5-Sterne-System zu bewerten und optional einen Text von max. 300 Wörtern abgeben können. Bei Abgabe der Bewertung wird das aktuelle Datum angegeben. Der Kunde wird nach Erhalt des Produktes informiert eine Bewertung abgeben zu können.
---

### **2. Altersverifikation für alkoholische Produkte**

**Ursprünglich vage formulierte Anforderung:**

Alkoholische Produkte erfordern eine Altersverifikation. Beim Aufrufen der Kategorie soll ein Fenster erscheinen, in dem Nutzer ihr Alter angeben müssen (18+), bevor sie Zugriff erhalten.

1\. Ist es möglich, das Alter anzupassen? (Profilangaben - Einstellungen z. B.) 
2\. Was passiert, wenn der Kunde ein falsches Datums-Format eingibt? (Anstatt - ein . oder /) (-> Info gewünschtes       Format) (-> Fehlermeldung: Bitte nutze folgendes Format) oder (-> dropdown list Calender - Format) 
3\. Wird die Altersverifikation beim Anklicken alkholischer Produkte ausgeführt? 
4\. Was, wenn man die URL versendet und aufruft (nicht direkt über die Seite öffnet) ? Kann die Person ohne              Altersverifikation Alkohol einkaufen? 

**Detaillierte Anforderungen:**
Der Kunde soll nach Auswahl von alkoholischen Getränken eine ALtersverifikation durchführen. Das gewünschte Format des Datums sollte so hinterlegt sein, dass der Kunde nur Zahlen eingeben muss oder ein Drop Down List Calender nutzt. Das Datum sollte im Profil anzupassen sein. Beim Aufrufen der URL mit alkholischen Getränken, wird erneut nach einer Altersverifikation gefragt

---

### **3. Änderungen bei den Versandkosten**

**Ursprünglich vage formulierte Anforderung:**

Versandkosten entfallen ab einem bestimmten Bestellwert. Darunter fallen Versandkosten an.

1\. Was passiert, wenn ein Produkt entfernt/hinzugefügt wird und der Betrag nun unter/über 20 ist?
2\. Sind die Versandkosten bei einem Mindestbestellwert von 20 Euro versandkostenfrei oder > 20 Euro ? 
3\. Passen sich die Versandkosten beim Aktualisieren der Seite erst an? 

**Detaillierte Anforderung:**

Der Kunde kann im Warenkorb Produkte hinzufügen sowie entfernen und die Versandkosten passen sich automatisch an ohne die Seite zu Aktualisieren. Die Versandkosten sind ab einem Mindestbestellwert von 20 Euro kostenlos. Unter 20 Euro zahlt der Kunde 5 Euro Versandkosten. 



_____________________________________________________________________________________________________________________




