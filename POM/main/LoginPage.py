from selenium.webdriver.common.by import By
from main.basePage import basePage


class LoginPage(basePage):
    # locators as tuples
    USERNAME_LOGIN_INPUT = (By.XPATH, "//form[@class='form']//input[@type='email']")
    PASSWORD_LOGIN_INPUT = (By.XPATH, "//form[@class='form']//input[@type='password']")
    SIGNIN_BUTTON = (By.XPATH, "//button[text()='Sign In']")

    def enter_username(self, username):
        username_input = self.driver.find_element(*self.USERNAME_LOGIN_INPUT)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_LOGIN_INPUT)
        password_input.send_keys(password)

    def click_signin_btn(self):
        self.click(self.SIGNIN_BUTTON)




