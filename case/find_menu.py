# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2017/12/8
describle：查找后台左侧菜单方法
"""
from  utils.base_page import BasePage

class Find_menu(BasePage):
    link = "class=>link"
    def find_menu(self,father_menu,child_menu):
        self.find_elements(self.link)


        pass



