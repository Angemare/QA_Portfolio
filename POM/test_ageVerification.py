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
    no_access = shoppe.get_invalid_age_verification_msg()
    assert no_access.is_displayed()

def test_age_veri_format_slash(logged_in_driver):
    driver = logged_in_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    shoppe = shopPage(driver)
    shoppe.enter_age_format_slash()
    no_access = shoppe.get_invalid_age_verification_msg()
    assert no_access.is_displayed()

def test_age_veri_format_only_numbers(logged_in_driver):
    driver = logged_in_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    shoppe = shopPage(driver)
    shoppe.enter_age_format_only_num()
    no_access = shoppe.get_invalid_age_verification_msg()
    assert no_access.is_displayed()


def test_younger_than_18_age_verification(logged_in_driver):
    driver = logged_in_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    # age verification
    shoppe = shopPage(driver)
    shoppe.enter_underage_date()
    no_access = shoppe.get_invalid_age_verification_msg()
    assert no_access.is_displayed()





#@pytest.mark.parametrize("date_format, expected", [
    #("22-05-1988", "access to alcohol")
#])
#def test_age_verification_access(date_format, expected):
    #assert test_age_verification_format(date_format) == expected


#@pytest.mark.parametrize("date_format, expected", [
    #("22/05/1988", AttributeError),
    #("22.05.1988", AttributeError),
    #("22051988", AttributeError)
#])
#def test_age_verification_format_no_access(date_format, expected):
    #with pytest.raises(AttributeError):
       # test_valid_age_verification_access_to_alcohol(date_format)





    # age veri date format - ok
    # customers 18. birthday is today
    # customer is younger than 18 - ok
    # new age verification after wrong input
    # open URL with alcoholic products - expected: no alcoholic products visible
