from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.basePage import basePage
from datetime import date, timedelta


class shopPage(basePage):
    # locators
    AGE_INPUT = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div/input")
    AGE_INPUT_CONFIRM_BUTTON = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div/button")
    ADD_TO_CART_GALA_APPLES_BUTTON = (By.XPATH, "//p[text()='Gala Apples']/ancestor::div[@class='card']//button[text()='Add to Cart']")
    SHOPPING_CART_ICON = (By.XPATH, "//div[@class='headerIcon'][3]")
    NAVIGATE_BOUGHT_GALA_APPLES_IMAGE = (By.XPATH, "//p[text()='Gala Apples']")
    CATEGORY_ALOCOHOL_MENU_LINK = (By.XPATH, "//a[@href='#' and text()='Alocohol']")
    ALOCOHOL_CATEGORY_TEXT = (By.XPATH, "//a[@href='#!' and text()='Alocohol']")
    ALCOHOL_BUTTON = (By.XPATH, "//a[@href='#' and text()='Alocohol']")
    NO_ACCESS_TO_ALCOHOL_TEXT = (By.XPATH, "//div[@class='card-body']")


    @classmethod
    def open_shop_with_age(cls, driver):
        page =  shopPage(driver)
        page.enter_default_age()
        return page

    def enter_age(self, age):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.AGE_INPUT)).send_keys(age)

    def click_confirm_Age(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.AGE_INPUT_CONFIRM_BUTTON)).click()

    def click_gala_apples_to_cart(self):
        self.click(self.ADD_TO_CART_GALA_APPLES_BUTTON)

    def click_shopping_cart_icon(self):
        self.click(self.SHOPPING_CART_ICON)

    def click_gala_apples_to_make_review(self):
        self.click(self.NAVIGATE_BOUGHT_GALA_APPLES_IMAGE)

        # open alcohol menu
    def click_alcohol_menu(self):
        self.click(self.CATEGORY_ALOCOHOL_MENU_LINK)

    def get_text_alocohol(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ALOCOHOL_CATEGORY_TEXT)).is_displayed()
        #return self.find_element(self.ALOCOHOL_PRODUCT_TITLE)

    def click_alcohol_btn(self):
        self.click(self.ALCOHOL_BUTTON)

    def get_message_no_access_to_alcohol(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NO_ACCESS_TO_ALCOHOL_TEXT))

    def get_invalid_age_verification_msg(self):
        self.click_alcohol_btn()
        return self.get_message_no_access_to_alcohol()

    def enter_default_age(self):
        age = "22-05-1988"
        self.enter_age(age)
        self.click_confirm_Age()

    def enter_underage_date(self):
        age = "20-07-2009"
        self.enter_age(age)
        self.click_confirm_Age()

    def enter_age_format_dot(self):
        age = "20.07.1977"
        self.enter_age(age)
        self.click_confirm_Age()

    def enter_age_format_slash(self):
        age = "17/03/1999"
        self.enter_age(age)
        self.click_confirm_Age()

    def enter_age_format_only_num(self):
        age = "1234567"
        self.enter_age(age)
        self.click_confirm_Age()
