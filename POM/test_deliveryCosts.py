
from main.HomePage import HomePage
from main.shopPage import shopPage
from main.shoppingCartPage import shoppingCartPage

def test_shipment_cost_20(shoppingcart_driver):
    driver = shoppingcart_driver
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    # open shoppage + age verification + click confirm with @classemethod in shopPage
    shoppe = shopPage.open_shop_with_age(driver)
    # order amount 20
    shoppe.enter_quantity_add_to_cart_open_shopping_cartpage()
    shopcartpage = shoppingCartPage(driver)
    shipment_free = shopcartpage.get_free_shipment()
    assert shipment_free.is_displayed()

def test_under_20_delivery_cost(shoppingcart_driver):
    driver = shoppingcart_driver
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    # open shoppage + age verification + click confirm with @classemethod in shopPage
    shoppe = shopPage.open_shop_with_age(driver)
    shoppe.click_gala_apples_to_cart()
    shoppe.click_shopping_cart_icon()
    shopcartpage = shoppingCartPage(driver)
    no_shipment_free = shopcartpage.get_delivery_costs()
    assert no_shipment_free.is_displayed()


def test_updated_shipment_costs_after_change_amount_to_18_on_cartpage(shoppingcart_driver):
    driver = shoppingcart_driver
    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    # open shoppage + age verification + click confirm with @classemethod in shopPage
    shoppe = shopPage.open_shop_with_age(driver)
    # order amount over 20
    shoppe.enter_quantity_add_to_cart_open_shopping_cartpage()
    shopcartpage = shoppingCartPage(driver)
    shopcartpage.click_minus_product_btn()
    deliverycosts_5 = shopcartpage.does_element_5_exist()
    assert deliverycosts_5 == "5€"

def test_free_shipment_info(shoppingcart_driver):
    driver = shoppingcart_driver
    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    # open shoppage + age verification + click confirm with @classemethod in shopPage
    shoppe = shopPage.open_shop_with_age(driver)
    # order amount over 20
    shoppe.enter_quantity_add_to_cart_open_shopping_cartpage()
    shopcartpage = shoppingCartPage(driver)
    get_free_shipment_msg = shopcartpage.get_free_shipment_message()
    assert get_free_shipment_msg.is_displayed()




