from common import base


import allure
import pytest


class HomePage(base.Base):
    now_page = 'Home Page - '
    
    # top nav
    popup_hint = '//*[contains(@class,"ReactModal")]'
    search_btn = '//a[@href="/directory"]'
    search_input = '//input[@type="search"]'
    search_related_btn = '//ul/li[1]'

    # bottom nav

    @allure.step(f'{now_page}skipped open by app hint')
    def skip_open_app_hint(self):
        self.find_element(self.popup_hint).click()

    @allure.step(f'{now_page}click search button')
    def click_search_btn(self):
        self.find_element(self.search_btn).click()

    @allure.step(f'{now_page}input search keyword')
    def input_search_keyword(self, keyword):
        self.find_element(self.search_input).send_keys(keyword)
        self.find_element(self.search_related_btn).click()