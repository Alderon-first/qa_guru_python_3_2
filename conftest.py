import pytest

from selene.support.shared import browser


@pytest.fixture(scope="session")
def open_browser():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.window_height = 1300