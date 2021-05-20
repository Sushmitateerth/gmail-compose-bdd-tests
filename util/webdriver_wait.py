from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_element(driver, locator):
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator)
    )