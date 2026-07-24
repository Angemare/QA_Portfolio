import pytest

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


@pytest.mark.parametrize("date", [
    ("22.04.1988"),
    ("12/09.1978"),
    ("12021966"),
    ("20-07-2009")
])

def test_date_format_age_verification(date, logged_in_driver):
    driver = logged_in_driver
    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()
    shoppe = shopPage(driver)
    shoppe.enter_age(date)
    shoppe.click_confirm_Age()

    no_access = shoppe.click_and_get_invalid_age_verification_msg()
    assert no_access.text.startswith("Underage Notice")


