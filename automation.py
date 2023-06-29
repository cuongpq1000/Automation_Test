import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

from config import info
from generalFunction import beforeTest
# Declare driver Chrome
driver = webdriver.Chrome()

def screenshot():
    beforeTest(
        driver,
        info.get('appUrl')
    )

    # Open link
    #driver.get("https://org26e7f761.crm5.dynamics.com/main.aspx?appid=77974422-fde3-ed11-8846-000d3a854b1d&pagetype=entityrecord&etn=crd55_tb_employees&id=8f73f474-1aea-ed11-8847-000d3a854b1d")

    # Wait 2 seconds
    time.sleep(2)

    driver.save_screenshot("imageTest2.png")

    # Loading the image
    image = Image.open("imageTest2.png")

    # Showing the image
    image.show()

    # Wait 2 seconds
    #time.sleep(20000)

    # Find element: Employee Code
    #employCode = driver.find_element(By.XPATH, "//input[@id = 'id-a893ef20-2e15-48b5-bc20-16f9e33b1cf0-1-crd55_employeecode4273edbd-ac1d-40d3-9fb2-095c621b552d-crd55_employeecode.fieldControl-text-box-text']")

    # Wait 5 seconds
    #time.sleep(10000)

screenshot()