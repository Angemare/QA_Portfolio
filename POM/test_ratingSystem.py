import time

from selenium.webdriver.common.by import By

from main.reviewPage import reviewPage
from main.shoppingCartPage import shoppingCartPage
from main.HomePage import HomePage
from main.shopPage import shopPage


def test_text_rating_visibility(review_driver):
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
    homepage.click_shop_btn()

    # click on bought product to make a review - gala apples
    shoppe.click_gala_apples_to_make_review()

    # add your star review
    reviewpage = reviewPage(driver)

    text_review = "TEST REVIEW"
    reviewpage.enter_star_review()
    reviewpage.enter_text_review(text_review)
    reviewpage.send_review()
    time.sleep(10)
    reviewpage.check_text_review()

    # check if review is visible
    assert reviewpage.check_text_review == "TEST REVIEW"


def test_text_limited_characters_500(logged_in_driver):
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
    homepage.click_shop_btn()

    # click on bought product to make a review - gala apples
    shoppe.click_gala_apples_to_make_review()

    # add your star review
    reviewpage = reviewPage(driver)

    text_review = "TEST REVIEW" * 500
    reviewpage.enter_star_review()
    reviewpage.enter_text_review(text_review)
    time.sleep(5)
    reviewpage.error_message_appears()
    time.sleep(5)

    assert reviewpage.error_message_appears, "You cannot tell us more about this product."

    if len(text_review) >= 500:
        assert reviewpage.error_message_appears,"You cannot tell us more about this product."


def test_review_without_text_possible(logged_in_driver, enter_star_review=None, check_star_review=None):
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
    homepage.click_shop_btn()

    # click on bought product to make a review - gala apples
    shoppe.click_gala_apples_to_make_review()

    # add your star review
    reviewpage = reviewPage(driver)

    reviewpage.enter_star_review()
    time.sleep(10)
    reviewpage.send_review()
    time.sleep(10)
    reviewpage.check_star_review()
    time.sleep(10)
    
    assert enter_star_review == check_star_review




# def test_review_without_stars
# def test_average_review









