from selenium.webdriver.common.by import By
from main.basePage import basePage


class HomePage(basePage):
    # locators as tuples
    SHOP_BUTTON = (By.XPATH, "//a[@href='/store']")


    def click_shop_btn(self):
        self.click(self.SHOP_BUTTON)