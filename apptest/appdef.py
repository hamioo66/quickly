#coding:utf-8
import random,time,os
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utils.logger import Logger
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

device='8ac7d424' #此处设备号
pack='com.yiyaotong.hurryfirewholesale' #此处是app的package名称
activity='com.yiyaotong.hurryfirewholesale.ui.GuideActivity'#此处是app的主activity

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
desired_caps = {}
desired_caps['device'] = 'android'
desired_caps['platformName'] = 'Android'
desired_caps['browserName'] = ''
desired_caps['Version'] = '4.4.4'
desired_caps['deviceName'] = device
desired_caps['appPackage'] = pack
desired_caps['appActivity'] = activity
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def xuantu():
    driver.implicitly_wait(2)
    tupian = driver.find_elements_by_id("image")
    tupian[random.randint(1, len(tupian) - 4)].click()
    save = driver.find_elements_by_id("tv_contact")
    save1 = driver.find_elements_by_id("menu_crop")
    if len(save) == 1:
        driver.find_element_by_id("tv_contact").click()
    elif len(save1) == 1:
        driver.find_element_by_id("menu_crop").click()
    time.sleep(2)
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    # print x,y
    return (x, y)
def swipeclick7(t):  # 批发商注册选择联系区域
    l = getSize()
    x1 = int(l[0] * 0.25)
    y1 = int(l[1] * 0.85)
    y2 = int(l[1] * 0.25)
    driver.swipe(x1, y1, x1, y2, t)
def swipeUp(t):  # 向上滑
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.85)
    y2 = int(l[1] * 0.25)
    driver.swipe(x1, y1, x1, y2, t)
def swipeDown(t):   #向下滑
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)
def swipeclickdate(t):  # 选择期望送达时间
    l = getSize()
    x1 = int(l[0] * 0.42)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.5)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)
def adress(jibie):
    # 选择地址方法，参数1代表选择到街道，其他值代表选择到区（需考虑选择控件的ID）
    findsheng = driver.find_elements_by_name('福建省')
    while len(findsheng) == 0:
        swipeclick7(1000)
        findsheng = driver.find_elements_by_name('福建省')
        if len(findsheng) == 1:
            driver.find_element_by_name('福建省').click()
            break
    driver.find_element_by_id("textViewCity").click()
    driver.find_element_by_name('福州市').click()
    driver.find_element_by_id("textViewCounty").click()
    driver.find_element_by_name("鼓楼区").click()
    if jibie == 1:
        driver.find_element_by_id("textViewStreet").click()
        driver.find_element_by_name("东街街道").click()
def update():
    #检查是否有更新，如果有就关闭
    driver.implicitly_wait(2)
    update = driver.find_elements_by_id("autoupdate_btnUpdate")
    if len(update) == 1:
        driver.keyevent(4)
def xiaoxi(geshu, title, neirong):
    # 是否接收到推送消息方法，参数：geshu:当前消息列表的条数，title:需要校验的消息标题，neirong:需要校验的消息内容
    logg(u"===== 进入推送消息校验环节 =====")
    driver.implicitly_wait(2)
    yes = "收到推送消息"
    xiaoxititle = driver.find_elements_by_id("message_title")
    if len(xiaoxititle) == 0:
        driver.find_element_by_id("messageIV").click()
    xiaoxititle = driver.find_elements_by_id("message_title")
    xiaoxineirong = driver.find_elements_by_id("message_content")
    if len(xiaoxititle) == geshu == len(xiaoxineirong) and unicode(title) in xiaoxititle[0].text and \
                    unicode(neirong) in xiaoxineirong[0].text:
        return yes
    else:
        return False
def pay(bankname, password):
    # 支付宝支付方法：bankname是支付宝页面显示的银行卡名称："中国工商银行储蓄卡(8130)"，password是支付密码
    driver.find_element_by_name('支付宝支付').click()
    driver.implicitly_wait(5)
    a = driver.find_elements_by_class_name("android.view.View")
    a[7].click()
    driver.find_element_by_accessibility_id(bankname).click()
    driver.implicitly_wait(10)
    driver.find_element_by_class_name("android.widget.Button").click()
    driver.find_element_by_class_name("android.widget.ListView").send_keys(password)
    driver.implicitly_wait(5)
    driver.find_element_by_name("完成").click()
    driver.implicitly_wait(3)
def yzm():
    #获取登录时的验证码。不需要带参数
    a = driver.find_element_by_id("tv_yzm").text
    b = str(a)
    yzm = b.split()
    driver.find_element_by_id("edit_yzm").send_keys(yzm)  # 填入验证码
def edittextclear(text):
   #清除EditText文本框里的内容
    driver.keyevent(123)
    for i in range(0, len(text)):
        driver.keyevent(67)