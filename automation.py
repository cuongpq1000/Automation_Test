from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

from config import info
from generalFunction import beforeTest, screenshot, sharePoint
# Declare driver Chrome
driver = webdriver.Chrome()

def example():
    beforeTest(driver, info.get('appUrl'))
    # screenshot(driver, "home", "test_home_screen", True)
    sharePoint(driver, info.get('sharepointUrl'), info.get('directory'))

example()