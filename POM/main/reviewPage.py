from selenium.webdriver.common.by import By
from main.basePage import basePage


class reviewPage(basePage):

    # locator as tuples
    STAR_REVIEW_INPUT = (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[5]")
    TEXT_REVIEW_INPUT = (By.XPATH, "//textarea[@class='new-review-form-control ']")
    SEND_REVIEW_BUTTON = (By.XPATH, "//button[@class= 'new-review-btn new-review-btn-send']")
    SENT_TEXT_REVIEW = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div")
    CLICK_MEATBALLS_MENU_BUTTON = (By.XPATH, "//div[@class='menu-icon']")
    DELETE_REVIEW_BUTTON = (By.XPATH, "//button[text()='Delete']")
    MAX_500_CHAR_TEXT_REVIEW_ERROR_MESSAGE = (By.XPATH, "//p[@class='error-message' and text()='You cannot tell us more about this product.']")
    SENT_STAR_REVIEW = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[2]/div/div/div/span[5]")


    # add your review and click send
    def enter_star_review(self):
        self.click(self.STAR_REVIEW_INPUT)

    def enter_text_review(self, text_review):
        text_review_input = self.driver.find_element(*self.TEXT_REVIEW_INPUT)
        text_review_input.send_keys(text_review)

    def send_review(self):
        self.click(self.SEND_REVIEW_BUTTON)

    # check if review is visible
    def check_text_review(self):
        self.find_element(self.SENT_TEXT_REVIEW)

    def check_star_review(self):
        self.find_element(self.SENT_STAR_REVIEW)

    # review löschen mit selenium locator finden
    def click_meatballs_menu(self):
        self.click(self.CLICK_MEATBALLS_MENU_BUTTON)

    def delete_review(self):
        self.click(self.DELETE_REVIEW_BUTTON)

    def error_message_appears(self):
        self.find_element(self.MAX_500_CHAR_TEXT_REVIEW_ERROR_MESSAGE)

