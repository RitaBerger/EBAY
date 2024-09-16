import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.regressiontest
def test_implicit_wait():
    service = Service()
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get("https://www.ebay.com")
    browser.find_element(By.LINK_TEXT, "Motors").click()
    browser.find_element(By.LINK_TEXT, "Find parts that fit your vehicle").click()
    assert 'https://www.ebay.com/g/mygarage' == browser.current_url
    assert 'My Garage | eBay' == browser.title
    browser.find_element(By.CSS_SELECTOR, "[src='https\:\/\/secureir\.ebaystatic\.com\/cr\/v\/c1\/gh_show_ads\.js']")
