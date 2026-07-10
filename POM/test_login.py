from conftest import logged_in_driver
from main.LoginPage import LoginPage


def test_login_valid(logged_in_driver):
    # arrange login
    driver = logged_in_driver

    assert driver.current_url == "https://grocerymate.masterschool.com/auth"

