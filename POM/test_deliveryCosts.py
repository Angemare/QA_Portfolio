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

    shopcartpage.get_empty_shoppingcart()

    # order amound under 20
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    shoppe.click_gala_apples_to_cart()
    shoppe.click_shopping_cart_icon()

    shopcartpage = shoppingCartPage(driver)
    no_shipment_free = shopcartpage.get_delivery_costs()
    assert no_shipment_free.is_displayed()

    shopcartpage.get_empty_shoppingcart()


def test_shipment_costs_update_after_refreshing_page(logged_in_driver):
    driver = logged_in_driver



    # check update of delivery costs on shoppingcart site after changing order
    # does info appear of difference value to reach free delivery

