# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2017/12/12
describle:
"""

import unittest
from selenium import webdriver
from case.login import Login
from case.common import Common
from utils.TestRunner import TestRunner
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        前提准备工作
        """
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://123.206.57.62:17000')
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        """
        关闭浏览器
        """
        cls.driver.quit()
    def test_a_add_agent(self):
        """测试后台正常登录"""
        Login(self.driver).login("1", "18888888888", "123456")
        Login(self.driver).get_windows_img()
        # Common(self.driver).find_menu(0, u"商品列表")
        Common(self.driver).find_menu(1, u"代理商列表")
        


if __name__ == "__main__":
    runner = TestRunner('./', u'集鲜丰后台用例测试', u'测试环境：Chrome')
    runner.run()