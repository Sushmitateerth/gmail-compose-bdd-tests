from behave import *
from selenium.webdriver.common.by import By

from util.webdriver_wait import get_element


@given('user enters To:"{to}", Subject:"{subject}" and Body:"{body}"')
def step_impl(context, to, subject, body):
    # Composes email with given parameters
    get_element(context.driver, (By.XPATH, "//a[@accesskey='c']")).click()
    get_element(context.driver, (By.NAME, "to")).send_keys(to)
    get_element(context.driver, (By.NAME, "subject")).send_keys(subject)
    get_element(context.driver, (By.NAME, "body")).send_keys(body)


@when('user clicks on send')
def step_impl(context):
    # Sends email
    get_element(context.driver, (By.CSS_SELECTOR, "input[value='Send']")).click()


@then('email is sent successfully')
def step_impl(context):
    # Verifies that email is sent successfully
    expected_msg = get_element(context.driver, (By.XPATH, "//b[contains(text(),'Your message has been sent.')]")).text
    actual_msg = "Your message has been sent."
    assert expected_msg == actual_msg
