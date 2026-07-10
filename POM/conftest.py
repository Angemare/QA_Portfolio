
import pytest
from selenium import webdriver
from main.LoginPage import LoginPage
from main.reviewPage import reviewPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(15)
    driver.get("https://grocerymate.masterschool.com/auth")

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    username = "a.stragies@gmx.de"
    password = "lalalalala"
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_signin_btn()
    return driver


@pytest.fixture
def review_driver(logged_in_driver):
    yield logged_in_driver
    # delete review
    reviewpage = reviewPage(logged_in_driver)
    reviewpage.click_meatballs_menu()
    reviewpage.delete_review()
    alert = logged_in_driver.switch_to.alert
    alert.accept()
