# -*- coding=UTF-8 -*-
import unittest
from selenium import webdriver
from case.login import Login
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        前提准备工作
        """
        cls.browse =webdriver.Firefox()
        cls.browse.get('http://123.206.57.62:17000')
    @classmethod
    def tearDownClass(cls):
        """
        关闭浏览器
        """
        cls.browse.quit()
    def test_login(self):
        Login(self.browse).login("1", "18888888888", "123456")
        Login(self.browse).get_windows_img()
