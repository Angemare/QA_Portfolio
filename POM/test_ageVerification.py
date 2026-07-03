from selenium.webdriver.common.by import By
from main.HomePage import HomePage
from main.LoginPage import LoginPage
from main.shopPage import shopPage


def test_age_verification_format(logged_in_driver):
    driver = logged_in_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()


    # age verification
    shoppe = shopPage(driver)
    shoppe.enter_age("22-05-1988")
    shoppe.click_confirm_Age()
    shoppe.click_oranges_to_cart()

    assert driver.current_url == "https://grocerymate.masterschool.com/store"