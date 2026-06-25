**1. Profile Icon**
- //div[@class='headerIcon']

**2.1 Eingabefeld 'Sign In':**
- //button[@class='submit-btn' and text()='Sign In']
- //button[text()='Sign In']

**2.2 Eingabefeld 'Create a new account':**
- //a[@href='#!' and text()='Create a new account']
- //a[text()='Create a new account']

**2.3 Eingabefeld 'Go to home':**
- //a[@href='#!' and text()='Go to home']
- //a[text()='Go to home']

**3.1 Eingabefeld "Full Name":**
- //form[@class='form']//input[text()='Full Name']
- //form[@class='form']//input[@type='text']

**3.2 Eingabefeld "Email address":**
- //form[@class='form']//input[@type='email']

**3.3 Eingabefeld "Password":**
- //form[@class='form']//input[@type='password']

**3.4 Button Sign up**
- //button[text()='Sign Up']

**4.1 Confirm Schaltfläche:**
- //div[@class='modal-content']//button[text()='Confirm']
- //p[text()='Oranges']//button[text()='Add to Cart']

**4.2 Mengeneingabefeld für Orangen**
- //p[text()='Oranges']//input[@type='number' and @value='1']

**4.3 Add to cart Schaltfläche für Oranges:**
- img[contains(@alt,'Oranges')]//button[text()='Add to Cart']

**4.4 Add to wish list Schaltfläche für Oranges:**
- //p[text()='Oranges']//button[text()='🤍'] #black heart actually 
- //p[text()='Oranges']//button[@class='btn btn-outline-dark']

