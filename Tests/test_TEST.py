import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.regressiontest
def test_TEST():
    service = Service()
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    browser.get("https://www.ebay.com")
    WebDriverWait(browser, 15).until(EC.title_is("Electronics, Cars, Fashion, Collectibles & More | eBay"))
    browser.find_element(By.LINK_TEXT, "Motors").click()
    makes_dropdown = Select(WebDriverWait(browser,15).until(EC.element_to_be_clickable(browser.find_element(By.NAME, "Make"))))
    makes_dropdown.select_by_visible_text("BMW")