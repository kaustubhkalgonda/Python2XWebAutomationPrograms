from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, allure, pytest


@pytest.mark.smoke
@allure.title("Update Employee Receord in OrangeHRM.")
@allure.description("Update Employee Receord in OrangeHRM.")
def test_mini_project05():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[contains(@class,'login-button')]").click()
    time.sleep(3)
    rows_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'table-body')]/div")
    rows = len(rows_elements)

    for i in range(1, rows + 1):
        name_element = driver.find_element(By.XPATH, "//div[contains(@class,'table-body')]/div[" + str(i) + "]//div[3]")
        if name_element.text.strip(" ") == "Emily":
            edit_element = driver.find_element(By.XPATH, "//div[contains(@class,'table-body')]/div[" + str(
                i) + "]//div[3]/following-sibling::div[6]//button/i[contains(@class,'pencil-fill')]")
            edit_element.click()
            time.sleep(3)
            driver.find_element(By.XPATH, "//a[contains(@href,'JobDetails')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH,
                                "//div[@class='oxd-form-row']/div/div[7]//div[contains(@class,'text-input')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//div[@role='listbox']//span[text()='Freelance']").click()
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(3)
            driver.find_element(By.XPATH, "//a[text()='Employee List']").click()
            time.sleep(3)
            employee_status_element = driver.find_element(By.XPATH, "//div[contains(@class,'table-body')]/div[" + str(
                i) + "]//div[3]/following-sibling::div[3]")
            if employee_status_element.text=="Freelance":
                print("Test Case Passed")
                break
            else:
                print("Test Case Failed.")