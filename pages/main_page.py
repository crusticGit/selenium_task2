from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def search_game(self, game_name):
        self.clear_and_send_keys(MainPageLocators.INPUT_SEARCH, game_name)
        search_btn = self.element_to_be_clickable(MainPageLocators.BUTTON_SEARCH)
        search_btn.click()
