# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2017/12/8

"""
import unittest
from utils.TestRunner import TestRunner
# suite = unittest.TestLoader().discover("testsuits")
if __name__=='__main__':
    # 执行用例并生成报告
    # runner=unittest.TextTestRunner()
    # runner.run(suite)
    testRunner = TestRunner('./', u'百度测试用例', u'测试环境：Chrome')
    testRunner.run()
