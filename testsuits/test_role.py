# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2017/12/8

"""
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time,unittest
from utils.TestRunner import TestRunner
from utils.logger import Logger
logger = Logger(logger="BasePage").getlog()
#参数0、1、2分别对应管理员、批发商代理商

class Role(unittest.TestCase):

    def login(self, num):
        self.driver = webdriver.Chrome()
        self.url = 'http://123.206.57.62:17000/index'
        self.driver.get(self.url)
        self.driver.maximize_window()
        user_file = open('../file/login.txt', 'r')
        values = user_file.readlines()
        user_file.close()
        i = []
        for search in values:
            i.append(search)
        type = i[num].split(':')[0]
        keys = i[num].split(':')[1]
        username = keys.split(',')[0]
        password = keys.split(',')[1]
        num = num+1
        s = Select(self.driver.find_element_by_class_name("selectpicker"))
        s.select_by_value(str(num))
        self.driver.find_element_by_name('telphone').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        if type == '管理员':
            logger.info('当前登录用户是管理员')

        elif type=='批发商':
            logger.info('当前登录用户是批发商')
        else:
            logger.info('当前登录用户是代理商')
        logger.info(u"用户名是:%s" %username)
        logger.info(u"密码是:%s" %password)
    def test_a_role(self):
        """权限校验数据"""
        self.login(0)
        lis = self.driver.find_elements_by_class_name('link')

        #点击权限管理
        lis[6].click()
        time.sleep(1)
        self.driver.find_element_by_link_text(u'用户列表').click()
        mainIframe=self.driver.find_elements_by_class_name('iframeBox')
        self.driver.switch_to.frame(mainIframe[-1])
        time.sleep(1)
        ss = self.driver.find_elements_by_css_selector('input.operate')
        ss[1].click()
        self.driver.find_element_by_link_text(u'分配角色').click()
        time.sleep(4)

        """获取当前用户可以分配的角色数据，并查看想要分配的角色是否存在"""
        table = self.driver.find_element_by_id('userRole')
        table_rows = table.find_elements_by_tag_name('tr')
        logger.info(u"总行数:%d", len(table_rows)-1)
        table_cols = table.find_elements_by_tag_name('th')
        logger.info(u"总列数:%d", len(table_cols)-len(table_rows))
        i = 0
        while i < len(table_rows):
            logger.info(u"第%d行的数据是：%s" %(i+1, table_rows[int(i)].text))
            info = table_rows[int(i)].text
            if info.find(u"zhy-超级管理员") != -1:
                logger.info(u'当前分配权限角色存在,在第%d行' %i)
                ids = self.driver.find_elements_by_css_selector('input.ids')
                ids[i].click()
            i = i + 1
        self.driver.find_element_by_css_selector('.layui-layer.layui-layer-page.layer-anim')
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        time.sleep(3)
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        self.driver.quit()

if __name__ == "__main__":
    runner = TestRunner('./', u'集鲜丰后台用例测试', u'测试环境：Chrome')
    runner.run()



