from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, allure, pytest


def test_svg_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    actions = ActionChains(driver)
    driver.find_element(By.XPATH, "//input[@name='q']").send_keys("AC")
    search_button = driver.find_element(By.XPATH, "//*[name()='svg' and contains(@xmlns,'w3.org')]")
    actions.move_to_element(search_button).click().perform()

    time.sleep(5)
