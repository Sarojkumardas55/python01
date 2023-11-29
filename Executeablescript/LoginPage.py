import time

from Reusable import ReuableMethod as rm

def login_App():
    rm.lunch("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    rm.waitUntilElementVisiable(15, "name", "username")
    rm.enterText("name", "username", "Admin")
    rm.enterText("xpath", "//input[@name='password']", "admin123")
    rm.click("xpath", "//button[@type='submit']")
    # rm.validateText("OrangeHrm",rm.getTitle())
    time.sleep(5)

def logout_App():
    rm.click("xpath","//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    rm.click("xpath","//a[text()='Logout']")
    time.sleep(2)