from main.LoginPage import LoginPage


def test_login_valid(driver):

# arrange login
    login_page = LoginPage(driver)
    login_page.enter_username("a.stragies@gmx.de")
    login_page.enter_password("lalalalala")

    # execute login
    login_page.click_signin_btn()

    assert driver.current_url == "https://grocerymate.masterschool.com/auth"

    # oder assert logout link is displayed