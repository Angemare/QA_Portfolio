from selenium import webdriver
from selenium.webdriver.common.by import By # locating elements on webpage with by
from _pytest.fixtures import fixture
import pytest
from selenium.webdriver.support.select import Select

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

@pytest.fixture
def driver():
    # instantiate a WebDriver object
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    # function will continue due to yield
    yield driver
    # end session
    driver.quit()

# create test function
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

    # 6./ 7./ fill in username & email & click on signup
    driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[2]").send_keys("Testuser")
    driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]").send_keys("testuse@tst.com")
    driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/button").click()

    # 8./ check if ENTER ACCOUNT INFORMATION is visible when registering
    enter_account_info = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/h2/b[text()='Enter Account Information']")
    assert enter_account_info.is_displayed()

    # 9./ fill in details: Title, Name, E-Mail, Password, birthdate
    driver.find_element(By.ID, "id_gender2").click()
    driver.find_element(By.ID, "password").send_keys("pwtest000")
    Select(driver.find_element(By.ID, "days")).select_by_value("1")
    Select(driver.find_element(By.ID, "months")).select_by_value("10")
    Select(driver.find_element(By.ID, "years")).select_by_value("1990")

    # 10./ click check box Sign up for our newsletter!
    driver.find_element(By.ID, "newsletter").click()

    # 11./ click check box for Receive special offers from our partners!
    driver.find_element(By.ID, "optin").click()

    # 12./ fill in address information for registration
    driver.find_element(By.ID, "first_name").send_keys("Testuser")
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "company").send_keys("Test-Company")
    driver.find_element(By.ID, "address1").send_keys("Testerstreet")
    driver.find_element(By.ID, "address2").send_keys("Testerstreet2")
    Select(driver.find_element(By.ID, "country")).select_by_value("New Zealand")
    driver.find_element(By.ID, "state").send_keys("Nelson")
    driver.find_element(By.ID, "city").send_keys("Nelson City")
    driver.find_element(By.ID, "zipcode").send_keys("00000")
    driver.find_element(By.ID, "mobile_number").send_keys("+63 12345678")

    # 13./ click on create account
    driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/form/button").click()

    # 14./ check if account created is visible
    acc_created_visible = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[1]/div/a/img")
    assert acc_created_visible.is_displayed()

    # 15./ click on button continue
    driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/a").click()

    # 16./ check if logged in as username is visible
    logged_in_as = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]")
    assert logged_in_as.is_displayed()

    # 17./ click on button delete account
    driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a").click()

    # 18./ check if account deleted is visible and click on button continue
    account_del_visible = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/h2/b")
    assert account_del_visible.is_displayed()

    driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/a").click()

