from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest.fixtures import fixture

"""
Schreibe ein Selenium-Skript, das Folgendes durchführt:

1. Browser starten
2. Zur URL navigieren: http://automationexercise.com
3. Überprüfen, dass die Startseite erfolgreich sichtbar ist
4. Auf die Schaltfläche **„Signup / Login“** klicken
5. Überprüfen, dass **„New User Signup!“** sichtbar ist
6. Namen und E-Mail-Adresse eingeben
7. Auf die Schaltfläche **„Signup“** klicken
8. Überprüfen, dass **„ENTER ACCOUNT INFORMATION“** sichtbar ist
9. Details ausfüllen: Titel, Name, E-Mail, Passwort, Geburtsdatum
10. Kontrollkästchen **„Sign up for our newsletter!“** auswählen
11. Kontrollkästchen **„Receive special offers from our partners!“
** auswählen
12. Details ausfüllen: Vorname, Nachname, Firma, Adresse, Adresse2, 
Land, Bundesstaat, Stadt, Postleitzahl, Handynummer
13. Auf die Schaltfläche **„Create Account“** klicken
14. Überprüfen, dass **„ACCOUNT CREATED!“** sichtbar ist
15. Auf die Schaltfläche **„Continue“** klicken
16. Überprüfen, dass **„Logged in as username“** sichtbar ist
17. Auf die Schaltfläche **„Delete Account“** klicken
18. Überprüfen, dass **„ACCOUNT DELETED!“** sichtbar ist und 
auf **„Continue“** klicken"""

@fixture
def driver():
    # instantiate a WebDriver object
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    # function will continue due to yield
    yield driver
    # end session
    driver.quit()

# test funktion erstellen
def test_registration_automation(driver):
    # 1./ 2./ start browser and navigate to website automationexercise.com
    driver.get("https://automationexercise.com/")

    # 3./ check if homepage is visible
    assert "Automation Exercise" in driver.title

    # 4./ click signup and login
    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()

    # 5./ check if New User Signup is visible
    new_sign_up_header = driver.find_element(By.XPATH, "//*[@ID='form']/div/div/div[3]/div/h2[text()='New User Signup!']")
    assert new_sign_up_header.is_displayed()

    #6./ 7./ fill in username & email & click on signup
    driver.find_element(By.CSS_SELECTOR, "login-email").send_keys("Testuser")
    driver.find_element(By.CSS_SELECTOR, "login-password").send_keys("testuser000@testing.com")
    driver.find_element(By.CSS_SELECTOR, "login-button").click()

    # 8./ check if ENTER ACCOUNT INFORMATION is visible when registering
    enter_account_info = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/h2/b[text()='Enter Account Information']")
    assert enter_account_info.is_displayed()
