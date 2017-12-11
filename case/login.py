# -*- coding=UTF-8 -*-
from utils.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
class Login(BasePage):
    telphone = "name=>telphone"
    password = "name=>password"
    roleCode = "name=>roleCode"
    loginbtn = "id=>loginBtn"
    # 登录
    def login(self,value,telphone,password):
        s = Select(self.find_element(self.roleCode))
        s.select_by_value(value)
        self.type(self.telphone,telphone)
        self.type(self.password,password)
        self.click(self.loginbtn)

if __name__ =="__main__":
    driver=webdriver.Firefox()
    driver.get("http://123.206.57.62:17000")
    time.sleep(2)
    Login(driver).login("1", "18888888888", "123456")
