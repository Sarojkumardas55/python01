import time
from Executeablescript import LoginPage as lp
from Reusable import ReuableMethod as rm

def click_admin_menu():
    rm.click("xpath","//span[text()='Admin']")
    time.sleep(2)
def click_qualificatios_tab():
    rm.click("xpath","//span[text()='Qualifications ']")
def click_education_dd():
    rm.click("xpath","//a[text()='Education']")
    time.sleep(2)
def click_add():
    rm.click("xpath","//button[text()=' Add ']")
    time.sleep(2)
def add_Education(text):
    rm.enterText("xpath","//label[text()='Level']//following::div[1]//input",text)
    time.sleep(2)
def check_and_save_cancel():
    flag=rm.isElementPresent("xpath","//span[text()='Already exists']")
    if flag==True:
  #  if rm.getText("xpath","//span[text()='Already exists']")=="Already exists":
        rm.click("xpath", "//button[text()=' Cancel ']")
    else:
        rm.click("xpath","//button[text()=' Save ']")

#lp.login_App()
click_admin_menu()
click_qualificatios_tab()
click_education_dd()
click_add()
add_Education("text")
check_and_save_cancel()
##time.sleep(2)
lp.logout_App()