'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2021-12-10 14:23:44
'''
import pytest
# from ddt import ddt, data, unpack
from selenium import webdriver

from base.base_util import BaseUtil
# from common.excel_util import ExcelUtil
from pageobject.login_page import LoginPage
#@ddt
class TestLogin(BaseUtil):

    # @data(*ExcelUtil().read_excel())
    # @unpack
    # @pytest.mark.parametrize("index,username,password",ExcelUtil().read_excel())
    def test_login(self):
        """ 登录 """
        lp = LoginPage(self.driver)
        lp.login()
        # if index==1:
        #     # 断言
        #     #self.assertEqual(lp.get_except_result(),'退出')
        #     assert lp.get_except_result() == '退出'