# -*- coding=UTF-8 -*-
# driver.find_element_by_class_name('selectpicker').click()
# driver.find_element_by_class_name("selectpicker").click()
# d=driver.find_elements_by_tag_name('option')
# d[0].click()
# driver.find_element_by_name('password').send_keys(u"123456")
# driver.find_element_by_name('telphone').send_keys(u"18888888888")

# for select in s.options:
#     print select.text
# driver.find_element_by_class_name("selectpicker").find_elements_by_tag_name("option")[2].click()

# from selenium.webdriver.support.select import Select
# s = Select(driver.find_element_by_class_name("selectpicker"))
# s.select_by_value(str(num))


# submit_btn = "id=>su"
def reversed_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
print sorted([36,5,1,9,21],reversed_cmp)

from Tkinter import *
from SimpleDialog import *
root = Tk()
# 创建一个SimpleDialog
# buttons:显示的按钮
# Default:默认选中的按钮
dlg = SimpleDialog(root,text=u"是否登录",buttons=['yes','no','cancel'],default=0)
print dlg.go()
root.mainloop()

for i in range(1,28):
    print i



