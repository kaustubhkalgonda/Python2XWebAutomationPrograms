from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time, allure, pytest

def test_implicit_wait():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://app.vwo.com/#/login")

    driver.find_element(By.ID,"login-username").send_keys("kaustubh@gmail.kom")
    driver.find_element(By.ID,"login-password").send_keys("kaustubh@gmail.kom")
    driver.find_element(By.ID, "js-login-btn").click()

    assert driver.find_element(By.ID,"js-notification-box-msg").is_displayed()
