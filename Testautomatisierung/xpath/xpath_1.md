**1. Finde das Haupt h1 Element:**
- //h1[@id='mainTitle']

**2. Navigations link "About us":**
- //nav//a[@href = '#about'] 

**3. DropDown-Link Graphic Design:**
- //ul[@class='dropdown']//a[@href='#graphicdesign']

**4. Name des Teammitglieds Jane Smith:**
- //h4[text()='Jane Smith']

**5. Beschreibung (im Absatz) der SEO Services:**
- //h3[text()='SEO Services']

**6. alle Service Elemente im Abschnitt "Our Services":**
- //section[@id='services']

**7. E-Mail Eingabefeld im Kontaktformular:**
- //form[@id='contactForm']//input[@type='email']

**8. Auswahl vom gesamten Kontaktformular:**
- //form[@id='contactForm']

**9. Auswahl Footer Absatz Element:**
- //footer//p

**10. Auswahl Name von h4 des 1. Teammitglieds:**
- //div[@class='team']//li[1]

**11. Auswahl Beschreibung des 2. Service Elements:**
- //div[@class='service-item']/p[2]

**12. Überschrift der Sektion "Contact Us"(h2 Element):**
- //h2[text()='Contact Us']

**13. alle Links innerhalb des Dropdowns unter "Services":**
- //a[@href='#services']//ul[@class='dropdown']/li

**14. 1. li im Abschnitt "Our Team":**
- //h3[text()='Our Team']//li[1]

**15. Finde die Schaltfläche "Send Message" im Kontaktforumular:**
- //form[@id='contactform']//input[@type='submit' and @value'Send Message']

