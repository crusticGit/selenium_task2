from pages.base_page import BasePage
from pages.locators import SearchPageLocators


class SearchPage(BasePage):
    def should_be_search_page(self):
        self.should_be_search_bar()
        self.should_be_result_search()
        self.should_be_search_url()

    def should_be_search_url(self):
        assert 'search' in self.browser.current_url, \
            'Url not contain a search'

    def should_be_search_bar(self):
        assert self.visibility_of_element_located(SearchPageLocators.INPUT_SEARCHBAR), \
            'Search bar is not visibility'

    def should_be_result_search(self):
        assert self.visibility_of_element_located(SearchPageLocators.RESULT_SEARCH), \
            'Result search is not visibility'

    def sort_by_price_desc(self):
        dropdown = self.element_to_be_clickable(SearchPageLocators.SORT_DROPDOWN)
        dropdown.click()
        self.visibility_of_element_located(SearchPageLocators.SORT_DROPDOWN_LIST)
        self.element_to_be_clickable(SearchPageLocators.SORT_HIGHEST_PRICE).click()
        self.presence_of_element_located(SearchPageLocators.LOAD_CONTAINER, poll_frequency=0.1)
        self.no_presence_of_element_located(SearchPageLocators.LOAD_CONTAINER, poll_frequency=0.1)

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
        games_list = self.presence_of_all_elements_located(SearchPageLocators.GAME_PRICE)[:count]
        games_price = [self._parse_price(game.text) for game in games_list]
        print(games_price)
        return games_price
