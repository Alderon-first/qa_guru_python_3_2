from selene.support.shared import browser
from selene import be, have, command


def test_some(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_crush(open_browser):
    browser.element('[name="q"]').should(be.blank).type('ctkty').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


