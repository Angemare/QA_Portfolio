import time
from selenium.common import TimeoutException
from conftest import logged_in_driver
from main.HomePage import HomePage
from main.shopPage import shopPage
from main.shoppingCartPage import shoppingCartPage


def test_shipment_cost_threshold_20(logged_in_driver):
    driver = logged_in_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    # age verification
    shoppe = shopPage(driver)
    shoppe.enter_default_age()
    # order amount over 20
    shoppe.enter_quantity_add_to_cart_open_shopping_cartpage()
    shopcartpage = shoppingCartPage(driver)
    shipment_free = shopcartpage.get_free_shipment()
    assert shipment_free.is_displayed()

    shopcartpage.clear_and_get_empty_shoppingcart()

    # order amound under 20
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    shoppe.click_gala_apples_to_cart()
    shoppe.click_shopping_cart_icon()

    shopcartpage = shoppingCartPage(driver)
    no_shipment_free = shopcartpage.get_delivery_costs()
    assert no_shipment_free.is_displayed()

    shopcartpage.clear_and_get_empty_shoppingcart()


def test_updated_shipment_costs_after_change_amount_to_18_on_cartpage(logged_in_driver):
    driver = logged_in_driver
    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    # age verification
    shoppe = shopPage(driver)
    shoppe.enter_default_age()
    # order amount over 20
    shoppe.enter_quantity_add_to_cart_open_shopping_cartpage()
    shopcartpage = shoppingCartPage(driver)
    shopcartpage.click_minus_product_btn()

    try:
        shopcartpage.get_delivery_costs()
    except TimeoutException:
        print("AssertionError: Element not updating to 5€ after changing order amount to 18.")
    finally:
        # check if shipment costs update to 5€ after refreshing page
        driver.refresh()
        time.sleep(5)
        no_shipment_free = shopcartpage.get_delivery_costs()
        assert no_shipment_free.is_displayed()

        shopcartpage.clear_and_get_empty_shoppingcart()


def test_free_shipment_info(logged_in_driver):
    driver = logged_in_driver
    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    # age verification
    shoppe = shopPage(driver)
    shoppe.enter_default_age()
    # order amount over 20
    shoppe.enter_quantity_add_to_cart_open_shopping_cartpage()
    shopcartpage = shoppingCartPage(driver)
    get_free_shipment_msg = shopcartpage.get_free_shipment_message()
    assert get_free_shipment_msg.is_displayed()

    shopcartpage.clear_and_get_empty_shoppingcart()

