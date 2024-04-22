from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_mini_project():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.find_element(By.ID, "btn-make-appointment").click()
    time.sleep(3)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()
    time.sleep(3)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    assert driver.find_element(By.XPATH, "//h2[normalize-space()='Make Appointment']").text == "Make Appointment"
