import os
from selenium import webdriver
from config import info
from generalFunction import beforeTest, screenshot, sharePoint
from pathlib import Path

# Declare driver Chrome
driver = webdriver.Chrome()

def example():
    beforeTest(driver, info().get('appUrl'))

    # screenshot(driver, "home", "test_home_screen", True)

    # Get current folder
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Create folder path
    path = os.path.join(current_dir, "json")
    # Get all the Json file in current directory
    fileJson = ""
    # Go into that directory
    entries = Path(path)
    # For loop through the file in that folder
    for entry in entries.iterdir():
        fileJson = fileJson + '"' + str(entry.name) + '" '
    # Create file path
    filePath = f"{path}\{fileJson}"

    sharePoint(driver, info().get('sharepointUrl'), filePath)
