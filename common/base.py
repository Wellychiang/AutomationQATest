from zipfile import Path

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

import allure
import time
import logging
import os

log_path = 'log/log.log'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')

console_log = logging.StreamHandler()  # sys.stdout
logger.addHandler(console_log)

file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

log = lambda x: logger.info(str(x).encode('utf-8', 'replace').decode('cp950', 'ignore'))


class Base:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, args):
        try:
            element = WebDriverWait(self.driver, 13).until(
                EC.presence_of_element_located((By.XPATH, args))
            )
            return element
        except:
            self.get_screen_shot()
            log(f'Can not find {args} element')
            return element

    def scroll_down(self, times=1):
        for _ in range(times):
            # 以視窗左上角 (0,0) 為起點，往下滾動 600 像素
            scroll_origin = ScrollOrigin.from_viewport(0, 0)
            ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 600).perform()
            time.sleep(1.5)  # 每次滾動完等一下，讓動態內容載入


    def get_screen_shot(self):
        time_ = time.strftime('%Y-%m-%d %H:%M:%S')
        time_string = self.strip_dot(time_)

        time_string = time_string[:-2]
        file_name = f'screenshot/{time_string}.png'
        self.driver.get_screenshot_as_file(filename=file_name)

        allure.attach.file(
            source= f'screenshot/{time_string}.png',
            name=time_string,
            attachment_type=AttachmentType.PNG
        )

    def strip_dot(self, items) -> str:
        string = ''
        for item in items:
            if item in (',', ':'):
                continue
            elif item == '.':
                break
            else:
                string += item
        return string

