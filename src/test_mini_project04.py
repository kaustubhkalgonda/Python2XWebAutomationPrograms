from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, allure, pytest


@pytest.mark.smoke
@allure.title("Verify cheapest 16gb laptop on ebay from search results.")
@allure.description("Verify cheapest 16gb laptop on ebay from search results.")
def test_mini_project04():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("16 gb")
    driver.find_element(By.XPATH, "//input[@value='Search']").click()
    time.sleep(3)
    cheapest_item = None
    cheapest_price = 0.0

    for value in range(1, 61):
        name = driver.find_element(By.XPATH,
                                   "//li[contains(@id,'item')][" + str(value) + "]//span[@role='heading']").text
        print(f"{value}. Name: " + name)
        price = driver.find_element(By.XPATH, "//li[contains(@id,'item')][" + str(
            value) + "]//span[@class='s-item__price']").text
        print("Price: " + price)
        if "$" in price:
            if "to" in price:
                pass
            else:
                new_price = float(price.replace("$", ""))
                if cheapest_price == 0.0:
                    cheapest_price = new_price
                elif new_price < cheapest_price:
                    cheapest_price = price
                    cheapest_item = name

    print(f"Cheapest Item: " + cheapest_item)
    print(f"Cheapest Price: " + str(cheapest_price))
