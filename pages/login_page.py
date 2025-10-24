from faker import Faker

from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
            'Url not contain a login'

    def should_be_login_form(self):
        assert self.visibility_of_element_located(LoginPageLocators.LOGIN_FORM), \
            'Login form is not visibility'

    def enter_credentials(self, email, password):
        self.clear_and_send_keys(LoginPageLocators.INPUT_LOGIN, email)
        self.clear_and_send_keys(LoginPageLocators.INPUT_PASS, password)

    def get_error_message(self):
        return self.get_element_text(LoginPageLocators.ERROR_MESSAGE)

    def attempt_login_with_invalid_credentials(self):
        faker = Faker()
        email = faker.email(domain=LoginPageLocators.EMAIL_DOMAIN)
        password = faker.password(length=LoginPageLocators.LENGTH_PASS, special_chars=True, digits=True)
        self.enter_credentials(email, password)
        self.element_to_be_clickable(LoginPageLocators.BUTTON_AUTH).click()
        self.element_attribute_to_include(LoginPageLocators.BUTTON_AUTH, "disabled")
        self.element_attribute_to_not_include(LoginPageLocators.BUTTON_AUTH, "disabled")
        return self.get_error_message()

    def attempt_login_with_valid_credentials(self):
        pass
