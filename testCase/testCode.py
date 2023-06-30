from selenium import webdriver
from config import info
from generalFunction import beforeTest, screenshot, sharePoint, getfilePath
from excel import convertExceltoJSON

# Declare driver Chrome
driver = webdriver.Chrome()

def example():
    convertExceltoJSON("file_example_XLS_10.xls", "upload_demo.json")

    beforeTest(driver, info().get('sharepointUrl'))

    filePath = getfilePath("testCase\json", "upload_demo.json")

    sharePoint(driver, info().get('sharepointUrl'), filePath)

    screenshot(driver, "sharepoint", "upload_file_json", False)
