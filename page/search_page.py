from common import base
from testcase.conftest import driver

import time
import allure
import pytest


class SearchPage(base.Base):
    now_page = 'Search Page - '
    
    streamer_name = '//h2/following-sibling::div/p'

    body = '//body'
    avoid_click_btn = '//h2[contains(text(),"分類")]'

    @allure.step(f'{now_page}scroll down 2 times')
    def scroll_down_2times(self):
        self.find_element(self.avoid_click_btn).click()

        for _ in range(2):
            self.find_element(self.body).send_keys(base.Keys.PAGE_DOWN)
            time.sleep(1.5)

    @allure.step(f'{now_page}click streamer name to go to streamer page')
    def click_streamer_name_to_goto_streamer_page(self,):
        self.find_element(self.streamer_name).click()
