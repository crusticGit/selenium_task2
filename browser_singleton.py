from selenium import webdriver

class BrowserSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.browser = webdriver.Chrome()
        return cls._instance

    def get_browser(self):
        return self.browser

    def quit_browser(self):
        if self.browser:
            self.browser.quit()
            self.browser = None
        BrowserSingleton._instance = None