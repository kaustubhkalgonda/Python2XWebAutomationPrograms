from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time, allure, pytest

def test_actions_scenarios_01():
    driver = webdriver.Chrome()
    #right click
    driver.get("https://the-internet.herokuapp.com/context_menu")
    time.sleep(2)
    actions = ActionChains(driver)
    right_click_box = driver.find_element(By.ID,"hot-spot")
    actions.context_click(right_click_box).perform()
    time.sleep(5)
    Alert(driver).accept()
    time.sleep(3)

    #drag and drop
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    from_element= driver.find_element(By.ID,"column-a")
    to_element = driver.find_element(By.ID, "column-b")
    actions.drag_and_drop(from_element,to_element).perform()
    time.sleep(2)


    #Hover
    driver.get("https://the-internet.herokuapp.com/hovers")
    hover_element= driver.find_element(By.XPATH,"//img[contains(@src,'avatar-blank')]")
    actions.move_to_element(hover_element).perform()
    driver.find_element(By.XPATH,"//a[@href='/users/1']").click()
    time.sleep(3)


def test_actions_scenarios_02():
    driver = webdriver.Chrome()
    #opening new window
    driver.get("https://the-internet.herokuapp.com/windows")
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Click Here']").click()
    windows = driver.window_handles
    for window in windows:
        driver.switch_to.window(window)
        if driver.current_url == "https://the-internet.herokuapp.com/windows/new":
            print("Test Passed.")
        else:
            pass
