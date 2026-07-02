from selenium.webdriver.common.by import By
from main.HomePage import HomePage
from main.LoginPage import LoginPage
from main.shopPage import shopPage


def test_rating_system_limited_characters(driver):
    # arrange login
    login_page = LoginPage(driver)
    login_page.enter_username("a.stragies@gmx.de")
    login_page.enter_password("lalalalala")

    # execute login
    login_page.click_signin_btn()

    assert driver.current_url == 'https://grocerymate.masterschool.com/auth'

    # navigate to shop page
    homepage = HomePage(driver)
    homepage.click_shop_btn()


    # age verification
    shoppe = shopPage(driver)
    shoppe.enter_age("22-05-1988")
    shoppe.click_confirm_Age()
    shoppe.click_oranges_to_cart()


    # click on shopping cart
    shoppingcart_link = driver.find_element(By.XPATH, "//div[@class='headerIcon'][3]")
    shoppingcart_link.click()

    # shipment address
    street_input = driver.find_element(By.XPATH, "//form[@class='payment-form']//input[@name='street']")
    street_input.send_keys("test street")

    city_input = driver.find_element(By.XPATH, "//form[@class='payment-form']//input[@name='city']")
    city_input.send_keys("test city")

    postalcode_input = driver.find_element(By.XPATH, "//form[@class='payment-form']//input[@name='postalCode']")
    postalcode_input.send_keys("00000")

    # payment
    card_number_input = driver.find_element(By.XPATH, "//form[@class='payment-form']//input[@name='cardNumber']")
    card_number_input.send_keys("0123456789")

    name_on_card_input = driver.find_element(By.XPATH, "//form[@class='payment-form']//input[@name='nameOnCard']")
    name_on_card_input.send_keys("test name")

    expiration_input = driver.find_element(By.XPATH, "//form[@class='payment-form']//input[@name='expiration']")
    expiration_input.send_keys("1234567")

    cvv_input = driver.find_element(By.XPATH, "//form[@class='payment-form']//input[@name='cvv']")
    cvv_input.send_keys("000")

    buy_now_button = driver.find_element(By.XPATH, "//form[@class='payment-form']//button[text()='Buy now']")
    buy_now_button.click()

    # navigate to shop page
    shop_link = driver.find_element(By.XPATH, "(//a[@href='/store'])[1]")
    shop_link.click()

    # click on Oranges
    oranges_review_click = driver.find_element(By.XPATH, "//p[text()='Oranges']")
    oranges_review_click.click()

    #star_review_input = driver.find_element(By.XPATH, "//div[@class='interactive-rating']/span[@class='star filled'][5]")
    star_review_input = driver.find_element(By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[5]")
    star_review_input.click()

    text_review = driver.find_element(By.XPATH, "//textarea[@class='new-review-form-control ']")
    text_review.send_keys("A")

    send_review_button = driver.find_element(By.XPATH, "//button[@class= 'new-review-btn new-review-btn-send']")
    send_review_button.click()

    #check if review with text limited is visible
    #check if test review without stars is displayed
    #check if test average review is displayed
    #check if test review without text is displayed

# def test_limited_characters == 500 characters, > 500 characters, < 500 characters
# def test_review_without_stars
# def test_average_review
# def test_review_without_text









