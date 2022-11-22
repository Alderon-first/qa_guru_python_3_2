from selene.support.shared import browser
from selene import be, have, command


def test_some(open_browser):
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))

