import pytest
from selene.support.shared import browser
from selene import be, have, command

url ='https://www.google.com'

@pytest.fixture()
def open_browser():
    #print('подготовка к прогону')
    browser.open(url)
    browser.driver.set_window_size(width=1920, height=1080)
    yield
    browser.element('[name="q"]').clear()




