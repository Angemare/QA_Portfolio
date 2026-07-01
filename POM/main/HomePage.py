from basepage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    SHOP_BUTTON = (By.XPATH, "//a[@href='/store'])[1]")


    def click_shop_btn(self):
        self.click(self.SHOP_BUTTON)