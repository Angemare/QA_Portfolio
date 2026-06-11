from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest.fixtures import fixture
import pytest


@fixture
def driver():
    # instantiate a WebDriver object
    driver = webdriver.Edge()

    yield driver
    # end session
    driver.quit()


@pytest.mark.parametrize("usernames", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"])


#  test function - website - automation
def test_website_login_and_product_name(driver, usernames):
    # navigate to saucedemo Website with get method
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(3000)

    # find and interact with accepted usernames and password
    driver.find_element(By.ID, "user-name").send_keys(usernames)
    driver.implicitly_wait(3000)

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.implicitly_wait(3000)

    login_button = (driver.find_element(By.ID, "login-button"))
    login_button.click()
    driver.implicitly_wait(3000)

    # find product name by checking its class name
    product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text


    #  test login with not successful login usernames
    if usernames == "locked_out_user":
        error_message = driver.find_element(By.CSS_SELECTOR, "error").text
        assert "Sorry, this user has been locked out" in error_message
    else:
        # test login with successful login usernames
        assert "Swag Labs" in driver.title


    # test availability of product_name Sauce Labs Backpack
    assert product_name == "Sauce Labs Backpack"



















