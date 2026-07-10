import time
from selenium.webdriver.common.by import By

from conftest import logged_in_driver
from main.HomePage import HomePage
from main.shopPage import shopPage


def test_delivery_costs_threshold(logged_in_driver):
    driver = logged_in_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    # age verification
    shoppe = shopPage(driver)

    age = "22-05-1988"
    shoppe.enter_age(age)
    shoppe.click_confirm_Age()
    time.sleep(10)

    # add gala apples to cart
    shoppe.click_gala_apples_to_cart()

    # click on shopping cart
    shoppe.click_shopping_cart_icon()

    #assert driver.current_url == "https://grocerymate.masterschool.com/checkout"

    shipment_not_free = driver.find_element(By.XPATH, "//h5[@class='fw-bold mb-0' and text()='5']")
    assert shipment_not_free.is_displayed()
    # empty shopping cart -.-

    # test delivery costs visible for amount >= und < 20 euro:
    # wenn product total >= 20 -> assert shipment == 0.00
    # wenn product total < 20 -> assert shipment == 5.00

    # check update of delivery costs on shoppingcart site after changing order
    # does info appear of difference value to reach free delivery

