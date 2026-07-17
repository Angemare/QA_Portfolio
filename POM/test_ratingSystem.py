from main.reviewPage import reviewPage
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
    shoppe.click_confirm_Age() # use explicit wait
    # click on bought product to make a review - gala apples
    shoppe.click_gala_apples_to_make_review()

    # add your star review
    reviewpage = reviewPage(driver)
    text_review = "TEST REVIEW"
    reviewpage.enter_star_review()
    reviewpage.enter_text_review(text_review)
    reviewpage.send_review()
    driver.refresh()
    # return check text review to be able to compare text review
    reviewPageText = reviewpage.check_text_review() # p element
    assert reviewPageText == text_review
    driver.refresh()
    # using xfail or skip due to AssertionError

def test_text_limited_characters(logged_in_driver):
    driver = logged_in_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    # age verification
    shoppe = shopPage(driver)
    age = "22-05-1988"
    shoppe.enter_age(age)
    shoppe.click_confirm_Age()
    # click on bought product to make a review - gala apples
    shoppe.click_gala_apples_to_make_review()

    # add your star review
    reviewpage = reviewPage(driver)
    text_review = "TEST REVIEW" * 500
    reviewpage.enter_star_review()
    reviewpage.enter_text_review(text_review)
    reviewPage_error_msg_max_text = reviewpage.limited_char_error_message()
    assert reviewPage_error_msg_max_text == True

def test_review_without_text_possible(logged_in_driver):
    driver = logged_in_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    # age verification
    shoppe = shopPage(driver)
    age = "22-05-1988"
    shoppe.enter_age(age)
    shoppe.click_confirm_Age()
    # click on bought product to make a review - gala apples
    shoppe.click_gala_apples_to_make_review()

    # add your star review
    reviewpage = reviewPage(driver)
    reviewpage.enter_star_review()
    reviewpage.send_review()
    driver.refresh()
    reviewPage_star_review = reviewpage.check_star_review()
    assert reviewPage_star_review == True


def test_review_without_stars_only_text(logged_in_driver):
    driver = logged_in_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    # age verification
    shoppe = shopPage(driver)
    age = "22-05-1988"
    shoppe.enter_age(age)
    shoppe.click_confirm_Age()
    # click on bought product to make a review - gala apples
    shoppe.click_gala_apples_to_make_review()

    # add your star review
    reviewpage = reviewPage(driver)
    text_review = "TEST REVIEW"
    reviewpage.enter_text_review(text_review)
    reviewpage.send_review()
    popup_error_msg_no_stars_review = reviewpage.review_error_message_popup()
    assert popup_error_msg_no_stars_review.is_displayed()
    driver.refresh()


def test_review_average(review_driver):
    driver = review_driver

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()

    # age verification
    shoppe = shopPage(driver)
    age = "22-05-1988"
    shoppe.enter_age(age)
    shoppe.click_confirm_Age()
    # click on bought product to make a review - gala apples
    shoppe.click_gala_apples_to_make_review()

    # add your star review
    reviewpage = reviewPage(driver)
    reviewpage.enter_star_review()
    reviewpage.send_review()
    driver.refresh()
    average_review = reviewpage.average_review_gala_apples()
    assert average_review.is_displayed()











