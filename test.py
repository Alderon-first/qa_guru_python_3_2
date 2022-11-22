import selene


def test_some(open_browser):
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))

