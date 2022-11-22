import pytest


@pytest.fixture(scope="session")
def open_browser():
    b = "browser"
    print("Браузер открыт")
    yield b # код ниже выполнится после завершения теста
    b = "браузер закрыт"
    print("Браузер открыт")


@pytest.fixture(open_browser)
#фуказываю тут предыдущую икстуру, чтобы определть порядок их запуска
def create_user():
    return "35"


def test_some(open_browser, create_user):
    assert open_browser == "browser"
    assert open_browser == "35"