# -*- coding=UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time,os
from selenium.webdriver.common.keys import Keys
from utils.logger import Logger
logger = Logger(logger="BasePage").getlog()

user_file = open('../file/login.txt', 'r')
values = user_file.readlines()
user_file.close()
i=[]
for search in values:
    i.append(search)
driver=webdriver.Chrome()
url='http://123.206.57.62:17000/index'
driver.get(url)
driver.maximize_window()
#参数0、1、2分别对应管理员、批发商代理商
def login(num):
    type=i[num].split(':')[0]
    keys=i[num].split(':')[1]
    username = keys.split(',')[0]
    password = keys.split(',')[1]
    num=num+1
    s=Select(driver.find_element_by_class_name("selectpicker"))
    s.select_by_value(str(num))
    driver.find_element_by_name('telphone').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    # driver.find_element_by_name('loginBtn').click()
    if type=='管理员':
        logger.info('当前登录用户是管理员')
        # lis[0].click()
        # driver.find_element_by_link_text('商品列表').click()
    elif type=='批发商':
        logger.info('当前登录用户是批发商')
    else:
        logger.info('当前登录用户是代理商')
    logger.info(u"用户名是:%s" %username)
    logger.info(u"密码是:%s" %password)
login(0)
lis=driver.find_elements_by_class_name('link')
#点击用户管理
lis[1].click()
time.sleep(1)
driver.find_element_by_link_text(u'代理商列表').click()
mainIframe=driver.find_elements_by_class_name('iframeBox')
driver.switch_to.frame(mainIframe[-1])
time.sleep(1)
driver.find_element_by_css_selector('button.columnBtn.js_add_agent').click()

mainIframe1=driver.find_elements_by_tag_name('iframe')
print mainIframe1
driver.switch_to.frame(mainIframe1[-1])
driver.find_element_by_css_selector('input[placeholder="请输入企业名称"]').send_keys('123456')
driver.find_element_by_css_selector('input[placeholder="有效的手机号码"]').send_keys('15599155289')

driver.find_element_by_id('file').send_keys('C:\\Users\\lenovo\\Pictures\\aa.jpg')
time.sleep(5)
# driver.find_element_by_xpath('//*[@id="agent_area_div"]/div[1]').click() #点击选择代理区域
driver.find_element_by_id('file2').send_keys('C:\\Users\\lenovo\\Pictures\\aa.jpg')
# driver.find_element_by_css_selector('input#file2.fileImg').click()
# #调用upfile.exe上传程序
# os.system("F:\\upfile.exe")
driver.find_element_by_id('file2').send_keys('C:\\Users\\lenovo\\Pictures\\bb.jpg')




def selectNum(self,num):
    self.num=num
    selects = driver.find_elements_by_css_selector('button[title="请选择"]')
    print len(selects)
    selects[num - 1].click()


    if num==1:
        selectArea()

    elif num==3:
        selectContactAddress()

area=[]
def selectArea(self,area):     #代理区域
    formSearchs = driver.find_elements_by_class_name('form-control')
    for i in area:
        pass


def selectContactAddress(self,province,city,area,country):   #联系地址
    self.province = province
    self.city = city
    self.area=area
    self.country=country
    formSearchs = driver.find_elements_by_class_name('form-control')
    formSearchs[self.num - 1].send_keys(self.province)
    formSearchs[self.num - 1].send_keys(Keys.ENTER)
    formSearchs[self.num].send_keys(self.city)
    formSearchs[self.num - 1].send_keys(Keys.ENTER)
    pass

selectNum(1)
