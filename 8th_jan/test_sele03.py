import selenium

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sele():
    driver =webdriver.Chrome()
    driver.get("https://www.ebay.com")

    #assert.driver.current_url == "https://www.ebay.com/"
    