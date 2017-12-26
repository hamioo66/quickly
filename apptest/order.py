# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2017/12/20
describle:批发商接单
设备号：华为机：PBV7N16C20000414    oppo：8ac7d424
"""
import appdef, unittest, random, time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from utils.TestRunner import TestRunner
from utils.logger import Logger
logger = Logger(logger="BasePage").getlog()

class Test_Order(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = appdef.driver
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #app端注册商户
    def test_a_register(self):
        i = random.randint(1, 1000)
        if i < 10:
            self.randomCellphone = '1873640000' + str(i)
        elif i > 10 and i < 100:
            self.randomCellphone = '187364000' + str(i)
        elif i > 100 and i <1000:
            self.randomCellphone = '18736400' + str(i)
        print self.randomCellphone
        # self.driver.implicitly_wait(5)
        self.driver.find_element_by_name(u'我的').click()
        self.driver.find_element_by_id('tv_rg').click()
        self.driver.find_element_by_id('merchantNameET').send_keys(self.randomCellphone)
        self.driver.find_element_by_id('passwordET').send_keys('123456')
        self.driver.find_element_by_id('codeET').send_keys('213213')
        self.driver.find_element_by_id('registerBT').click()
        if self.driver.find_element_by_name('完善信息') and self.driver.find_element_by_id('phoneET').text == self.randomCellphone:
            self.assertTrue(u"商户注册成功")
            print "商户注册成功"
        else:
            self.assertFalse(u"商户注册异常")
            print "商户注册异常"
        self.driver.find_element_by_id('loginTV').click()


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

    # 后台校验数据
    def test_b_system_date(self):
        self.login(0)
        lis = self.driver.find_elements_by_class_name('link')
        # 点击权限管理
        lis[2].click()
        time.sleep(1)
        self.driver.find_element_by_link_text(u'商户列表').click()
        mainIframe = self.driver.find_elements_by_class_name('iframeBox')
        self.driver.switch_to.frame(mainIframe[-1])
        time.sleep(1)





    # """商户我的--交易记录数据校验"""
    # def test_data(self):
    #     self.driver.find_element_by_name(u'我的').click()
    #     self.driver.find_element_by_id('edit_account').send_keys('17300200006')
    #     self.driver.find_element_by_id('edit_pz').send_keys('123456')
    #     a = self.driver.find_element_by_id("tv_yzm").text
    #     b = str(a)
    #     yzm = b.split()
    #     self.driver.find_element_by_id("edit_yzm").send_keys(yzm)
    #     self.driver.find_element_by_id('tv_login').click()
    #     self.driver.find_element_by_name(u'我的').click()
    #     self.driver.find_element_by_id('merchant_lookall').click()
    #     time.sleep(5)
    #     data = self.driver.find_elements_by_class_name('android.widget.TextView')
    #     supplier = self.driver.find_elements_by_id('supplierNameTV')
    #     # print supplier[1].text
    #     print data, len(data)
    #     j = 0
    #     datas = []
    #     while j < len(data):
    #         print data[j].text
    #         datas.append(data[j].text)
    #         j = j + 1
    #     for i in datas:
    #         print i
    #









    # def test_b_acceptOrder(self):
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element_by_name(u'我的').click()
    #     orders = self.driver.find_elements_by_id('whlosalersp_awaiting_receivingLL').click()
    #     orders[5].click()




if __name__ == '__main__':
    runner = TestRunner('./', u'集鲜丰app订单用例测试', u'测试环境：app')
    runner.run()


