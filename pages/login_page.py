from faker import Faker
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_FORM = (By.XPATH, '//*[@data-featuretarget="login"]//form')
    INPUT_LOGIN = (By.XPATH, '//*[@data-featuretarget="login"]//input[@type="text"]')
    INPUT_PASS = (By.XPATH, '//*[@data-featuretarget="login"]//input[@type="password"]')
    BUTTON_AUTH = (By.XPATH, '//*[@data-featuretarget="login"]//button[not(@disabled)]')
    DISABLED_BUTTON_AUTH = (By.XPATH, '//*[@data-featuretarget="login"]//button[@disabled]')
    ERROR_MESSAGE = (By.XPATH, '//*[@data-featuretarget="login"]//button/parent::div/following-sibling::div')

    def enter_credentials(self, email, password):
        self.presence_of_element_located(self.INPUT_LOGIN).send_keys(email)
        self.presence_of_element_located(self.INPUT_PASS).send_keys(password)

    def attempt_login_with_invalid_credentials(self, email_domain, length_pass):
        faker = Faker()
        email = faker.email(domain=email_domain)
        password = faker.password(length=length_pass, special_chars=True, digits=True)

        self.enter_credentials(email, password)
        self.element_to_be_clickable(self.BUTTON_AUTH).click()
        self.presence_of_element_located(self.DISABLED_BUTTON_AUTH)
        self.presence_of_element_located(self.BUTTON_AUTH)
        return self.presence_of_element_located(self.ERROR_MESSAGE).text

    def attempt_login_with_valid_credentials(self):
        pass
