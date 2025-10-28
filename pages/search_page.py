from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    INPUT_SEARCHBAR = (By.ID, 'term')
    RESULT_SEARCH = (By.ID, 'sort_by_dselect_container')
    SORT_DROPDOWN = (By.ID, 'sort_by_trigger')
    SORT_DROPDOWN_LIST = (By.ID, 'sort_by_droplist')
    SORT_HIGHEST_PRICE = (By.ID, 'Price_DESC')
    LOAD_CONTAINER = (By.XPATH, '//div[@id="search_result_container" and contains(@style, "opacity")]')
    GAME_PRICE = (By.XPATH, '//*[@class="discount_prices"]')

    def sort_by_price_desc(self):
        dropdown = self.element_to_be_clickable(self.SORT_DROPDOWN)
        dropdown.click()
        self.visibility_of_element_located(self.SORT_DROPDOWN_LIST)
        self.element_to_be_clickable(self.SORT_HIGHEST_PRICE).click()
        self.presence_of_element_located(self.LOAD_CONTAINER, poll_frequency=0.1)
        self.no_presence_of_element_located(self.LOAD_CONTAINER, poll_frequency=0.1)

    @staticmethod
    def _parse_price(price_text):
        import re
        matches = re.findall(r'\d+,\d+|\d+', price_text)
        if matches:
            last_match = matches[-1]
            clean_price = last_match.replace(',', '.')

            try:
                return float(clean_price)
            except ValueError:
                return 0.0

        return 0.0

    def get_games_list(self, count):
        games_list = self.presence_of_all_elements_located(self.GAME_PRICE)[:count]
        games_price = [self._parse_price(game.text) for game in games_list]
        print(games_price)
        return games_price
