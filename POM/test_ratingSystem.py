import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.shoppingCartPage import shoppingCartPage
from main.HomePage import HomePage
from main.shopPage import shopPage


def test_rating_system_limited_characters(review_driver):
    driver = review_driver
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

    # enter shipment address details
    shopcartpage = shoppingCartPage(driver)

    street = "test street"
    city = "test city"
    postalcode = "00000"

    shopcartpage.enter_street(street)
    shopcartpage.enter_city(city)
    shopcartpage.enter_postalcode(postalcode)

    # enter payment details
    card_number = "0123456789"
    name_on_card = "test name"
    expiration_date = "1234567"
    cvv = "000"

    shopcartpage.enter_card_number(card_number)
    shopcartpage.enter_name_on_card(name_on_card)
    shopcartpage.enter_expiration_date(expiration_date)
    shopcartpage.enter_cvv(cvv)
    shopcartpage.click_buy_now()

    # navigate to shop page
    shop_link = driver.find_element(By.XPATH, "(//a[@href='/store'])[1]")
    shop_link.click()

    # click on bought product - gala apples
    gala_apples_review_click = driver.find_element(By.XPATH, "//p[text()='Gala Apples']")
    gala_apples_review_click.click()

    # add your star review
    star_review_input = driver.find_element(By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[5]")
    star_review_input.click()

    text_review_input = driver.find_element(By.XPATH, "//textarea[@class='new-review-form-control ']")
    text_review_input.send_keys("AAAAA")

    send_review_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class= 'new-review-btn new-review-btn-send']")))
    send_review_button.click()

    # check if review is visible
    text_review = driver.find_element(By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div")
    assert text_review.is_displayed()
    assert text_review == "AAAAA"





    # pytest.mark.parametrize("Eigenschaften", [
    #   (data to test)
    #])

    #check if review with text limited is visible
    #check if test review without stars is displayed
    #check if test average review is displayed
    #check if test review without text is displayed

# def test_limited_characters == 500 characters, > 500 characters, < 500 characters
# def test_review_without_stars
# def test_average_review
# def test_review_without_text









