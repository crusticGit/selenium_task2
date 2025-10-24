import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_page import SearchPage


class TestLoginFromMainPage:
    def test_guest_should_see_login_link_on_main_page(self, browser):
        link = 'https://store.steampowered.com/'
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_main_page(self, browser):
        link = "https://store.steampowered.com/"
        main_page = MainPage(browser, link)
        main_page.open()

        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_invalid_login_shows_error_message(self, browser):
        link = "https://store.steampowered.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        expected_error = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
        actual_error = login_page.attempt_login_with_invalid_credentials()
        assert actual_error == expected_error, f'Ожидаемый результат:{expected_error}, фактический: {actual_error}'

    @pytest.mark.parametrize("game_name, games_count", [('The Witcher', 10), ('Fallout', 20)])
    def test_search_game_from_main_page(self, browser, game_name, games_count):
        link = "https://store.steampowered.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.search_game(game_name)

        search_page = SearchPage(browser, browser.current_url)
        search_page.should_be_search_page()
        search_page.sort_by_price_desc()

        actual_games_price = search_page.get_games_list(games_count)
        expected_games_price = sorted(actual_games_price, reverse=True)
        assert actual_games_price == expected_games_price, 'List is not sorted correctly'
