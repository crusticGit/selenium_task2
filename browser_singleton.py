from selenium import webdriver


class BrowserSingleton:
    _browser = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._browser = webdriver.Chrome()
        return cls._instance

    @staticmethod
    def get_browser():
        return BrowserSingleton._browser

    @staticmethod
    def quit_browser():
        if BrowserSingleton._browser:
            BrowserSingleton._browser.quit()
            BrowserSingleton._browser = None
            BrowserSingleton._instance = None
