# -*- coding=UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import random,time,logging



logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)-8s %(levelname)-8s%(message)s',
                #datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)-8s %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)



user_file = open('file/login.txt', 'r')
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
    #logging.info("",num,type,keys)
    username = keys.split(',')[0]
    password = keys.split(',')[1]
    num=num+1
    s=Select(driver.find_element_by_class_name("selectpicker"))
    s.select_by_value(str(num))
    driver.find_element_by_name('telphone').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    # driver.find_element_by_name('loginBtn').click()

    if type=='管理员':
        logging.info('当前登录用户是管理员')
        # lis[0].click()
        # driver.find_element_by_link_text('商品列表').click()
    elif type=='批发商':
        logging.info('当前登录用户是批发商')
    else:
        logging.info('当前登录用户是代理商')
    logging.info(u"用户名是:%s" %username)
    logging.info(u"密码是:%s" %password)
# print len(lis)
login(1)
lis=driver.find_elements_by_class_name('link')
lis[2].click()
driver.find_element_by_link_text('订单列表').click()
mainIframe=driver.find_elements_by_class_name('iframeBox')
driver.switch_to.frame(mainIframe[-1])
#根据订单号查找订单数据
# driver.find_element_by_id('orderNo').send_keys('MD01201711061111537404096')
"""根据状态查找订单数据"""
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/button').click()
liss=driver.find_elements_by_tag_name('li')
value5=liss[5].text
logging.info(u"当前选择状态是:%s" %value5)
"""0全部 1 已付定金 2待发货 3已发货 4已签收 5交易成功 6已取消"""
liss[5].click()
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/table/tbody/tr[2]/td/input[1]').click()
time.sleep(5)
table=driver.find_element_by_id('orderList')
"""table的总行数，包含标题"""
table_rows=table.find_elements_by_tag_name('tr')
logging.info(u"总行数:%d",len(table_rows))
"""table的总列数"""
table_cols=table.find_elements_by_tag_name('th')
logging.info(u"总列数:%d",len(table_cols))

for i in range(1,len(table_rows)):
    rowRandom_col6=table_rows[int(i)].find_elements_by_tag_name('td')[6].text
    logging.info(u"第%i行6列的值:%s",i,rowRandom_col6)
    if rowRandom_col6==value5:
        logging.info("查询数据正确")
    else:
        logging.info("查询有问题")
# time.sleep(5)
"""切换到初始的iframe"""
driver.switch_to.default_content()
time.sleep(2)
"""退出登录"""
moveto=driver.find_element_by_class_name('userListBox')
ActionChains(driver).move_to_element(moveto).perform()
driver.find_element_by_link_text('退出').click()

time.sleep(2)
driver.quit()

