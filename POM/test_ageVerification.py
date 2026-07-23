from main.HomePage import HomePage
from main.shopPage import shopPage


def test_age_verification_format_hyphen(logged_in_driver):
    driver = logged_in_driver
    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    # age verification
    shoppe = shopPage(driver)
    shoppe.enter_default_age()
    # open alcohol menu
    shoppe.click_alcohol_menu()
    text_category_alocohol = shoppe.get_text_alocohol()
    assert text_category_alocohol == True

def test_age_veri_format_dot(logged_in_driver):
    driver = logged_in_driver
    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    shoppe = shopPage(driver)
    shoppe.enter_age_format_dot()
    no_access = shoppe.click_and_get_invalid_age_verification_msg()
    assert no_access.is_displayed()

def test_age_veri_format_slash(logged_in_driver):
    driver = logged_in_driver
    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    shoppe = shopPage(driver)
    shoppe.enter_age_format_slash()
    no_access = shoppe.click_and_get_invalid_age_verification_msg()
    assert no_access.is_displayed()

def test_age_veri_format_only_numbers(logged_in_driver):
    driver = logged_in_driver
    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    shoppe = shopPage(driver)
    shoppe.enter_age_format_only_num()
    no_access = shoppe.click_and_get_invalid_age_verification_msg()
    assert no_access.is_displayed()

def test_younger_than_18_age_verification(logged_in_driver):
    driver = logged_in_driver
    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    # age verification
    shoppe = shopPage(driver)
    shoppe.enter_underage_date()
    no_access = shoppe.click_and_get_invalid_age_verification_msg()
    assert no_access.is_displayed()
