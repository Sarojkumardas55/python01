import requests as request
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import*
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#ser=Service("C:\Selenium")
driver= webdriver.Chrome()
# driver.get("https://ewebdevelopment.com/quotes/inquire/openchart.com")
driver.maximize_window()
#driver=lunchDriver()
def lunchDriver(dname):
    if dname == "chrome":
        driver= webdriver.chrome()
       # driver.maximize_window()
    elif dname=="filefox":
        driver=webdriver.Firefox()
        driver.maximize_window()
    elif dname=="edge":
        driver=webdriver.Edge()
        driver.maximize_window()
    else:
        print("Enter correct driver")
    return driver


#driver = lunchDriver("chrome")
def isElementPresent(type,locator):
    try:
        if type == "name":
            flag = driver.find_element(By.NAME, locator).is_displayed()
            return flag
        elif type == "id":
            flag = driver.find_element(By.ID, locator).is_displayed()
            return flag
        elif type == "class":
            flag = driver.find_element(By.CLASS_NAME, locator).is_displayed()
            return flag
        elif type == "xpath":
            flag = driver.find_element(By.XPATH, locator).is_displayed()
            return flag
    except NoSuchElementException as e:
      print(f"Element not found: {e}")
      return flag
    except ElementNotVisibleException as e:
        print(f"Element not visiable: {e}")
        return flag

def isElementEnable(By):
    try:
      flag=driver.find_element(By).is_enabled()
      return flag
    except ElementNotInteractableException as e:
      print(f"Element not interactable: {e}")
      return flag

def waitTime(f):
    driver.implicitly_wait(f)

def waitUntilEleentVisiable(By,time):
    try:
     wait = WebDriverWait(driver, time)
     wait.until(EC.presence_of_element_located(By))
    except ElementNotVisibleException as e:
     print(f"Element not visiable: {e}")
def waitUntilElementVisiable(time,type,locator):
    try:
     wait = WebDriverWait(driver, time)
     if type=="name":
       wait.until(EC.presence_of_element_located((By.NAME,locator)))
     elif type=="class":
         wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator)))
     elif type == "id":
         wait.until(EC.presence_of_element_located((By.ID, locator)))
     elif type=="xpath":
         wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    except ElementNotVisibleException as e:
     print(f"Element not visiable: {e}")
def enterText(type,locator,text):
    #if isElementPresent(By)
    if type=="name":
        driver.find_element(By.NAME,locator).send_keys(text)
    elif type=="id":
        driver.find_element(By.ID, locator).send_keys(text)
    elif type=="class":
        driver.find_element(By.CLASS_NAME, locator).send_keys(text)
    elif type=="xpath":
        driver.find_element(By.XPATH, locator).send_keys(text)
    # driver.find_element((By.XPATH,"//input[@name='password']"))

def click(type,locator):
    #if isElementPresent(By):
        if type == "name":
            driver.find_element(By.NAME, locator).click()
        elif type == "id":
            driver.find_element(By.ID, locator).click()
        elif type == "class":
            driver.find_element(By.CLASS_NAME, locator).click()
        elif type == "xpath":
            driver.find_element(By.XPATH, locator).click()

def takeScreenShot(file):
    if isElementPresent(By):
        driver.save_screenshot(file)

def lunch(url):
    driver.get(url)
def tearDown():
    driver.quit()

def getTitle():
    return driver.title

def switchFrame(By):
    if isElementPresent(By):
      driver.switch_to.frame(By)

def switchToDefaultContent():
    driver.switch_to.default_content()

def acceptAlert():
    driver.switch_to.alert.accept()

def rejectAlert():
    driver.switch_to.alert.dismiss()

def selectByVisibleText(By,text):
    ele=driver.find_element(By)
    select=Select(ele)
    select.select_by_visible_text(text)

def selectByValue(By,value):
    ele=driver.find_element(By)
    select=Select(ele)
    select.select_by_value(value)

def selectByIndex(By,index):
    ele=driver.find_element(By)
    select=Select(ele)
    select.select_by_index(index)
def deselectByVisibleText(By,text):
    ele=driver.find_element(By)
    select=Select(ele)
    select.deselect_by_visible_text(text)

def deselectByValue(By,value):
    ele=driver.find_element(By)
    select=Select(ele)
    select.deselect_by_value(value)

def deselectByIndex(By,index):
    ele=driver.find_element(By)
    select=Select(ele)
    select.deselect_by_index(index)

def validateText(exp,act):
    if exp==act:
        print("Validate sucessfuly")
    else:
        print("Validation is not sucessful")

def getText(type,locator):
    if type=="xpath":
        return driver.find_element(By.XPATH, locator).text
    elif type == "class":
        return driver.find_element(By.CLASS_NAME, locator).text
    elif type == "id":
        return driver.find_element(By.ID, locator).text
    elif type == "name":
        return driver.find_element(By.NAME, locator).text