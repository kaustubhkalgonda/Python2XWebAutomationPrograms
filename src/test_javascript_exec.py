from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, allure, pytest


def test_javascript_exec():
    driver = webdriver.Chrome()
    driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")

    textfield = driver.find_element(By.NAME, "username")
    driver.execute_script("arguments[0].scrollIntoView(true);",textfield)
    driver.execute_script("arguments[0].value='Python';",textfield)

    btn = driver.find_element(By.NAME,"spbutton")
    driver.execute_script("arguments[0].click();",btn)



    time.sleep(3)
