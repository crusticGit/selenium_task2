from selenium import webdriver


class BrowserSingleton:
    _instance = None
    _browser = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(BrowserSingleton, cls).__new__(cls)
        return cls._instance

    def get_browser(self):
        if self._browser is None:
            self._browser = webdriver.Chrome()
        return self._browser

    def quit_browser(self):
        if self._browser:
            self._browser.quit()
            self._browser = None
