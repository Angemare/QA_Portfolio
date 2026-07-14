from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.basePage import basePage


class shopPage(basePage):
    # locators
    AGE_INPUT = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div/input")
    AGE_INPUT_CONFIRM_BUTTON = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div/button")
    ADD_TO_CART_GALA_APPLES_BUTTON = (By.XPATH, "//p[text()='Gala Apples']/ancestor::div[@class='card']//button[text()='Add to Cart']")
    SHOPPING_CART_ICON = (By.XPATH, "//div[@class='headerIcon'][3]")
    NAVIGATE_BOUGHT_GALA_APPLES_IMAGE = (By.XPATH, "//p[text()='Gala Apples']")
    CATEGORY_ALOCOHOL_MENU_LINK = (By.XPATH, "//a[@href='#' and text()='Alocohol']")
    ALOCOHOL_PRODUCT_TITLE = (By.XPATH, "//p[@class='lead' and text()='Perlenbacher Pilsner Lager']")


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

    def find_alocohol_product(self):
        self.find_element(self.ALOCOHOL_PRODUCT_TITLE)
