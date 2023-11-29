# example_steps.py
import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Reusable import ReuableMethod as rm


@when('lunch the url of orrangehrm application')
def step_lunch_url_app(context):
    rm.lunch("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

@then('enter the "{username}" and "{password}" to orangehrm application')
def step_enter_username_password(context,username,password):
    rm.enterText("name", "username", username)
    rm.enterText("xpath", "//input[@name='password']", password)

@then('click on the login button on orangehrm application')
def step_click_login(context):
    rm.click("xpath", "//button[@type='submit']")
@then('verify the "{title}" orangehrm application')
def verify_title(title):
    time.sleep(5)
    rm.validateText(title, rm.getTitle())

