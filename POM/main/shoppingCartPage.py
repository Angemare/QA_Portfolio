from selenium.webdriver.common.by import By
from main.basePage import basePage


class shoppingCartPage(basePage):

    # locators as tuples
    SHIPMENT_STREET_INPUT = (By.XPATH, "//form[@class='payment-form']//input[@name='street']")
    SHIPMENT_CITY_INPUT = (By.XPATH, "//form[@class='payment-form']//input[@name='city']")
    SHIPMENT_POSTALCODE_INPUT = (By.XPATH, "//form[@class='payment-form']//input[@name='postalCode']")
    PAYMENT_CARDNUMBER_INPUT = (By.XPATH, "//form[@class='payment-form']//input[@name='cardNumber']")
    PAYMENT_NAME_ON_CARD_INPUT = (By.XPATH, "//form[@class='payment-form']//input[@name='nameOnCard']")
    PAYMENT_EXPIRATION_DATE_INPUT = (By.XPATH, "//form[@class='payment-form']//input[@name='expiration']")
    PAYMENT_CVV_INPUT = (By.XPATH, "//form[@class='payment-form']//input[@name='cvv']")
    BUY_NOW_BUTTON = (By.XPATH, "//form[@class='payment-form']//button[text()='Buy now']")


    # enter shipment address details
    def enter_street(self, street):
        street_input = self.driver.find_element(*self.SHIPMENT_STREET_INPUT)
        street_input.send_keys(street)

    def enter_city(self, city):
        city_input = self.driver.find_element(*self.SHIPMENT_CITY_INPUT)
        city_input.send_keys(city)

    def enter_postalcode(self, postalcode):
        postalcode_input = self.driver.find_element(*self.SHIPMENT_POSTALCODE_INPUT)
        postalcode_input.send_keys(postalcode)

    # enter payment details and click buy now button
    def enter_card_number(self, cardnumber):
        cardnumber_input = self.driver.find_element(*self.PAYMENT_CARDNUMBER_INPUT)
        cardnumber_input.send_keys(cardnumber)

    def enter_name_on_card(self, name_on_card):
        name_on_card_input = self.driver.find_element(*self.PAYMENT_NAME_ON_CARD_INPUT)
        name_on_card_input.send_keys(name_on_card)

    def enter_expiration_date(self, expiration_date):
        expiration_date_input = self.driver.find_element(*self.PAYMENT_EXPIRATION_DATE_INPUT)
        expiration_date_input.send_keys(expiration_date)

    def enter_cvv(self, cvv):
        cvv_input = self.driver.find_element(*self.PAYMENT_CVV_INPUT)
        cvv_input.send_keys(cvv)

    def click_buy_now(self):
        self.click(self.BUY_NOW_BUTTON)





