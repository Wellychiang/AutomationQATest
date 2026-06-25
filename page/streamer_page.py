from common import base
from testcase.conftest import driver

import allure
import pytest


class StreamerPage(base.Base):
    now_page = 'Streamer Page - '
    
    video_player = '//*[@data-a-target="video-ref"]'
    streamer_pic = '//a[contains(@href, "home") and contains(@class, "link")]'
    streamer_content = '//a[contains(@href, "videos") and contains(@class, "link")]'


    @allure.step(f'{now_page}wait for page load then take screenshot')
    def wait_for_page_load_and_take_screenshot(self):
        self.find_element(self.video_player)
        self.find_element(self.streamer_pic)
        self.find_element(self.streamer_content)
        self.get_screen_shot()