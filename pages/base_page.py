from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait

from ConfigReader import ConfigReader


class BasePage:
    UNIQUE_ELEMENT_LOC = None  # should be overriden

    def __init__(self, browser):
        self.browser = browser
        self.config = ConfigReader()
        self.timeout = self.config.get_timeout()

    def wait(self, poll_frequency=0.5, timeout=None):
        timeout = timeout or self.timeout
        wait = WebDriverWait(self.browser, timeout, poll_frequency)
        return wait

    def wait_for_open(self):
        self.wait().until(Ec.presence_of_element_located(self.UNIQUE_ELEMENT_LOC))
