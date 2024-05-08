from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, allure, pytest


def test_explicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://www.geeksforgeeks.org/")

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Applied Data Science")))
    element.click()

    assert (driver.current_url
            == "https://www.geeksforgeeks.org/courses/full-stack-applied-data-science-program?utm_source=geeksforgeeks&utm_medium=rightbar_datascience_def&utm_campaign=inbound_promotions")
