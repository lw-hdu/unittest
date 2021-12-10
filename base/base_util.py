'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:32
LastEditTime: 2021-12-09 15:59:25
'''
# -*- coding:utf-8 -*-

import time

from selenium import webdriver

class BaseUtil:

    def setup(self) -> None:
        global driver
        # 打开浏览器
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.driver = webdriver.Chrome(chrome_options=self.option)
        # driver = self.driver
        # 加载网页
        self.driver.get("http://10.0.10.131/")

    def teardown(self) -> None:
        time.sleep(3)
        self.driver.quit()