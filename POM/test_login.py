from conftest import logged_in_driver


def test_login_valid(logged_in_driver):
    # arrange login
    driver = logged_in_driver

    assert driver.current_url == "https://grocerymate.masterschool.com/auth"

