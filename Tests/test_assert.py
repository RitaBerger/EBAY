import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.mark.regressiontest
def test_assert():
    service = Service()
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    browser.get("https://www.ebay.com")
    assert "https://www.ebay.com/" == browser.current_url
    assert "Electronics, Cars, Fashion, Collectibles & More | eBay" == browser.title