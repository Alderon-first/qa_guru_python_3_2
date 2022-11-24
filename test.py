from selene.support.shared import browser
from selene import be, have, command


def test_some(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_negativ(open_browser):
    browser.element('[name="q"]').should(be.blank).type('билибердабилибердабилибердабилибердабилибердабилиберда')\
        .press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу '
                                                               'билибердабилибердабилибердабилибердабилибердабилиберда '
                                                               'ничего не найдено.'))


