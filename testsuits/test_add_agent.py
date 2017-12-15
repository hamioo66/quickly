# -*- coding=UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time,os,unittest
from selenium.webdriver.common.keys import Keys
from utils.logger import Logger
logger = Logger(logger="BasePage").getlog()
#参数0、1、2分别对应管理员、批发商代理商

def login(num):
    user_file = open('../file/login.txt', 'r')
    values = user_file.readlines()
    user_file.close()
    i = []
    for search in values:
        i.append(search)
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



def sendValueToInput(inputValues=[]):
    allInputs = driver.find_elements_by_css_selector('li>input')
    try:
        i=0
        while i<len(inputValues):
                allInputs[i].send_keys(inputValues[i])
                i=i+1
    except:
         print("参数值为空")

def selectArea(area=[]):     #级联选择
    formSearchs = driver.find_elements_by_class_name('form-control')
    selects = driver.find_elements_by_css_selector('button[title="请选择"]')
    i = 0
    while i < len(area):
        for j in range(0,len(area)):
            try:
                selects[j].click()
                formSearchs[j].send_keys(area[i])
                formSearchs[j].send_keys(Keys.ENTER)
                i=i+1
            except:
                ValueError

def FileImg(file):
    imgFiles = driver.find_elements_by_css_selector('section>input')
    print len(imgFiles)
    try:
        i=0
        while i<len(imgFiles):
            imgFiles[i].send_keys(file)
            i=i+1
    except:
         print("参数值为空")

def MoreImgFiles(file):  #上传更多图片，只针对第二张
    try:
        secondImgFile = driver.find_element_by_id("file2")
        more=driver.find_element_by_id("file3")
        secondImgFile.send_keys(file)
        more.send_keys(file)
    except:
        print "当前元素不存在"

if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = 'http://123.206.57.62:17000/index'
    driver.get(url)
    driver.maximize_window()
    login(0)
    lis = driver.find_elements_by_class_name('link')
    # 点击用户管理
    lis[1].click()
    time.sleep(1)
    driver.find_element_by_link_text(u'代理商列表').click()
    mainIframe = driver.find_elements_by_class_name('iframeBox')
    driver.switch_to.frame(mainIframe[-1])
    time.sleep(1)
    driver.find_element_by_class_name('columnBtn').click()
    print driver.find_element_by_class_name('columnBtn').text
    time.sleep(5)
    driver.find_element_by_css_selector('button.columnBtn.js_add_agent').click()
    mainIframe1 = driver.find_elements_by_tag_name('iframe')
    driver.switch_to.frame(mainIframe1[-1])

    inputValues=[u'测试', '15599155289', '15599155289', u'测试地址地址']
    sendValueToInput(inputValues)

    # 测试添加代理商
    area = [u'北京市', u'市辖区', u'北京市', u'市辖区', u'东城区', u'景山街道']
    selectArea(area)

    FileImg('C:\\Users\\lenovo\\Pictures\\aa.jpg')
    MoreImgFiles('C:\\Users\\lenovo\\Pictures\\bb.jpg')
    secondImgFile = driver.find_element_by_id("file3")
    secondImgFile.send_keys('C:\\Users\\lenovo\\Pictures\\cc.jpg')

    li = driver.find_elements_by_css_selector('li>input')
    # print li[1].text
    li[1].clear()
    time.sleep(4)
    scroll_to = driver.find_element_by_css_selector("input[name='addDetail']")
    scroll_to.send_keys(Keys.SHIFT, Keys.TAB)

    # selects = driver.find_elements_by_css_selector('button[title="请选择"]')
    # selects[0].send_keys(Keys.SHIFT, Keys.TAB)

    # scroll_to = driver.find_element_by_css_selector("input[name='addDetail']")
    # scroll_to.send_keys(Keys.TAB)
    # time.sleep(4)
    # driver.find_element_by_class_name('submit').click()
    # driver.find_element_by_class_name('layui-layer-btn0').click()

    # selectArea(area=[u'贵州省', u'贵阳市'])
    # driver.quit()


