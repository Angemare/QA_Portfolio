import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.HomePage import HomePage
from main.shopPage import shopPage





def test_age_verification_format(logged_in_driver):
    driver = logged_in_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    # age verification
    shoppe = shopPage(driver)
    age = "22-05-1988"
    shoppe.enter_age(age)
    shoppe.click_confirm_Age()
    time.sleep(5)

    assert driver.current_url == "https://grocerymate.masterschool.com/store"

#@pytest.mark.parametrize("date_format, expected", [
    #("22-05-1988", "access to alcohol")
#])
#def test_age_verification_access(date_format, expected):
    #assert test_age_verification_format(date_format) == expected


@pytest.mark.parametrize("date_format, expected", [
    ("22/05/1988", AttributeError),
    ("22.05.1988", AttributeError),
    ("22051988", AttributeError)
])
def test_age_verification_format_no_access(date_format, expected):
    with pytest.raises(AttributeError):
        test_age_verification_format(date_format)


    #category_alcohol = driver.find_element(By.XPATH, "//a[@href='#' and text()='Alocohol']")
    #category_alcohol.click()

    #no_access_to_alcohol = driver.find_element(By.XPATH, "//div[@class='card-body']")
    #assert no_access_to_alcohol.is_displayed()


    # customers 18. birthday is today
    # customer is younger than 18
    # new age verification after wrong input
    # open URL with alcoholic products - expected: no alcoholic products visible
