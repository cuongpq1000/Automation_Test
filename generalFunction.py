import time
from selenium.webdriver.common.by import By
from config import info

def nextSignIn(driver):
    button = driver.find_element(By.XPATH, "//input[@data-report-event = 'Signin_Submit']")
    button.click()

    # Wait 2 seconds
    time.sleep(2)

def login(driver):
    # Find element: User Name
    userName = driver.find_element(By.NAME, 'loginfmt')

    # Put value in User Name
    userName.send_keys(info.get("username"))

    # Click Next
    nextSignIn(driver)

    # Find element: Password
    passWord = driver.find_element(By.NAME, "passwd")

    # Put value in PassWord
    passWord.send_keys(info.get("password"))

    # Click Next
    nextSignIn(driver)

    # Click Next
    nextSignIn(driver)

def beforeTest(driver, url):
    # Open link
    driver.get(url)

    # Full screen
    driver.maximize_window()

    # Wait 3 seconds
    time.sleep(3)

    # login
    login(driver)