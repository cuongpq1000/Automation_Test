import time
import os
from selenium.webdriver.common.by import By
from config import info
from PIL import Image
from datetime import datetime

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

def screenshot(driver, function, testCaseName, isOpen):
    # Get now
    now = datetime.now().strftime("%d_%m_%y_%H_%M_%S")

    # Get current folder
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Create file name
    fileName = f"{now}.png"

    # Create folder path
    path = os.path.join(current_dir, "screenshot", function, testCaseName)

    # Create file path
    filePath = f"{path}/{fileName}"

    # Create folder
    if not os.path.isdir(path):
        os.makedirs(path)

    # Save screenshot
    driver.save_screenshot(filePath)

    if isOpen:
        # Loading the image
        image = Image.open(filePath)
        
        # Showing the image
        image.show()

def beforeTest(driver, url):
    # Open link
    driver.get(url)

    # Full screen
    driver.maximize_window()

    # Wait 3 seconds
    time.sleep(3)

    # login
    login(driver)