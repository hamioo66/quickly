# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2017/12/8
describle：查找后台左侧菜单方法
"""
from utils.base_page import BasePage

class Find_menu(BasePage):
    link = "class_name=>link"
    def find_menu(self, father_menu, child_menu):
        child_menu_text = "link_text=>%s" % child_menu
        links = self.find_elements(self.link)
        #print links
        self.click_list(self.link, father_menu)
        print links[father_menu].text
        submenus = self.find_elements(child_menu_text)
        #print submenus
        for j in range(0, len(submenus)):
            print j
            self.click_list(child_menu_text,j)
        self.sleep(5)


