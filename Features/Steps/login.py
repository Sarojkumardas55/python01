# example_steps.py
import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('initialize the driver instance')
def step_initialize_driver(context):
    context.driver = webdriver.Chrome()


@when('lunch the url of application')
def lunch_url_app(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(5)


@then('enter the "{username}" and "{password}" to application')
def step_enter_username_password(context, username, password):
    lc1 = context.driver.find_element("name", "username")
    lc1.send_keys(username)
    lc2 = context.driver.find_element(By.XPATH, "//input[@name='password']")
    lc2.send_keys(password)


@then('click on the login button')
def step_click_login(context):
    lc2 = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    lc2.click()


@then('verify the "{title}"')
def verify_title(context, title):
    time.sleep(5)
    print(context.driver.title)


@then('I close the browser')
def step_then_close_browser(context):
    context.driver.quit()
