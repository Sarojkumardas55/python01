import time
from Executeablescript import LoginPage as lp
from Reusable import ReuableMethod as rm
from Executeablescript import AddEducation as ae

def select_Education(name):
    rm.click("xpath",f'//div[text()="+str{name}+"]//preceding::input[@type="checkbox"][1]')
    time.sleep(2)

def click_Delete(name):
    rm.click("xpath",f'//div[text()="+str{name}+"]//following::i[@class="oxd-icon bi-trash"][1]')
    time.sleep(2)
def click_Yes():
    rm.click("xpath",'//button[text()=" Yes, Delete "]')
    time.sleep(2)
lp.login_App()
ae.click_admin_menu()
ae.click_qualificatios_tab()
ae.click_education_dd()
select_Education("High")
click_Delete("High")
click_Yes()
time.sleep(2)
lp.logout_App()