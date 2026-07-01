from selenium.webdriver.common.by import By




def test_ratingsystem(driver):
    username_login_input = driver.find_element(By.XPATH, "//form[@class='form']//input[@type='email']")
    username_login_input.send_keys("a.stragies@gmx.de")

    password_login_input = driver.find_element(By.XPATH, "//form[@class='form']//input[@type='password']")
    password_login_input.send_keys("lalalalala")

    signin_button = driver.find_element(By.XPATH, "//button[text()='Sign In']")
    signin_button.click()

    shop_link = driver.find_element(By.XPATH, "(//a[@href='/store'])[1]")
    shop_link.click()

    birthdate_input = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div/input")
    birthdate_input.send_keys("22-05-1988")

    confirm_birthdate_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div/button")
    confirm_birthdate_button.click()

    orange_add_to_cart_button = driver.find_element(By.XPATH, "//p[text()='Oranges']/ancestor::div[@class='card']//button[text()='Add to Cart']")
    orange_add_to_cart_button.click()

    shoppingcart_link = driver.find_element(By.XPATH, "//div[@class='headerIcon'][3]")
    shoppingcart_link.click()

















