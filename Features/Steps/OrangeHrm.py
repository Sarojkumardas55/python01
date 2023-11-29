import time

from behave import *
from Executeablescript import LoginPage as lp
from Executeablescript import AddEducation as ae
from Reusable import ReuableMethod as rm


@when('lunch the url and login to orrangehrm application')
def login_App():
    rm.lunch("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    rm.waitUntilElementVisiable(15, "name", "username")
    rm.enterText("name", "username", "Admin")
    rm.enterText("xpath", "//input[@name='password']", "admin123")
    rm.click("xpath", "//button[@type='submit']")
    # rm.validateText("OrangeHrm",rm.getTitle())
    time.sleep(5)

@Then('click admin menu')
def click_admin_menu():
    rm.click("xpath","//span[text()='Admin']")


@Then('Click on qualification tab')
def click_qualificatios_tab():
    rm.click("xpath","//span[text()='Qualifications ']")


@Then('select add education from list')
def click_education_dd():
    rm.click("xpath","//a[text()='Education']")


@Then('click on add button')
def click_add():
    rm.click("xpath","//button[text()=' Add ']")


@Then('add education "{Name}"')
def add_Education(text):
    rm.enterText("xpath","//label[text()='Level']//following::div[1]//input",text)


@Then('check and save')
def check_and_save_cancel():
    flag=rm.isElementPresent("xpath","//span[text()='Already exists']")
    if flag==True:
  #  if rm.getText("xpath","//span[text()='Already exists']")=="Already exists":
        rm.click("xpath", "//button[text()=' Cancel ']")
    else:
        rm.click("xpath","//button[text()=' Save ']")


@Then('logout from application')
def logout_App():
    rm.click("xpath","//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    rm.click("xpath","//a[text()='Logout']")


@then('I close the browser orangehrm application')
def step_then_close_browser():
    rm.tearDown()


@Then('wait for "{min}" second')
def step_wait(min):
    time.sleep(min)
