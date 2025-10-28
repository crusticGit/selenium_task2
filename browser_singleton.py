from selenium import webdriver


class BrowserSingleton:
    _browser = None

    @staticmethod
    def get_browser():
        if BrowserSingleton._browser is None:
            BrowserSingleton._browser = webdriver.Chrome()
        return BrowserSingleton._browser

    @staticmethod
    def quit_browser():
        if BrowserSingleton._browser:
            BrowserSingleton._browser.quit()
            BrowserSingleton._browser = None
