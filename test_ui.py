'''
Descripttion: 
Author: Liuwen
Date: 2021-12-07 17:14:57
LastEditTime: 2021-12-10 11:12:19
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestUI(unittest.TestCase):
    # def test_login(self):
    #     global driver
    #     # option = webdriver.ChromeOptions()
    #     # # 防止打印一些无用的日志
    #     # option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    #     # driver = webdriver.Chrome(chrome_options=option)
    #     driver = webdriver.Chrome()
    #     driver.get('http://10.0.10.131/')
    #     driver.find_element(By.XPATH,'//input[@placeholder="请输入用户名"]').send_keys('admin')
    #     driver.find_element(By.XPATH,'//input[@placeholder="请输入密码"]').send_keys('1qaz!QAZ')
    #     driver.find_element(By.XPATH,'//span[text()=" 登  录 "]').click()

        # driver.find_element(By.XPATH,'//span[text()="电站管理"]').click()
    def test_power(self):
        global driver
        option = webdriver.ChromeOptions()
        # # 防止打印一些无用的日志
        option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        driver = webdriver.Chrome(chrome_options=option)
        driver.get('http://10.0.10.131/')
        driver.find_element(By.XPATH,'//input[@placeholder="请输入用户名"]').send_keys('admin')
        driver.find_element(By.XPATH,'//input[@placeholder="请输入密码"]').send_keys('1qaz!QAZ')
        driver.find_element(By.XPATH,'//span[text()=" 登  录 "]').click()
        driver.implicitly_wait(5)
        ##进入电站管理
        driver.find_element(By.XPATH,'//span[text()="电站管理"]').click()
        time.sleep(1)
        # #进入电站列表页
        # driver.find_element(By.XPATH,'//button[@class="el-button el-button--mini"]').click()
        # time.sleep(1)
        # #添加电站
        # driver.find_element(By.XPATH,'//button[@class="el-button el-button--primary el-button--small"]/span[text()=" 添加 "]').click()
        # time.sleep(1)
        # driver.find_element(By.XPATH,'//div[@class="el-input el-input--small"]/input[@placeholder="请输入电站名称"]').send_keys('测试电站1209')
        # #选择电压等级
        # driver.find_element(By.XPATH,'//input[@placeholder="请输入电压等级"]').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH,'//li[@class="el-select-dropdown__item hover"]').click()
        #电站列表页根据电站名称查询
        driver.find_element(By.XPATH,'//input[@placeholder="请输入电站名称"]').send_keys('空港')
        time.sleep(1)
        driver.find_element(By.XPATH,'//span[text()=" 查询 "]').click()
        time.sleep(3)
        # #电站列表页根据电站状态查询
        # time.sleep(2)
        #定位到下拉菜单
        # driver.find_element(By.XPATH,'//input[@placeholder="状态"]').click()
        # time.sleep(3)
        # #对下拉菜单的选项做选择
        # driver.find_element(By.XPATH,'//li[@class="el-select-dropdown__item selected hover"]/span[text()="告警"]').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH,'//span[text()=" 查询 "]').click()
        # #进入设备管理
        # driver.find_element(By.XPATH,'//li[@class="el-menu-item is-active"]').click()
        ##下拉框点击第一个选项
        # sel =select(driver.find_element(By.XPATH,'//input[@placeholder="请输入电站名称"]')).send_keys('空港')
        # sel.select_by_index("2")
        # driver.implicitly_wait(2)
        driver.find_element(By.XPATH,'//li[@class="el-menu-item"]/span[text()="数据大屏"]').click()
        time.sleep(3)
        driver.close()
        
if __name__ == '__main__':
    unittest.main()