'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2021-12-09 16:02:05
'''
# -*- coding:utf-8 -*-

import sys
sys.path.append('D:\\liuwen10\\Desktop\\publicdemo\\base')
from base_util import BaseUtil
sys.path.append('D:\\liuwen10\\Desktop\\publicdemo\\pageobject')
from power_manage_page import PowerManagePage

class TestPowerManage(BaseUtil):

    def test_select_power(self):

        pm = PowerManagePage(self.driver)
        pm.select_power()



