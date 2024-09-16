import Pytest
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.regressiontest
def test_send_keys():
    service = Service()
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    browser.get("https://www.ebay.com")
    browser.find_element(By.NAME, "_nkw").send_keys("Dress"+Keys.ENTER)
