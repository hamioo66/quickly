# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2017/12/8
describle：查找后台左侧菜单方法
"""
from utils.base_page import BasePage

class Common(BasePage):
    link = "class_name=>link"
    iframebox = "tag_name=>iframe"                                     # 获取iframe的个数
    search_marchant_accout = "selector_selector=>input[type='text']"   # 搜索商户账号
    search_btn = "selector_selector=>input[value='搜索']"              # 点击搜索
    table = "id=>example"                                              # 获取dataTable的id
    tr = "selector_selector=>tr[role='row']"                           # 获取当前数据有多少行
    th = "selector_selector=>tr[role='row']>th"                        # 获取当前数据有多少列

    frames = "class_name=>iframeBox"


    def find_menu(self, father_menu_index, child_menu):
        """
        查找菜单
        :param father_menu_index: 根节点菜单索引值
        :param child_menu: 子菜单名字 
        :return: find_menu(1, "商品列表")
        """
        child_menu_text = "link_text=>%s" % child_menu
        links = self.find_elements(self.link)
        self.click_list(self.link, father_menu_index)
        print links[father_menu_index].text
        self.sleep(3)
        submenus = self.find_elements(child_menu_text)
        for j in range(0, len(submenus)):
            self.click_list(child_menu_text, j)



    def merchant(self, iframeNum, account):
        """
        手机端注册商户，后台校验数据是否存在
        :param iframeNum: 遍历iframe
        :param account: 商户注册账号
        :return: merchant(1, "17300200000")
        """
        self.switch_to_frame(self.iframebox, iframeNum)
        self.type(self.search_marchant_accout, account)
        self.sleep(2)
        self.click(self.search_btn)
        self.sleep(5)

    def get_table_text(self,account):
        """
        逐行获取列表数据
        :param account: 商户注册账号
        :return: get_table_text("17300200000")
        """
        table = self.find_element(self.table)
        table_rows = self.find_elements(self.tr)
        print(u"总行数:%d"  %(len(table_rows) - 1))
        table_cols = self.find_elements(self.th)
        print(u"总列数:%d" % len(table_cols))
        i = 0
        while i < len(table_rows):
            info = table_rows[int(i)].text
            if info.find(account) != -1:
                print(u"第%d行的数据是：%s" % (i, table_rows[int(i)].text))
                print("用户注册成功")
            i = i + 1

    def add_agent(self):
        self.switch_to_frame(self.frames, -1)
        self.sleep(2)






