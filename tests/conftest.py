import pytest

from browser_singleton import BrowserSingleton


@pytest.fixture(scope='function')
def browser():
    browser_s = BrowserSingleton()
    browser = browser_s.get_browser()
    print("\nstart browser for test..")
    yield browser
    print('\n quit browser..')
    browser_s.quit_browser()
