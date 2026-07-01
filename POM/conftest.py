import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(8)
    driver.get("https://grocerymate.masterschool.com/auth")

    yield driver

    driver.quit()
