'''
Descripttion: 
Author: Liuwen
Date: 2021-12-10 10:45:15
LastEditTime: 2021-12-10 10:58:46
'''
from selenium import webdriver

from base.base_util import BaseUtil
from pageobject.big_screen_page import BigScreenPage


class TestBigScreen(BaseUtil):
    def test_bigscreen(self):
        bs = BigScreenPage(self.driver)
        bs.big_screen()
        
