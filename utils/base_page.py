# coding=utf-8
import os.path
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from utils.logger import Logger

# 创建日志实例
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器并结束测试
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # 定位单个元素方法
    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("找到元素成功返回的数据是：%s By %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("找到元素成功返回的数据是：%s By %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("没有元素异常: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("请输入有效类型的目标元素")

        return element

    # 输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 或者网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)



 #集鲜丰公共的一些方法

        # 定位多个元素

    """
        author:hamioo
        date:2017/12/8
    """
    def find_elements(self, selector):
        elements = ''
        if '=>' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                elements = self.driver.find_elements_by_css_selector(selector_value)
                logger.info("当前元素的个数为%d" % len(elements))
            except NoSuchElementException as e:
                logger.error("元素不存在: %s" % e)
                self.get_windows_img()
        elif selector_by == "n" or selector_by == 'name':
            elements = self.driver.find_elements_by_name(selector_value)
            logger.info("当前元素的个数为%d" % len(elements))
        elif selector_by == "c" or selector_by == 'class_name':
            elements = self.driver.find_elements_by_class_name(selector_value)
            logger.info("当前元素的个数为%d" % len(elements))
        elif selector_by == "l" or selector_by == 'link_text':
            elements = self.driver.find_elements_by_link_text(selector_value)
            logger.info("当前元素的个数为%d" % len(elements))
        elif selector_by == "p" or selector_by == 'partial_link_text':
            elements = self.driver.find_elements_by_partial_link_text(selector_value)
            logger.info("当前元素的个数为%d" % len(elements))
        elif selector_by == "t" or selector_by == 'tag_name':
            elements = self.driver.find_elements_by_tag_name(selector_value)
            logger.info("当前元素的个数为%d" % len(elements))
        elif selector_by == "s" or selector_by == 'selector_selector':
            elements = self.driver.find_elements_by_css_selector(selector_value)
            logger.info("当前元素的个数为%d" % len(elements))
        else:
            raise NameError("请输入有效类型的目标元素")

        return elements


    def click_list(self, selector, num):
        """
        多元素的定位点击
        :param selector: 
        :param num: 
        :return: 
        """
        els = self.find_elements(selector)
        try:
            els[num].click()
            logger.info("The element \' %s \' was clicked." % els[num])
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    def switch_to_frame(self, selector, num):
        """
        切换到对应的iframe
        :param selector: 
        :param num: 
        :return: 
        """
        els = self.find_elements(selector)
        self.driver.switch_to.frame(els[num])


    def switch_to_frame_out(self):
        """
        回到中iframe中
        """
        self.driver.switch_to.default_content()

    # 获取表单中所有input并传值
    def value_to_input(self, inputValues=[]):
        allInputs = self.driver.find_elements_by_css_selector('li>input')
        try:
            i = 0
            while i < len(inputValues):
                    allInputs[i].send_keys(inputValues[i])
                    i = i+1
        except:
            logger.info("参数值为空")

    # 获取表单级联下拉列表并选值，这里针对select2
    def select_area(self, area=[]):     #级联选择
        formSearchs = self.driver.find_elements_by_class_name('form-control')
        selects = self.driver.find_elements_by_css_selector('button[title="请选择"]')
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
    # 上传图片
    def fileImg(self, file):
        imgFiles = self.driver.find_elements_by_css_selector('section>input')
        print len(imgFiles)
        try:
            i = 0
            while i < len(imgFiles):
                imgFiles[i].send_keys(file)
                i = i+1
        except:
            logger.info("参数值为空")
    # 上传多张图片
    def moreImgFiles(self, file):  #上传更多图片，只针对第二张
        try:
            secondImgFile = self.driver.find_element_by_id("file2")
            more = self.driver.find_element_by_id("file3")
            secondImgFile.send_keys(file)
            more.send_keys(file)
        except:
            logger.info("当前元素不存在")