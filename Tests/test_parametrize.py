import pytest
from selenium import Keys
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("item",
                         [
                              "Books",
                              "Dresses",
                              "Toys",
                              "Sandals"
                         ])
def test_simple_search(browser,item):
    browser.get("https://www.ebay.com")
    browser.find_element(By.ID, 'gh-ac').send_keys(item + Keys.ENTER)
