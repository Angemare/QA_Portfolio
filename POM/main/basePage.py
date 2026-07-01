

class basePage:
    def __init__(self, driver):
        self.driver = driver


    def click(self, locator):
        element = self.driver.find_element(*locator) # element finden
        element.click() # element anklicken