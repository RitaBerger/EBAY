import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.mark.regressiontest
def test_assert():
    service = Service()
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    browser.get("https://www.google.com")
    assert "https://www.google.com" == browser.current_url
    assert "Google" == browser.title
