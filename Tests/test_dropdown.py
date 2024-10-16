import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.regressiontest
def test_dropdown():
    service = Service()
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    browser.get("https://www.ebay.com")
    categories_dropdown = Select(browser.find_element(By.ID, "gh-cat"))
    categories_dropdown.select_by_visible_text("Art")
    categories_dropdown.select_by_index("1")
    categories_dropdown.select_by_value("281")



