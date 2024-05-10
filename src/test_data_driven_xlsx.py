import openpyxl
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, allure, pytest, os

file_path = os.getcwd() + "/src/vwo_login_data.xlsx"


def read_credentials_from_file(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({
            "username": username,
            "password": password
        })
    return credentials


@pytest.mark.parametrize("user_cred", read_credentials_from_file(file_path=file_path))
@allure.title("Verify vwo login with invalid credentials.")
@allure.description("Verify vwo login with data from excel sheet.")
def test_vwo_login(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    vwo_login(username=username, password=password)


def vwo_login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    driver.find_element(By.ID, "login-username").send_keys(username)
    driver.find_element(By.ID, "login-password").send_keys(password)
    driver.find_element(By.ID, "js-login-btn").click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "js-notification-box-msg")))
    assert element.is_displayed()
    allure.attach(driver.get_screenshot_as_png(), name="invalid-login", attachment_type=AttachmentType.PNG)
