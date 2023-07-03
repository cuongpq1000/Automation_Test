from selenium.webdriver.common.by import By

def getElementByAttribute(driver, tag, attribute, value):
    value = value.split(' ')
    text = []
    for item in value:
        text.append(f"contains(@{attribute}, '{item}')")
    xpath = f"//{tag}[{' and '.join(text)}]"
    return driver.find_element(By.XPATH, xpath)