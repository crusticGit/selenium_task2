import random

from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.XPATH, '//*[contains(@class, "global_action_link") and @href]')


class MainPageLocators:
    INPUT_SEARCH = (By.XPATH, '//form[@role="search"]//input[@role="combobox"]')
    BUTTON_SEARCH = (By.XPATH, '//form[@role="search"]/button')


class SearchPageLocators:
    INPUT_SEARCHBAR = (By.XPATH, '//*[@id="term"]')
    RESULT_SEARCH = (By.XPATH, '//*[@id="sort_by_dselect_container"]')

    SORT_DROPDOWN = (By.XPATH, '//*[@id = "sort_by_trigger"]')
    SORT_DROPDOWN_LIST = (By.XPATH, '//*[@id = "sort_by_droplist"]')

    SORT_HIGHEST_PRICE = (By.XPATH, '//*[@id = "Price_DESC"]')
    SORT_LOWEST_PRICE = (By.XPATH, '//*[@id = "Price_ASC"]')
    SORT_RELEVANCE = (By.XPATH, '//*[@id = "_ASC"]')
    SORT_RELEASE_DATE = (By.XPATH, '//*[@id = "Released_DESC"]')

    RESULT_CONTAINER = (By.XPATH, '//*[@id = "search_result_container"]')
    LOAD_CONTAINER = (By.XPATH, '//div[@id="search_result_container" and contains(@style, "opacity")]')
    GAME_PRICE = (By.XPATH, '//*[@class="discount_prices"]')


class LoginPageLocators:
    EMAIL_DOMAIN = 'example.com'
    LENGTH_PASS = random.randint(1, 60)

    LOGIN_FORM = (By.XPATH, '//*[@data-featuretarget="login"]//form')
    INPUT_LOGIN = (By.XPATH, '//*[@data-featuretarget="login"]//input[@type="text"]')
    INPUT_PASS = (By.XPATH, '//*[@data-featuretarget="login"]//input[@type="password"]')
    BUTTON_AUTH = (By.XPATH, '//*[@data-featuretarget="login"]//button')
    ERROR_MESSAGE = (By.XPATH, '//*[@data-featuretarget="login"]//button/parent::div/following-sibling::div')
