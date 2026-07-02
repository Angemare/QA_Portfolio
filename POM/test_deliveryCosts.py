from selenium.webdriver.common.by import By
from main.HomePage import HomePage
from main.LoginPage import LoginPage
from main.shopPage import shopPage


def test_delivery_costs_threshold(driver):
    # arrange login
    login_page = LoginPage(driver)
    login_page.enter_username("a.stragies@gmx.de")
    login_page.enter_password("lalalalala")

    # execute login
    login_page.click_signin_btn()

    assert driver.current_url == "https://grocerymate.masterschool.com/auth"

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    # age verification
    shoppe = shopPage(driver)
    shoppe.enter_age("22-05-1988")
    shoppe.click_confirm_Age()
    shoppe.click_oranges_to_cart()

    assert driver.current_url == "https://grocerymate.masterschool.com/store"

    # click on shopping cart
    shoppingcart_link = driver.find_element(By.XPATH, "//div[@class='headerIcon'][3]")
    shoppingcart_link.click()

    # test delivery costs visible for amount >= 20 euro