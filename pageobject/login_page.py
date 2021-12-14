'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2021-12-10 16:04:19
'''
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
# import sys
# sys.path.append('D:\\liuwen10\\Desktop\\publicdemo\\base')
from base.base_page import BasePage


class LoginPage(BasePage):

    #页面的元素
    username_loc = (By.XPATH,'//input[@placeholder="请输入用户名"]')
    password_loc = (By.XPATH,'//input[@placeholder="请输入密码"]')
    submit_loc = ((By.XPATH,'//span[text()=" 登  录 "]'))
    # tuichu_loc = (By.LINK_TEXT,'退出')

    #页面的动作
    def login(self,username="admin",password="1qaz!QAZ"):
        self.send_keys(LoginPage.username_loc,username)
        self.send_keys(LoginPage.password_loc,password)
        self.click(LoginPage.submit_loc)

    #断言
    # def get_except_result(self):
    #     self.goto_frame("header-frame")
    #     return self.get_value(LoginPage.tuichu_loc)