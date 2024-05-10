from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, allure, pytest
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.smoke
@allure.title("Add user and then search in OrangeHRM.")
@allure.description("Add user and then search in OrangeHRM.")
def test_mini_project06():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[contains(@class,'login-button')]").click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Admin']")))
    driver.find_element(By.XPATH, "//span[text()='Admin']").click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'oxd-button')]//i")))
    driver.find_element(By.XPATH, "//button[contains(@class,'oxd-button')]//i").click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Add User']")))

    # select user role
    driver.find_element(By.XPATH,
                        "//div[@class='oxd-form-row']//div[contains(@class,'orangehrm-full')]/div[1]//div[contains(@class,'select-text-input')]").click()
    driver.find_element(By.XPATH,
                        "//div[@class='oxd-form-row']//div[contains(@class,'orangehrm-full')]/div[1]//div[contains(@class,'select-wrapper')]//div[@role='listbox']//span[text()='Admin']").click()

    # enter employee name
    driver.find_element(By.XPATH,
                        "//div[@class='oxd-form-row']//div[contains(@class,'orangehrm-full')]/div[2]//div[contains(@class,'text-input')]//input").send_keys(
        "Bruce")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//div[@class='oxd-form-row']//div[contains(@class,'orangehrm-full')]/div[2]//div[@role='listbox']//span[text()='Bruce Randall York']"))).click()

    # select status
    driver.find_element(By.XPATH,
                        "//div[@class='oxd-form-row']//div[contains(@class,'orangehrm-full')]/div[3]//div[contains(@class,'select-text-input')]").click()
    driver.find_element(By.XPATH,
                        "//div[@class='oxd-form-row']//div[contains(@class,'orangehrm-full')]/div[3]//div[contains(@class,'select-wrapper')]//div[@role='listbox']//span[text()='Enabled']").click()

    # enter username
    driver.find_element(By.XPATH,
                        "//div[@class='oxd-form-row']//div[contains(@class,'orangehrm-full')]/div[4]//input").send_keys(
        "kadmink2234")

    # enter password
    driver.find_element(By.XPATH,
                        "//div[contains(@class,'user-password')]//div[contains(@class,'user-password')]//input[@type='password']").send_keys(
        "kkadmin123")

    # enter confirm password
    driver.find_element(By.XPATH,
                        "//div[contains(@class,'user-password')]//div[@class='oxd-grid-item oxd-grid-item--gutters']//input[@type='password']").send_keys(
        "kkadmin123")

    # click save button
    driver.find_element(By.XPATH,
                        "//button[@type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//div[contains(@class,'table-body')]/div")))

    # search for added user
    rows_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'table-body')]/div")
    rows = len(rows_elements)

    for i in range(1, rows + 1):
        name_element = driver.find_element(By.XPATH, "//div[contains(@class,'table-body')]/div[" + str(i) + "]//div[2]")
        if name_element.text.strip(" ") == "kadmink2234":
            print("User successfully created.")
            break
