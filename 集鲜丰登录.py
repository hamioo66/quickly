# -*- coding=UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random

user_file = open('file/login.txt', 'r')
values = user_file.readlines()
user_file.close()
i=[]
for search in values:
    i.append(search)
driver=webdriver.Chrome()
driver.get('http://123.206.57.62:17000/index')
driver.maximize_window()
# driver.find_element_by_class_name('selectpicker').click()
# driver.find_element_by_class_name("selectpicker").click()
# d=driver.find_elements_by_tag_name('option')
# d[0].click()
# driver.find_element_by_name('password').send_keys(u"123456")
# driver.find_element_by_name('telphone').send_keys(u"18888888888")

# for select in s.options:
#     print select.text
# driver.find_element_by_class_name("selectpicker").find_elements_by_tag_name("option")[2].click()
num=random.randint(0,2)
type=i[num].split(':')[0]
keys=i[num].split(':')[1]
print num,type,keys
username = keys.split(',')[0]
password = keys.split(',')[1]
num=num+1
s=Select(driver.find_element_by_class_name("selectpicker"))
s.select_by_value(str(num))
driver.find_element_by_name('telphone').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
# driver.find_element_by_name('loginBtn').click()
lis=driver.find_elements_by_class_name('link')
lis[1].click()
if type=='管理员':
    print '当前登录用户是管理员'
elif type=='批发商':
    print '当前登录用户是批发商'
    driver.find_element_by_link_text('商品列表').click()
else:
    print '当前登录用户是代理商'
print("用户名是:%s" %username)
print("密码是:%s" %password)
# print len(lis)



