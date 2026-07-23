from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class basePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15

    def click(self, locator):
        element = self.driver.find_element(*locator) # element finden
        element.click() # element anklicken

    def getText(self, locator):
        element = self.driver.find_element(*locator) # element finden
        return element.text

    def getDropdown(self, locator):
        element = self.driver.find_element(*locator)
        return Select(element)

    def find_element(self, locator):
        """ Find a single element using Explicit Wait """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator))

