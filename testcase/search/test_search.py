from page.search_page import SearchPage
from page.home_page import HomePage
from page.streamer_page import StreamerPage

import pytest
import allure
import time


@allure.feature('Search')
@allure.story('Search and go to streamer page')
@allure.severity('blocker')
def test_search(driver):
    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    streamer_page = StreamerPage(driver)

    game_name = 'StarCraft II'
    swipe_times = 2

    home_page.click_search_btn()
    home_page.input_search_keyword(game_name)

    for _ in range(swipe_times):
        search_page.scroll_down_2times()

    search_page.click_streamer_name_to_goto_streamer_page()
    streamer_page.wait_for_page_load_and_take_screenshot()

