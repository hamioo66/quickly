# coding:utf-8
import unittest
from selenium import webdriver
class Test_002(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "start"

    @classmethod
    def tearDownClass(cls):
        print "end"
    def test_open(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://www.baidu.com")
if __name__=="__main__":
    unittest.main()