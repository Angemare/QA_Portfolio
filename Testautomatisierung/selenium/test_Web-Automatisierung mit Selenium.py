from selenium import webdriver
from selenium.webdriver.common.by import By


def driver():
    driver = webdriver.Edge()

    yield driver

    driver.quit



# Login - automation
def test_login_saucedemo(driver, username):
    # navigate to Saucedemo Website with get method
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(3000)
    # login-prozess
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click("Login")








