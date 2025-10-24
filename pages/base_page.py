from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def presence_of_element_located(self, locator, poll_frequency=0.5, timeout=10):
        wait = WebDriverWait(self.browser, timeout, poll_frequency)
        return wait.until(Ec.presence_of_element_located(locator))

    def no_presence_of_element_located(self, locator, poll_frequency=0.5, timeout=10):
        wait = WebDriverWait(self.browser, timeout, poll_frequency)
        return wait.until_not(Ec.presence_of_element_located(locator))

    def presence_of_all_elements_located(self, locator, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(Ec.presence_of_all_elements_located(locator))

    def visibility_of_element_located(self, locator, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(Ec.visibility_of_element_located(locator))

    def element_to_be_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(Ec.element_to_be_clickable(locator))

    def element_attribute_to_include(self, locator, attribute, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(Ec.element_attribute_to_include(locator, attribute))

    def element_attribute_to_not_include(self, locator, attribute, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until_not(Ec.element_attribute_to_include(locator, attribute))

    def clear_and_send_keys(self, locator, text, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        element = wait.until(Ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        element = wait.until(Ec.visibility_of_element_located(locator))
        return element.text

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.visibility_of_element_located(BasePageLocators.LOGIN_LINK), "Login link is not visibility"

    def go_to_login_page(self):
        link = self.visibility_of_element_located(BasePageLocators.LOGIN_LINK)
        link.click()
