from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, allure, pytest


def test_shadow_dom():
    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")

    username = driver.find_element(By.XPATH, "//div[@id='userName']")
    driver.execute_script("arguments[0].scrollIntoView(true);", username)
    time.sleep(3)
    driver.execute_script(
        "document.querySelector('div#userName').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input#pizza').value='Python';")

    time.sleep(3)
