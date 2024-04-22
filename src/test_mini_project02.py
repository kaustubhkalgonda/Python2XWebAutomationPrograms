from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, allure, pytest


@pytest.mark.smoke
@allure.title("Verify Your Trial has expired message.")
@allure.description("Verify Your Trial has expired message.")
def test_mini_project02():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.find_element(By.ID, "username").send_keys("augtest_040823@idrive.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "frm-btn").click()
    time.sleep(5)
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    assert driver.find_element(By.XPATH, "//h5[@class='id-card-title']").text == "Your free trial has expired"
    allure.attach(driver.get_screenshot_as_png(), name="trial-expired", attachment_type=AttachmentType.PNG)
