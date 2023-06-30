import numpy as np
from selenium import webdriver
from excel import *
from generalFunction import *
import time

def readTestCase(data):
    testCaseList = []
    testCase = {}
    isAddTestCase = False

    for row in data:
        if row[0] is not np.nan and isAddTestCase is True:
            testCaseList.append(testCase)
            testCase = {}

        if row[0] is not np.nan:
            testCase["name"] = row[0]
            testCase["testStep"] = [row[2]]
            testCase["url"] = row[1]
            isAddTestCase = True
        else:
            testCase["testStep"].append(row[2])
    testCaseList.append(testCase)
    return testCaseList


def excuteTest(functionName, testCase):
    print("excute test case >>", testCase["name"])
    driver = webdriver.Chrome()
    result = {"name": testCase["name"], "result": None, "screenshot": []}
    beforeTest(driver, testCase["url"])
    time.sleep(10)
    for step in testCase["testStep"]:
        print("run >>", step)
        if(step == "create"):
            button = getElementByAttribute(driver, "button", "data-id", "NewRecord")
            button.click()
        if(step == "screenshot"):
            image = screenshot(driver, functionName, testCase["name"], False)
            result["screenshot"].append(image)
        result["result"] = "Pass"
    driver.close()
    return result


def run():
    path = getPath("testCase/input/Demo.xlsx")
    df = readExcel(path, "Sheet1")
    functionName = getCell(df, 0, 0)
    data = df.values[2:]
    testCaseList = readTestCase(data)
    testResult = []
    for testCase in testCaseList:
        result = excuteTest(functionName, testCase)
        testResult.append(result)

    writeExcel(testResult, "TestResult.xlsx")
