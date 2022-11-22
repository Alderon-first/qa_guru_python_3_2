import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def open_browser():
    browser.open('https://www.google.com')
    browser.element('[name="q"]').clear()
