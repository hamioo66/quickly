# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2017/12/8

"""
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from utils.logger import Logger
logger = Logger(logger="BasePage").getlog()
#参数0、1、2分别对应管理员、批发商代理商
driver = webdriver.Chrome()
url = 'http://123.206.57.62:17000/index'
driver.get(url)
driver.maximize_window()
def login(num):
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
    s = Select(driver.find_element_by_class_name("selectpicker"))
    s.select_by_value(str(num))
    driver.find_element_by_name('telphone').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    if type == '管理员':
        logger.info('当前登录用户是管理员')

    elif type=='批发商':
        logger.info('当前登录用户是批发商')
    else:
        logger.info('当前登录用户是代理商')
    logger.info(u"用户名是:%s" %username)
    logger.info(u"密码是:%s" %password)
login(0)
lis=driver.find_elements_by_class_name('link')

#点击权限管理
lis[6].click()
time.sleep(1)
driver.find_element_by_link_text(u'用户列表').click()
mainIframe=driver.find_elements_by_class_name('iframeBox')
driver.switch_to.frame(mainIframe[-1])
time.sleep(1)
ss = driver.find_elements_by_css_selector('input.operate')
ss[1].click()
driver.find_element_by_link_text(u'分配角色').click()
time.sleep(4)

"""获取当前用户可以分配的角色数据，并查看想要分配的角色是否存在"""
table = driver.find_element_by_id('userRole')
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
        ids = driver.find_elements_by_css_selector('input.ids')
        ids[i].click()
    i = i + 1
driver.find_element_by_css_selector('.layui-layer.layui-layer-page.layer-anim')
driver.find_element_by_class_name('layui-layer-btn0').click()
time.sleep(3)
driver.find_element_by_class_name('layui-layer-btn0').click()
driver.quit()





