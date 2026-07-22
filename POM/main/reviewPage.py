from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.basePage import basePage


class reviewPage(basePage):

    # locator
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
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.STAR_REVIEW_INPUT)).click()

    def enter_text_review(self, text_review):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TEXT_REVIEW_INPUT)).send_keys(text_review)

    def send_review(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.SEND_REVIEW_BUTTON)).click()

    # check if review is visible
    def check_text_review(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SENT_TEXT_REVIEW)).text
        #return self.find_element(self.SENT_TEXT_REVIEW).text

    def check_star_review(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SENT_STAR_REVIEW)).is_displayed()
        #return self.find_element(self.SENT_STAR_REVIEW).is_displayed()

    # review löschen mit selenium locator finden
    def click_meatballs_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CLICK_MEATBALLS_MENU_BUTTON)).click()
        #self.click(self.CLICK_MEATBALLS_MENU_BUTTON)

    def delete_review(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DELETE_REVIEW_BUTTON)).click()

    def get_limited_char_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MAX_500_CHAR_TEXT_REVIEW_ERROR_MESSAGE)).is_displayed()

    def get_review_error_message_popup(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.REVIEW_NOT_ABLE_TO_SEND_ERROR_POPUP))

    def get_average_review_gala_apples(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.AVERAGE_REVIEW_GALA_APPLES))