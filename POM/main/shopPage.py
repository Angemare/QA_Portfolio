from selenium.webdriver.common.by import By
from main.basePage import basePage


class shopPage(basePage):
    # locators as tuples
    AGE_INPUT = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div/input")
    AGE_INPUT_CONFIRM_BUTTON = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div/button")
    ADD_TO_CART_ORANGES_BUTTON = (By.XPATH, "//p[text()='Oranges']/ancestor::div[@class='card']//button[text()='Add to Cart']")

    def enter_age(self, age):
        age_verification_input = self.driver.find_element(*self.AGE_INPUT)
        age_verification_input.send_keys(age)

    def click_confirm_Age(self):
        self.click(self.AGE_INPUT_CONFIRM_BUTTON)

    def click_oranges_to_cart(self):
        self.click(self.ADD_TO_CART_ORANGES_BUTTON)
