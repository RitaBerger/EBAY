import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("item",
                         [
                              "Books",
                              "Dresses",
                              "Toys",
                              "Sandals"
                         ])
def test_simple_search(browser, item):
    service = Service()
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    browser.get("https://www.ebay.com")
    browser.find_element(By.ID, 'gh-ac').send_keys(item + Keys.ENTER)
