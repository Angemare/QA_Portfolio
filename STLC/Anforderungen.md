# Anforderungen


### **Die Applikation:**

https://grocerymate.masterschool.com/

Webshop mit folgenden Grundfunktionen:

- Registrierung und Login
- Produktsuche mit Sortierfunktion (z. B. nach Preis), Kategorisierung von Produkten
- Produkte zu Favoriten hinzufügen
- Produkte in den Warenkorb legen
- Bestellabschluss: Eingabe von Rechnungs- und Versandinformationen, Auswahl der Zahlungsmethode, Preisberechnung (Gesamtsumme)

---

## **Neue Funktionen (Features)**

---

### **1. Bewertungssystem für Produkte**

**Ursprünglich vage formulierte Anforderung:**

  - Nutzer sollen Produkte mit einem 5-Sterne-System bewerten und zusätzlich schriftliches Feedback hinterlassen können.

**Fragen:**

1\. Kann die maximale Anzahl an Wörter überschritten werden? (500 Wörter max.)

2\. Ist es möglich Feedback ohne Text abzugeben und umgekehrt nur Text ohne Stern Bewertung?

3\. Wird das aktuelle Datum bei der Abgabe des Feedbacks automatisch vom System abgegeben? 

4.\ Passt sich die durchschnittlich angegebene Sterne Bewertung und Anzahl der Bewertungen nach Abgabe/Entfernen von Bewertungen korrekt an?


**Detaillierte Anforderungen:**

  - Der Kunde soll nach Erhalt der Ware die Möglichkeit haben, das gekaufte Produkt mit einem 5-Sterne-System zu bewerten und optional einen Text von max. 500 Wörtern abgeben können. Bei Feedback Abgabe muss der Kunde mindestens einen Stern abgeben. Es ist nicht möglich die Stern Bewertung auszulassen sowie 0 Sterne abzugeben. Bei Abgabe der Bewertung wird das aktuelle Datum automatisch vom System angegeben und entspricht folgendes Format DD-MM-YYYY. Die durchschnittliche Bewertung passt sich nach Abgabe/Enternung von Bewertungen an.
---

### **2. Altersverifikation für alkoholische Produkte**

**Ursprünglich vage formulierte Anforderung:**

  -  Alkoholische Produkte erfordern eine Altersverifikation. Beim Aufrufen der Kategorie soll ein Fenster erscheinen, in dem Nutzer ihr Alter angeben müssen (18+), bevor sie Zugriff erhalten.

1\. Funktionieren alle Formate (DD-MM-YYYY, DD.MM.YYYY, DD/MM/YYYY oder DDMMYYYY) bei der Eingabe des Datums? 

2\. Was, wenn man die URL von alkoholischen Artikeln aufruft (nicht direkt über die Seite öffnet) Kann die Person ohne Altersverifikation alkoholische Produkte sehen und einkaufen? 

3\. Wie lange ist die Altersverifikation im System gespeichert?

4\. Haben Kunden >= 18 Jahre oder erst > 18 Jahre Zugriff auf alkoholische Produkte?


**Detaillierte Anforderungen:**

  - Der Kunde soll direkt nach der Registrierung oder dem Login eine Altersverifikation durchführen, hierzu erscheint ein Pop Up Fenster. Die Eingabe des Alters wird in jeder Session gespeichert. Beim Schließen und neu Öffnen des Webshops, wird der Kunde gebeten sein Alter neu einzugeben. Beim Aufrufen einer URL mit alkoholischen Getränken soll es nicht möglich sein die alkoholischen Produkte zu sehen. Kunden unter 18 Jahre können das Menü der alkoholischen Produkte nicht sehen. 
---

### **3. Änderungen bei den Versandkosten**

**Ursprünglich vage formulierte Anforderung:**

  -  Versandkosten entfallen ab einem bestimmten Bestellwert. Darunter fallen Versandkosten an.

1\. Was passiert, wenn ein Produkt im Warenkorb entfernt/hinzugefügt wird und der Betrag nun unter/über 20 ist?

2\. Sind die Versandkosten bei einem Mindestbestellwert von (>=) 20 Euro versandkostenfrei oder > 20 Euro ?

3\. Passen sich die Versandkosten beim Aktualisieren der Seite im Warenkorb erst an? 

4\. Wird der Differenzwert in Euro für einen kostenlosen Versand im Warenkorb angegeben? (Bsp. "Es fehlen noch xy Euro für einen gratis Versand") 


**Detaillierte Anforderung:**

  -  Der Kunde kann im Warenkorb Produkte hinzufügen sowie entfernen und die Versandkosten passen sich automatisch an ohne die Seite zu Aktualisieren. Die Versandkosten sind ab einem Mindestbestellwert von 20 Euro kostenlos. Unter 20 Euro zahlt der Kunde 5 Euro Versandkosten. Der Kunde wird darüber informiert, wieviel Euro fehlen bis zum gratis Versand.



_____________________________________________________________________________________________________________________




