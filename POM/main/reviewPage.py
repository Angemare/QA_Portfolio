from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.basePage import basePage


class reviewPage(basePage):

    # locator as tuples
    STAR_REVIEW_INPUT = (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[5]")
    TEXT_REVIEW_INPUT = (By.XPATH, "//textarea[@class='new-review-form-control ']")
    SEND_REVIEW_BUTTON = (By.XPATH, "//button[@class= 'new-review-btn new-review-btn-send']")
    SENT_TEXT_REVIEW = (By.XPATH, "//div[@class='comment-body']//p")
    MAX_500_CHAR_TEXT_REVIEW_ERROR_MESSAGE = (By.XPATH, "//p[@class='error-message' and text()='You cannot tell us more about this product.']")
    SENT_STAR_REVIEW = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[2]/div/div/div/span[5]")
    CLICK_MEATBALLS_MENU_BUTTON = (By.XPATH, "//div[@class='menu-icon']")
    DELETE_REVIEW_BUTTON = (By.XPATH, "//div[@class='dropdown-menu']//button[text()='Delete']")
    AVERAGE_REVIEW_GALA_APPLES = (By.XPATH, "//p[@class='reviews']")
    REVIEW_NOT_ABLE_TO_SEND_ERROR_POPUP = (By.XPATH, "//*[@id='root']/div/section/section[1]/div[1]/div/div/div[2]")

    # add your review and click send
    def enter_star_review(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.STAR_REVIEW_INPUT)).click()

    def enter_text_review(self, text_review):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TEXT_REVIEW_INPUT)).send_keys(text_review)

    def send_review(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEND_REVIEW_BUTTON)).click()

    # check if review is visible
    def check_text_review(self):
        return self.find_element(self.SENT_TEXT_REVIEW).text

    def check_star_review(self):
        self.find_element(self.SENT_STAR_REVIEW)

    # review löschen mit selenium locator finden
    def click_meatballs_menu(self):
        self.click(self.CLICK_MEATBALLS_MENU_BUTTON)

    def delete_review(self):
        self.click(self.DELETE_REVIEW_BUTTON)

    def error_message_appears(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MAX_500_CHAR_TEXT_REVIEW_ERROR_MESSAGE))
        return self.find_element(self.MAX_500_CHAR_TEXT_REVIEW_ERROR_MESSAGE).is_displayed()

    def dynamic_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.REVIEW_NOT_ABLE_TO_SEND_ERROR_POPUP))

    def average_review_gala_apples(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.AVERAGE_REVIEW_GALA_APPLES))