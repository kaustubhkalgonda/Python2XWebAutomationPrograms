from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, allure, pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with

from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.smoke
@allure.title("Relative locator username error message.")
@allure.description("Relative locator username error message.")
def test_mini_project07():
    driver = webdriver.Chrome()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")
    driver.find_element(By.XPATH, "//button[@aria-label='Close Ad']").click()

    driver.switch_to.frame("result")
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    username_error_element = driver.find_element(locate_with(By.TAG_NAME, "small").below({By.ID: "username"}))
    assert username_error_element.text == "Username must be at least 3 characters"
