# -*- coding=UTF-8 -*-
import unittest
from utils.TestRunner import TestRunner
suite = unittest.TestLoader().discover("testsuits")
if __name__=='__main__':
    #执行用例
    runner=unittest.TextTestRunner()
    runner.run(suite)
    testRunner = TestRunner('./', '百度测试用例', '测试环境：Chrome')
    testRunner.run()
