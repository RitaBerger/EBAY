import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.regressiontest
def test_text_and_is_displayed():
    service = Service()
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    browser.get("https://www.ebay.com")
    ##Text in the button
    search_button = browser.find_element(By.ID, "gh-btn")
    print(search_button.get_attribute("value"))
    ## Text
    advanced = browser.find_element(By.ID, "gh-as-a")
    print(advanced.text)
    ## Verify that Search button and Advanced are displayed
    assert search_button.is_displayed()
    assert advanced.is_displayed()
