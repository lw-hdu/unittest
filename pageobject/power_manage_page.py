'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2021-12-10 14:33:36
'''
# -*- coding:utf-8 -*-

import time
from selenium.webdriver.common.by import By
import sys
sys.path.append('D:\\liuwen10\\Desktop\\publicdemo\\base')
from base_page import BasePage
sys.path.append('D:\\liuwen10\\Desktop\\publicdemo\\pageobject')
from login_page import LoginPage


class PowerManagePage(BasePage):

    #页面元素
    power_manager_loc = (By.XPATH,'//li[@class="el-menu-item"]')
    select_loc = (By.XPATH,'//input[@placeholder="请输入电站名称"]')
    button_loc = (By.XPATH,'//span[text()=" 查询 "]')

    reset_loc = (By.XPATH,'//span[text()=" 重置 "]')
    status_loc = (By.XPATH,'//input[@placeholder="状态"]')
    alarm_loc = (By.XPATH,'/html/body/div[2]/div/div/ul/li[3]')

    
    #页面动作
    def select_power(self):
        #登录
        lp = LoginPage(self.driver)
        lp.login()
        time.sleep(3)
        #查询
        self.click(PowerManagePage.power_manager_loc)
        time.sleep(1)
        self.send_keys(PowerManagePage.select_loc,"空港")
        time.sleep(1)
        self.click(PowerManagePage.button_loc)
        time.sleep(5)
        self.click(PowerManagePage.reset_loc)
        time.sleep(1)
        self.click(PowerManagePage.status_loc)
        time.sleep(2)
        self.click(PowerManagePage.alarm_loc)
        time.sleep(1)
        self.click(PowerManagePage.button_loc)