import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from main.HomePage import HomePage
from main.LoginPage import LoginPage
from main.shopPage import shopPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(15)
    driver.get("https://grocerymate.masterschool.com/auth")

    yield driver

    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("a.stragies@gmx.de")
    login_page.enter_password("lalalalala")
    login_page.click_signin_btn()
    return driver

@pytest.fixture
def review_driver(logged_in_driver):
    yield logged_in_driver
    # review löschen mit selenium locator finden
    meatballs_menu = logged_in_driver.find_element(By.XPATH, "//div[@class='menu-icon']")
    meatballs_menu.click()
    delete_review = logged_in_driver.find_element(By.XPATH, "//button[text()='Delete']")
    delete_review.click()
    alert = logged_in_driver.switch_to.alert
    alert.accept()

@pytest.fixture
def navigate_to_shop_veri_age_add_oranges_to_cart_driver(logged_in_driver):
    homepage = HomePage(logged_in_driver)
    homepage.click_shop_btn()
    shoppe = shopPage(logged_in_driver)
    shoppe.enter_age("22-05-1988")
    shoppe.click_confirm_Age()
    time.sleep(3)
    shoppe.click_oranges_to_cart()
    return logged_in_driver