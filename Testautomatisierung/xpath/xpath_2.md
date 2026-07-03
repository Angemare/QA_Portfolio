**Gehe zu https://grocerymate.masterschool.com**

**1. Profile Icon**
- //div[@class='social-icon-cont']/div[1]


**Öffne nun https://grocerymate.masterschool.com/auth.**

**2.1 Eingabefeld 'Sign In':**
- //button[@class='submit-btn' and text()='Sign In']

**2.2 Eingabefeld 'Create a new account':**
- //a[@href='#!' and text()='Create a new account']
- //a[text()='Create a new account']

**2.3 Eingabefeld 'Go to home':**
- //a[@href='#!' and text()='Go to Home']
- //a[text()='Go to Home']

**3.1 Eingabefeld "Full Name":**
- //form[@class='form']/input[@type='text']

**3.2 Eingabefeld "Email address":**
- //form[@class='form']//input[@type='email']

**3.3 Eingabefeld "Password":**
- //form[@class='form']//input[@type='password']

**3.4 Button Sign up**
- //button[text()='Sign Up']


**Gehe zu https://grocerymate.masterschool.com/store, dann wirst du die folgende Benutzeroberfläche sehen:**

**4.1 Confirm Schaltfläche:**
- //div[@class='modal-content']//button[text()='Confirm']

**4.2 Mengeneingabefeld für Orangen**
- //p[text()='Oranges']/ancestor::div[@class='card']//input

**4.3 Add to cart Schaltfläche für Oranges:**
- //img[contains(@alt,'Oranges')]/ancestor::div[@class='card']//button[text()='Add to Cart']
- //p[text()='Oranges']/ancestor::div[@class='card']//button[text()='Add to Cart']

**4.4 Add to wish list Schaltfläche für Oranges:**
- //p[text()='Oranges']/ancestor::div[@class='card']//button[contains(@class,'btn-outline-dark')]
