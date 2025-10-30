from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec

from pages.base_page import BasePage


class MainPage(BasePage):
    LOGIN_LINK = (By.XPATH, '//*[contains(@class, "global_action_link") and @href]')
    INPUT_SEARCH = (By.XPATH, '//form[@role="search"]//input[@role="combobox"]')
    BUTTON_SEARCH = (By.XPATH, '//form[@role="search"]/button')
    UNIQUE_ELEMENT_LOC = (By.XPATH, '//form[@role="search"]/button')

    def search_game(self, game_name):
        inp_search = self._create_wait().until(Ec.presence_of_element_located(self.INPUT_SEARCH))
        inp_search.send_keys(game_name)
        search_btn = self._create_wait().until(Ec.element_to_be_clickable(self.BUTTON_SEARCH))
        search_btn.click()

    def go_to_login_page(self):
        link = self._create_wait().until(Ec.presence_of_element_located(self.LOGIN_LINK))
        link.click()

    def is_login_link_visible(self):
        try:
            self._create_wait().until(Ec.presence_of_element_located(self.LOGIN_LINK))
            return True
        except TimeoutException:
            return False
