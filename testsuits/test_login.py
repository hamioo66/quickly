# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2017/12/8

"""
import unittest
from selenium import webdriver
from case.login import Login
from utils.TestRunner import TestRunner
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        前提准备工作
        """
        cls.browse =webdriver.Firefox()
        cls.browse.get('http://123.206.57.62:17000')
        cls.browse.maximize_window()
    @classmethod
    def tearDownClass(cls):
        """
        关闭浏览器
        """
        cls.browse.quit()
    def test_login(self):
        Login(self.browse).login("1", "18888888888", "123456")
        Login(self.browse).get_windows_img()


if __name__ == "__main__":
    runner = TestRunner('./', '百度测试用例', '测试环境：Chrome')
    runner.run()