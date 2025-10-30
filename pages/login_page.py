from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec

from pages.base_page import BasePage


class LoginPage(BasePage):
    INPUT_LOGIN = (By.XPATH, '//*[@data-featuretarget="login"]//input[@type="text"]')
    INPUT_PASS = (By.XPATH, '//*[@data-featuretarget="login"]//input[@type="password"]')

    BUTTON_AUTH = (By.XPATH, '//*[@data-featuretarget="login"]//button[not(@disabled)]')
    DISABLED_BUTTON_AUTH = (By.XPATH, '//*[@data-featuretarget="login"]//button[@disabled]')
    ERROR_MESSAGE = (By.XPATH, '//*[@data-featuretarget="login"]//button/parent::div/following-sibling::div')

    UNIQUE_ELEMENT_LOC = (By.XPATH, '//*[@data-featuretarget="login"]//form')

    def enter_credentials(self, email, password):
        self._create_wait().until(Ec.presence_of_element_located(self.INPUT_LOGIN)).send_keys(email)
        self._create_wait().until(Ec.presence_of_element_located(self.INPUT_PASS)).send_keys(password)

    def attempt_login_with_invalid_credentials(self, email, password):
        self.enter_credentials(email, password)
        self._create_wait().until(Ec.element_to_be_clickable(self.BUTTON_AUTH)).click()
        self._create_wait().until(Ec.presence_of_element_located(self.DISABLED_BUTTON_AUTH))
        self._create_wait().until(Ec.presence_of_element_located(self.BUTTON_AUTH))
        return self._create_wait().until(Ec.presence_of_element_located(self.ERROR_MESSAGE)).text
