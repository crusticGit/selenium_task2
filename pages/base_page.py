from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait

from ConfigReader import ConfigReader


class BasePage:
    LOAD_PAGE = (By.CLASS_NAME, 'responsive_page')

    def __init__(self, browser):
        self.browser = browser
        self.config = ConfigReader()
        self.timeout = self.config.get_timeout()

    def presence_of_element_located(self, locator, poll_frequency=0.5, timeout=None):
        timeout = timeout or self.timeout
        wait = WebDriverWait(self.browser, timeout, poll_frequency)
        return wait.until(Ec.presence_of_element_located(locator))

    def no_presence_of_element_located(self, locator, poll_frequency=0.5, timeout=None):
        timeout = timeout or self.timeout
        wait = WebDriverWait(self.browser, timeout, poll_frequency)
        return wait.until_not(Ec.presence_of_element_located(locator))

    def presence_of_all_elements_located(self, locator, timeout=None):
        timeout = timeout or self.timeout
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(Ec.presence_of_all_elements_located(locator))

    def visibility_of_element_located(self, locator, timeout=None):
        timeout = timeout or self.timeout
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(Ec.visibility_of_element_located(locator))

    def element_to_be_clickable(self, locator, timeout=None):
        timeout = timeout or self.timeout
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(Ec.element_to_be_clickable(locator))

    def wait_for_open(self):
        self.presence_of_element_located(self.LOAD_PAGE)
