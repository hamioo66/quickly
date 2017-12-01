# -*- coding:UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
def login(self,driver,Select,logFile,num):
    i=[]
    type = i[num].split(':')[0]
    keys = i[num].split(':')[1]
    # logFile.info("",num,type,keys)
    username = keys.split(',')[0]
    password = keys.split(',')[1]
    num = num + 1
    s = Select(driver.find_element_by_class_name("selectpicker"))
    s.select_by_value(str(num))
    driver.find_element_by_name('telphone').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    # driver.find_element_by_name('loginBtn').click()

    if type == '管理员':
        logFile.info('当前登录用户是管理员')
        # lis[0].click()
        # driver.find_element_by_link_text('商品列表').click()
    elif type == '批发商':
        logFile.info('当前登录用户是批发商')

    else:
        logFile.info('当前登录用户是代理商')
    logFile.info(u"用户名是:%s" % username)
    logFile.info(u"密码是:%s" % password)
# 退出登录方法
def logout(self,driver):
    moveto=driver.find_element_by_class_name('userListBox')
    driver.move_to_element(moveto)


