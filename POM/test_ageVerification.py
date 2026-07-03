import time

from conftest import logged_in_driver, navigate_to_shop_veri_age_driver
from main.HomePage import HomePage
from main.shopPage import shopPage


def test_age_verification_format(navigate_to_shop_veri_age_driver):
    driver = navigate_to_shop_veri_age_driver


    # navigate to shop page
    #homepage = HomePage(driver)
    #homepage.click_shop_btn()

    # age verification
    #shoppe = shopPage(driver)
    #shoppe.enter_age("22-05-1988")
    #shoppe.click_confirm_Age()
    #shoppe.click_oranges_to_cart()

