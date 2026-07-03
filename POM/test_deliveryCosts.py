import time

from selenium.webdriver.common.by import By
from main.HomePage import HomePage
from main.LoginPage import LoginPage
from main.shopPage import shopPage


def test_delivery_costs_threshold(logged_in_driver):
    driver = logged_in_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    # age verification
    shoppe = shopPage(driver)
    shoppe.enter_age("22-05-1988")
    shoppe.click_confirm_Age()
    time.sleep(3)
    shoppe.click_oranges_to_cart()

    assert driver.current_url == "https://grocerymate.masterschool.com/store"

    # click on shopping cart
    shoppingcart_link = driver.find_element(By.XPATH, "//div[@class='headerIcon'][3]")
    shoppingcart_link.click()

    assert driver.current_url == "https://grocerymate.masterschool.com/checkout"

    # test delivery costs visible for amount >= 20 euro
    # wenn product total >= 20 -> assert shipment == 0.00
    # wenn product total < 20 -> assert shipment == 5.00