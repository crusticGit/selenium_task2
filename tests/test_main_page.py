import pytest
from faker import Faker

from ConfigReader import ConfigReader
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_page import SearchPage


class TestLoginFromMainPage:
    def test_guest_should_see_login_link_on_main_page(self, browser):
        link = ConfigReader().get_url('base_url')

        main_page = MainPage(browser)
        browser.get(link)
        main_page.wait_for_open()
        assert main_page.is_login_link_visible(), \
            "Login link is not visibility"

    def test_guest_can_go_to_login_page_from_main_page(self, browser):
        link = ConfigReader().get_url('base_url')

        main_page = MainPage(browser)
        browser.get(link)
        main_page.wait_for_open()
        main_page.go_to_login_page()

        login_page = LoginPage(browser)
        login_page.wait_for_open()

    @pytest.mark.parametrize("email_domain, length_pass", [
        ("example.com", 10),
        ("mail.ru", 5),
        ("google.com", 40)
    ])
    def test_invalid_login_shows_error_message(self, browser, email_domain, length_pass):
        link = ConfigReader().get_url('base_url')

        main_page = MainPage(browser)
        browser.get(link)
        main_page.wait_for_open()
        main_page.go_to_login_page()

        login_page = LoginPage(browser)
        login_page.wait_for_open()

        faker = Faker()
        email = faker.email(domain=email_domain)
        password = faker.password(length=length_pass, special_chars=True, digits=True)

        actual_error = login_page.attempt_login_with_invalid_credentials(email, password)
        expected_error = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
        assert actual_error == expected_error, f'Actual result:{actual_error}, expected: {expected_error}'

    @pytest.mark.parametrize("game_name, games_count", [('The Witcher', 10), ('Fallout', 20)])
    def test_search_game_from_main_page(self, browser, game_name, games_count):
        link = ConfigReader().get_url('base_url')

        main_page = MainPage(browser)
        browser.get(link)
        main_page.wait_for_open()
        main_page.search_game(game_name)

        search_page = SearchPage(browser)
        search_page.wait_for_open()

        search_page.sort_by_price_desc()

        actual_games_price = search_page.get_games_list(games_count)
        expected_games_price = sorted(actual_games_price, reverse=True)
        assert actual_games_price == expected_games_price, (f'List is not sorted correctly.'
                                                            f' Actual result {actual_games_price}, expected: {expected_games_price}')
