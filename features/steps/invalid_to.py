import time

from behave import *
from selenium.webdriver.common.by import By

from util.webdriver_wait import get_element


@then('error "{error_msg}" is displayed')
def step_impl(context, error_msg):
    # Verifies that appropriate error message is displayed
    actual_text = get_element(context.driver, (By.CSS_SELECTOR, 'td[role="alert"] b')).text
    assert actual_text == error_msg

