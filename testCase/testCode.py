import os
from selenium import webdriver
from config import info
from generalFunction import beforeTest, screenshot, sharePoint

# Declare driver Chrome
driver = webdriver.Chrome()

def example():
    beforeTest(driver, info().get('appUrl'))

    # screenshot(driver, "home", "test_home_screen", True)

    # Get current folder
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Create folder path
    path = os.path.join(current_dir, "json")

    # Create file path
    filePath = f"{path}\demo.json"

    sharePoint(driver, info().get('sharepointUrl'), filePath)
