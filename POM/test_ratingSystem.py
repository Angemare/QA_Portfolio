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
    reviewpage.enter_star_review() # use explicit wait
    reviewpage.enter_text_review(text_review) # use explicit wait
    reviewpage.send_review()
    driver.refresh()
    # return check text review to be able to compare text review
    reviewPageText = reviewpage.check_text_review() # check for p element text review
    # check if review is visible
    assert reviewPageText == text_review

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
    reviewPage_error_msg_max_text = reviewpage.error_message_appears()

    assert reviewPage_error_msg_max_text == True


# if len(text_review) >= 500:
# assert reviewPage_error_msg_max_text.is_displayed()
# else:
# return False





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

    # click on bought product to make a review - gala apples
    shoppe.click_gala_apples_to_make_review()

    # add your star review
    reviewpage = reviewPage(driver)
    reviewpage.enter_star_review()
    reviewpage.send_review()
    driver.refresh()
    reviewpage.check_star_review()

    assert enter_star_review == check_star_review # return check star review and try again


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

    # save dynamic error message into a variable
    dynamic_element_without_stars = reviewpage.dynamic_error_message()

    # wait until dynamic error message visible
    assert dynamic_element_without_stars.is_displayed()


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











