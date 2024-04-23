from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, allure, pytest


@pytest.mark.smoke
@allure.title("Verify error message for username field.")
@allure.description("Verify error message for username field.")
def test_mini_project03():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    time.sleep(2)
    driver.switch_to.frame(driver.find_element(By.ID,"result"))
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("123@123.kom")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
    driver.find_element(By.XPATH, "//input[@id='password2']").send_keys("123456")
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="empty-username", attachment_type=AttachmentType.PNG)
    assert (driver.find_element(By.XPATH,
                               "//input[@id='username']/following::small").text
            == "Username must be at least 3 characters")
