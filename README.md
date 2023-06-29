# Automation_Test
    Run: py -m pip install selenium
    Run: py -m pip install Image

# Step create test case
    Step 1: In folder testCase create [testCaseName].py
    Step 2: In file __init__.py add "from .[testCaseName] import *"
    Step 3: Call your function from [testCaseName].py in "automation.py"
    Step 4: Run "py -m automation.py"

# Walkthourgh example
    from selenium import webdriver
    from config import info
    from generalFunction import beforeTest, screenshot

    # Declare driver Chrome
    driver = webdriver.Chrome()

    def example():
        # Call function login
        beforeTest(driver, info().get('appUrl'))

        # Call function screenshot
        screenshot(driver, "home", "test_home_screen", True)

# Call function login
    beforeTest(driver, [url])

# Call function screenshot
    # [page name] name of folder contains test result image (string)
    # [test case name] children folder of [page name] (string)
    # [show image] open image after screenshot (True / False)
    screenshot(driver, [page name], [test case name], [show image])