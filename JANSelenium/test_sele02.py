import pytest

from selenium import webdriver


@pytest.fixture
def start_browser():
    driver = webdriver.Chrome()
    yield driver  # only runs for the function


def test_open_url_verify(start_browser):
    start_browser.get("https://app.vwo.com")
    print(start_browser.title)
    assert "Login - VWO" == start_browser.title
    assert "Login - VWO-" != start_browser.title
