#-*- coding:utf-8 -*-
'''
APP操作订单
'''
import appdef,unittest,HTMLTestRunner,random,time
from utils.logger import Logger

suijishu = str(random.randint(10000,99999))
logger  = Logger(logger="BasePage").getlog()
class Dingdan_app(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '判断当前APP是否处于登录状态，并初始化登录状态'
        driver = appdef.driver
        driver.implicitly_wait(3)
        driver.find_element_by_name("我的").click()
        a = driver.find_elements_by_id("whlosalersp_settingMIV")
        b = driver.find_elements_by_id("merchant_settingMIV")
        if len(a) == 1:
            driver.find_element_by_id("whlosalersp_settingMIV").click()
            driver.find_element_by_id("loginOutLL").click()
        elif len(b) == 1:
            driver.find_element_by_id("merchant_settingMIV").click()
            driver.find_element_by_id("loginOutLL").click()
    def test_register_wholesaler(self):
        '注册批发商，正常注册，预期结果：注册批发商成功'
        driver = appdef.driver
        driver.find_element_by_name("批发商").click()
        driver.find_element_by_id("tv_rg").click()
        driver.find_element_by_id("merchantNameET").send_keys(u"176230" + suijishu)
        driver.find_element_by_id("passwordET").send_keys(u"123456")
        driver.find_element_by_id("codeET").send_keys(u"213213")
        driver.find_element_by_id("registerBT").click()
        a = driver.find_element_by_id("titlebar_text").text
        self.assertEqual(u"完善信息", a)
        time.sleep(2)
        if a == u"完善信息":
            driver.find_element_by_id("phoneET").send_keys(u"176231" + suijishu)
            driver.find_element_by_id("enterpriseNameET").send_keys(u"自动批发商" + suijishu)
            driver.find_element_by_id("regionTV").click()
            appdef.adress(0)
            driver.find_element_by_id("contactAddressET").send_keys(u"批发商详细地址" + suijishu)
            driver.find_element_by_id("addressTV").click()
            driver.find_element_by_id("contentTV").click()
            appdef.adress(0)
            time.sleep(1)
            driver.find_element_by_id("tv_contact").click()
            driver.find_element_by_id("classTypeTV").click()
            hyfl = driver.find_elements_by_id("contentCheckBox")
            hyfl[1].click()
            hyfl[2].click()
            hyfl[3].click()
            driver.find_element_by_id("tv_contact").click()
            driver.find_element_by_id("logoIV").click()
            appdef.xuantu()
            driver.find_element_by_id("registerBT").click()
            time.sleep(1)
            a = driver.find_elements_by_id("licenseIV")
            self.assertEqual(1, len(a))
            if len(a) == 1:
                driver.find_element_by_id("licenseIV").click()
                appdef.xuantu()
                driver.find_element_by_id("identity1IV").click()
                appdef.xuantu()
                driver.find_element_by_id("identity2IV").click()
                appdef.xuantu()
                driver.find_element_by_id("image").click()
                appdef.xuantu()
                driver.find_element_by_id("registerBT").click()
                save1 = driver.find_element_by_id("titlebar_text").text
                self.assertEqual(u"登录",save1)
                if save1 == u"登录":
                    logg(u"批发商注册成功，流程继续")
        else:
            logg(u"批发商注册失败，流程中断")
    def test_wholesaler_login(self):
        '使用刚注册的批发商账号登录APP，预期结果：登录成功'
        driver = appdef.driver
        driver.find_element_by_id("edit_account").send_keys(u"176230" + suijishu)
        driver.find_element_by_id("edit_pz").send_keys(u"123456")
        appdef.yzm()
        driver.find_element_by_id("tv_login").click()
        a = driver.find_element_by_id("supplierNameTV").text
        self.assertEqual(u"自动批发商" + suijishu, a)
        driver.find_element_by_name("我的").click()
        b = driver.find_element_by_id("whlosalersp_accountTV").text
        self.assertEqual(u"176230" + suijishu ,b)
        if u"自动批发商" + suijishu == a and u"176230" + suijishu == b:
            logg(u"批发商登录成功，流程继续")
        else:
            logg(u"批发商登录失败，流程中断")
    def test_wholesaler_setting_shop(self):
        '批发商设置店铺，预期结果：可正常设置店铺'
        driver = appdef.driver
        driver.find_element_by_id("whlosalersp_shopMIV").click()
        driver.find_element_by_id("store_manage_btnShopSetup").click()
        a = driver.find_element_by_id("shop_setup_tvAcceptTime").text
        logg(u"接单时间的默认值是：" + a)
        driver.find_element_by_id("shop_setup_tvAcceptTime").click()
        driver.find_element_by_id("tv_sure").click()
        b = driver.find_element_by_id("shop_setup_tvDispatchTime").text
        logg(u"配送时间的默认值是：" + b)
        driver.find_element_by_id("shop_setup_tvDispatchTime").click()
        driver.find_element_by_id("tv_sure").click()
        driver.find_element_by_id("shop_setup_etTime").send_keys(u"2")
        driver.find_element_by_id("shop_setup_etMoney").send_keys(u"100")
        driver.find_element_by_id("shop_setup_btnSave").click()
        c = driver.find_elements_by_id("shop_setup_btnSave")
        self.assertEqual(0,len(c))
        if len(c) == 0:
            logg(u"批发商店铺设置成功，流程继续")
        else:
            logg(u"批发商店铺设置失败，流程中断")
    def test_wholesaler_setting_fenlei(self):
        '批发商设置店铺分类，预期结果：可正常设置店铺分类'
        driver = appdef.driver
        driver.find_element_by_id("store_manage_btnShopType").click()
        driver.find_element_by_id("shop_type_tvAdd").click()
        driver.find_element_by_id("shop_type_adjust_etName").send_keys(u"自动分类" + suijishu)
        driver.find_element_by_id("shop_type_adjust_etOrder").send_keys(u"1")
        driver.find_element_by_id("shop_type_adjust_cbStatus").click()
        time.sleep(1)
        driver.find_element_by_id("shop_type_adjust_btnSave").click()
        a = driver.find_element_by_id("list_shop_type_tvType").text
        b = driver.find_element_by_id("list_shop_type_tvStatus").text
        self.assertEqual(u"自动分类" + suijishu,a)
        self.assertEqual(u"已启用",b)
        if u"自动分类" + suijishu == a  and u"已启用" == b:
            logg(u"批发商店铺分类新建成功，流程继续")
        else:
            logg(u"批发商店铺分类新建失败，流程中断")
        driver.find_element_by_id("titlebar_img_back").click()
        time.sleep(1)
        # driver.find_element_by_id("titlebar_img_back").click()
        # driver.find_element_by_id("whlosalersp_shopMIV").click()
    def test_wholesaler_setting_product(self):
        '批发商添加商品，预期结果：可正常添加商品'
        driver = appdef.driver
        driver.find_element_by_id("store_manage_btnProductManage").click()
        driver.find_element_by_id("product_manage_btnAdd").click()
        driver.find_element_by_id("product_add_etProductName").send_keys(u"自动商品" + suijishu)
        driver.find_element_by_id("item_image_ivPictrue").click()
        appdef.xuantu()
        fenlei = driver.find_element_by_id(u"product_add_tvShopType").text
        a = u"自动分类" + suijishu in fenlei
        self.assertEqual(True,a)
        if u"自动分类" + suijishu in fenlei:
            logg(u"商品分类回显正确，流程继续")
            driver.find_element_by_id("product_add_etProductUnits").clear()
            driver.find_element_by_id("product_add_etProductUnits").send_keys(u"件")
            a = driver.find_element_by_id("product_add_tvUnit01").text
            b = driver.find_element_by_id("product_add_tvUnit02").text
            c = u"件" in b
            self.assertEqual(u"/件",a)
            self.assertEqual(u" 件",b)
            if a == u"/件" and b == u" 件":
                logger(u"商品单位回显正确，流程继续")
                driver.find_element_by_id("product_add_etProductPrice").send_keys(u"100")
                driver.find_element_by_id("product_add_etProductQuantity").send_keys(u"3")  #限购3件，单价100/件
                driver.find_element_by_id("product_add_btnSave").click()
                productname = driver.find_element_by_id("list_product_tvName").text
                productprice = driver.find_element_by_id("list_product_tvPrice").text
                status = driver.find_element_by_id("list_product_tvStatus").text
                power = driver.find_elements_by_class_name("android.widget.TextView")
                power1 = []
                for i in power:
                    power1.append(i.text)
                if u" 编辑" in power1[-4:] and u" 删除" in power1[-4:] and u" 上架" not in power1[-4:] and u" 下架" not in power1[-4:]:
                    logger(u"审核中状态的商品权限正确，流程继续")
                    self.assertEqual(u"自动商品" + suijishu,productname)
                    self.assertIn(u"100.00/件",productprice)
                    self.assertEqual(u"审核中",status)
                else:
                    logger(u"审核中状态的商品权限错误，流程中断")
                    self.assertEqual(1,0)   #返回测试报告状态码：case失败
            else:
                logger(u"商品单位回显错误，流程中断")
        else:
            logger(u"商品分类回显错误，流程中断")
    def test_web_reviewproduct(self):
        '后台管理员审核商品，预期结果：审核通过'
        import webdef
        browser = webdef.browser
        webdef.login_index(1)
        webdef.login_web(1,'审核列表')
        webdef.action('通过')
        webdef.iframe(-2)
        webdef.login_web(1,'商品列表')
        a = webdef.listrow('自动商品' + suijishu,'通过')
        self.assertEqual("找到新增数据，列表回显正确",a)
        if a == "找到新增数据，列表回显正确":
            logger(u"管理员审核商品通过，流程继续")
        else:
            logger(u"管理员审核商品失败，流程中断")
        browser.quit()
    def test_wholesaler_setting_product_001(self):
        '后台审核通过商品，APP校验商品状态。预期结果：商品当前状态为已通过，权限为：上架，编辑，删除'
        driver = appdef.driver
        driver.find_element_by_id("titlebar_img_back").click()
        driver.find_element_by_id("store_manage_btnProductManage").click()
        productname = driver.find_element_by_id("list_product_tvName").text
        productprice = driver.find_element_by_id("list_product_tvPrice").text
        status = driver.find_element_by_id("list_product_tvStatus").text
        power = driver.find_elements_by_class_name("android.widget.TextView")
        power1 = []
        for i in power:
            power1.append(i.text)
        if u" 编辑" in power1[-4:] and u" 删除" in power1[-4:] and u" 上架" in power1[-4:] and u" 下架" not in power1[-4:]:
            logger(u"已通过状态的商品权限正确，流程继续")
            self.assertEqual(u"自动商品" + suijishu, productname)
            self.assertIn(u"100.00/件", productprice)
            self.assertEqual(u"已通过", status)
        else:
            logger(u"已通过状态的商品权限错误，流程中断")
            self.assertEqual(1, 0)  # 返回测试报告状态码：case失败
    def test_wholesaler_setting_product_002(self):
        '调价，修改商品价格，检查商品状态。预期结果：商品价格发生变动，其他状态不变'
        driver = appdef.driver
        driver.find_element_by_id("list_product_tvPriceAdjust").click()
        productname = driver.find_element_by_id("dialog_price_tvName").text
        productprice = driver.find_element_by_id("dialog_price_etPrice").text
        self.assertEqual(u"自动商品" + suijishu,productname) #商品名称有bug，待修复
        self.assertEqual(u"100.00",productprice)
        if u"自动商品" + suijishu == productname and u"100.00" == productprice:
            logger(u"商品调整价格页面中，商品属性回显正确，流程继续")
        else:
            logger(u"商品调整价格页面中，商品属性回显正确，流程中断")
        driver.find_element_by_id("dialog_price_etPrice").clear()
        driver.find_element_by_id("dialog_price_etPrice").send_keys(u"200")
        driver.find_element_by_id("dialog_price_btnConfirm").click()
        driver.find_element_by_id("titlebar_img_back").click()
        driver.find_element_by_id("store_manage_btnProductManage").click()
        productname = driver.find_element_by_id("list_product_tvName").text
        productprice = driver.find_element_by_id("list_product_tvPrice").text
        status = driver.find_element_by_id("list_product_tvStatus").text
        power = driver.find_elements_by_class_name("android.widget.TextView")
        power1 = []
        for i in power:
            power1.append(i.text)
        if u" 编辑" in power1[-4:] and u" 删除" in power1[-4:] and u" 上架" in power1[-4:] and u" 下架" not in power1[-4:]:
            logger(u"调价后的商品权限正确，流程继续")
            self.assertEqual(u"自动商品" + suijishu, productname)
            self.assertIn(u"200.00/件", productprice)
            self.assertEqual(u"已通过", status)
        else:
            logger(u"调价后的商品权限错误，流程中断")
            self.assertEqual(1, 0)  # 返回测试报告状态码：case失败
    def test_wholesaler_setting_product_003(self):
        '编辑商品，商品信息发生更改，其他信息不变。预期结果：可正常编辑商品'
        driver = appdef.driver
        driver.find_element_by_id("list_product_tvEdit").click()
        title = driver.find_element_by_id("titlebar_text").text
        productname = driver.find_element_by_id("product_add_etProductName").text
        productfenlei = driver.find_element_by_id("product_add_tvShopType").text
        productdanwei = driver.find_element_by_id("product_add_etProductUnits").text
        productprice = driver.find_element_by_id("product_add_etProductPrice").text
        productxiangou = driver.find_element_by_id("product_add_etProductQuantity").text
        self.assertEqual(u"编辑商品",title)
        self.assertEqual(u"自动商品" + suijishu, productname)
        time.sleep(2)
        a = u"自动分类" + suijishu in productfenlei
        self.assertEqual(True,a)
        self.assertEqual(u"件", productdanwei)
        self.assertEqual(u"200.0", productprice)#此处应显示200.00。等待bug修复
        self.assertEqual(u"3", productxiangou)
        if title == u"编辑商品" and productname == u"自动商品" + suijishu:
            logger(u"商品编辑页面中，商品信息回显正确，流程继续")
            driver.find_element_by_id("product_add_etProductName").clear()
            driver.find_element_by_id("product_add_etProductName").send_keys(u"自动商品" + str(int(suijishu) + 1))
            driver.find_element_by_id("product_add_etProductPrice").clear()
            driver.find_element_by_id("product_add_etProductPrice").send_keys(u"150")
            driver.find_element_by_id("product_add_btnSave").click()
            time.sleep(1)
            productname1 = driver.find_element_by_id("list_product_tvName").text
            productprice1 = driver.find_element_by_id("list_product_tvPrice").text
            status1 = driver.find_element_by_id("list_product_tvStatus").text
            self.assertEqual(u"自动商品" + str(int(suijishu) + 1), productname1)
            self.assertIn(u"150.00/件", productprice1)
            self.assertEqual(u"已通过",status1)
            if u"自动商品" + str(int(suijishu) + 1) == productname1 and u"150.00/件" == productprice1\
                    and status1 == u"已通过":
                power = driver.find_elements_by_class_name("android.widget.TextView")
                power1 = []
                for i in power:
                    power1.append(i.text)
                if u" 编辑" in power1[-4:] and u" 删除" in power1[-4:] and u" 上架" in power1[-4:] and u" 下架" not in power1[-4:]:
                    logger(u"调价后的商品权限正确，流程继续")
                else:
                    logger(u"调价后的商品权限错误，流程中断")
                    self.assertEqual(1, 0)  # 返回测试报告状态码：case失败
        else:
            logger(u"商品编辑页面中，商品信息回显正确，流程中断")
    def test_wholesaler_setting_product_004(self):
        '批发商操作商品上架。预期结果：未上架中商品消失，已上架中显示该商品'
        driver = appdef.driver
        driver.find_element_by_id("list_product_tvproductOpen").click()
        a = driver.find_elements_by_id("product_add_etProductPrice")
        self.assertEqual(0,len(a))
        if len(a) == 0 :
            driver.find_element_by_name("已上架").click()
            productname = driver.find_element_by_id("list_product_tvName").text
            productprice = driver.find_element_by_id("list_product_tvPrice").text
            status = driver.find_element_by_id("list_product_tvStatus").text
            power = driver.find_elements_by_class_name("android.widget.TextView")
            power1 = []
            for i in power:
                power1.append(i.text)
            if u" 编辑" not in power1[-4:] and u" 删除" not in power1[-4:] and u" 上架" not in power1[-4:] and u" 下架" in power1[-4:]:
                logger(u"上架后的商品权限正确，流程继续")
                self.assertEqual(u"自动商品" + str(int(suijishu)+1), productname)
                self.assertIn(u"150.00/件", productprice)
                self.assertEqual(u"已上架", status)
                if status == u"已上架":
                    driver.find_element_by_name("已下架").click()
                    time.sleep(1)
                    productname1 = driver.find_elements_by_id("list_product_tvName")
                    self.assertEqual(0,len(productname1))
                    if len(productname1) == 0:
                        logger(u"批发商操作商品上架成功，流程继续")
                    else:
                        logger(u"批发商操作商品上架失败，流程中断")
            else:
                logger(u"上架后的商品权限错误，流程中断")
                self.assertEqual(1, 0)  # 返回测试报告状态码：case失败
    def test_user_shop_001(self):
        '注销批发商，注册商户。预期结果：注册商户成功'
        driver = appdef.driver
        driver.find_element_by_id("titlebar_img_back").click()
        time.sleep(1)
        driver.find_element_by_id("titlebar_img_back").click()
        driver.find_element_by_id("whlosalersp_settingMIV").click()
        driver.find_element_by_id("loginOutLL").click()
        driver.find_element_by_name("商户").click()
        driver.find_element_by_id("tv_rg").click()
        title = driver.find_element_by_id("titlebar_text").text
        self.assertEqual(u"商户注册",title)
        driver.find_element_by_id("merchantNameET").send_keys(u"176888" + suijishu)
        driver.find_element_by_id("passwordET").send_keys(u"123456")
        driver.find_element_by_id("codeET").send_keys(u"213213")
        driver.find_element_by_id("registerBT").click()
        title1 = driver.find_element_by_id("titlebar_text").text
        self.assertEqual(u"完善信息",title1)
        driver.find_element_by_id("phoneET").send_keys(u"176889" + suijishu)
        driver.find_element_by_id("storeNameET").send_keys(u"自动商户" + suijishu)
        driver.find_element_by_id("regionTV").click()
        appdef.adress(0)
        driver.find_element_by_id("contactAddressET").send_keys(u"自动商户门店详细地址" + suijishu)
        driver.find_element_by_id("registerBT").click()
        title2 = driver.find_element_by_id("titlebar_text").text
        self.assertEqual(u"选填信息",title2)
        driver.find_element_by_id("enterpriseNameET").send_keys(u"自动商户企业" + suijishu)
        driver.find_element_by_id("storeIV").click()
        appdef.xuantu()
        time.sleep(1)
        driver.find_element_by_id("licenseIV").click()
        appdef.xuantu()
        time.sleep(1)
        driver.find_element_by_id("identity1IV").click()
        appdef.xuantu()
        time.sleep(1)
        driver.find_element_by_id("identity2IV").click()
        appdef.xuantu()
        time.sleep(1)
        driver.find_element_by_id("image").click()
        appdef.xuantu()
        time.sleep(1)
        driver.find_element_by_id("registerBT").click()
        time.sleep(1)
        driver.find_element_by_name("商户").click()
        driver.find_element_by_id("edit_account").send_keys(u"176888" + suijishu)
        driver.find_element_by_id("edit_pz").send_keys(u"123456")
        appdef.yzm()
        driver.find_element_by_id("tv_login").click()
        driver.find_element_by_name("我的").click()
        merchantname = driver.find_element_by_id("merchant_nameTV").text
        merchantphone = driver.find_element_by_id("merchant_accountTV").text
        self.assertEqual(u"自动商户" + suijishu,merchantname)
        self.assertEqual(u"176888" + suijishu,merchantphone)
        if u"自动商户" + suijishu == merchantname and u"176888" + suijishu and merchantphone:
            logger(u"商户注册成功，流程继续")
        else:
            logger(u"商户注册失败，流程中断")
    def test_user_shop_002(self):
        '使用商户角色查询该批发商并检查商品显示。预期结果：正常搜索到批发商，并正确显示商品'
        driver = appdef.driver
        driver.find_element_by_name("批发商").click()
        driver.find_element_by_id("wholesalers_searchET").click()
        driver.find_element_by_id("wholesalerss_searchET").send_keys(suijishu)
        driver.find_element_by_id("wholesalerss_gosearchTV").click()
        wholesalername = driver.find_element_by_id("wholesalersi_name").text
        readytime = driver.find_element_by_id("wholesalersi_stockup_time").text
        self.assertEqual(u"自动批发商" + suijishu,wholesalername)
        self.assertEqual(u"2小时",readytime)
        if u"自动批发商" + suijishu == wholesalername and u"2小时" == readytime:
            driver.find_element_by_id("wholesalersi_name").click()
            wholesalername1 = driver.find_element_by_id("supplierNameTV").text
            productname = driver.find_element_by_id("productNameTV").text
            price = driver.find_element_by_id("priceTV").text
            productfenlei = driver.find_elements_by_id("categoryName")[1].text
            qipimoney = driver.find_element_by_id("mustMoneyTV").text
            chamoney = driver.find_element_by_id("distanceMoneyTV").text
            productCount = driver.find_element_by_id("productCountTV").text
            add = driver.find_elements_by_id("cutDownIV")
            self.assertEqual(u"自动批发商" + suijishu,wholesalername1)
            self.assertEqual(u"自动商品" + str(int(suijishu)+1),productname)
            self.assertEqual(u"自动分类" + suijishu, productfenlei)
            self.assertEqual(u"￥150.00/件",price)
            self.assertEqual(u"距起批金额 ￥100.00",qipimoney)
            self.assertEqual(u"差 ￥100.00",chamoney)
            self.assertEqual(u"0",productCount)
            self.assertEqual(0,len(add))
            if u"自动商品" + str(int(suijishu)+1) == productname:
                logger(u"批发商店铺中的商品显示正确，流程继续")
            else:
                logger(u"批发商店铺中的商品显示错误，流程中断")
    def test_user_shop_003(self):
        '商户在批发商店铺中进行选择商品校验。预期结果：商品信息显示正确，合计、起批金额和选择的商品数量*价格匹配'
        driver = appdef.driver
        driver.find_element_by_id("addIV").click()
        productCount1 = driver.find_element_by_id("productCountTV").text
        add1 = driver.find_elements_by_id("cutDownIV")
        self.assertEqual(u"1",productCount1)
        self.assertEqual(1,len(add1))
        driver.find_element_by_id("addIV").click()
        time.sleep(1)
        driver.find_element_by_id("addIV").click()
        time.sleep(1)
        productCount2 = driver.find_element_by_id("productCountTV").text
        self.assertEqual(u"3",productCount2)
        driver.find_element_by_id("addIV").click()
        productCount3 = driver.find_element_by_id("productCountTV").text
        self.assertEqual(u"3", productCount3)                          #超过限购数量
        hejimoney = driver.find_element_by_id("totalMoneyTV").text
        chamoney1 = driver.find_element_by_id("distanceMoneyTV").text
        self.assertEqual(u"合计 : ￥450.00",hejimoney)
        self.assertEqual(u"差 ￥0.00",chamoney1)
        logger(u"商户可以在批发商店铺中做系列操作，流程继续")
    def test_user_shop_004(self):
        '商户选择商品后，检查购物车数据同步。预期结果：购物车数据和店铺中的数据同步'
        driver = appdef.driver
        driver.find_element_by_id("carIV").click()
        time.sleep(1)
        productselect = driver.find_element_by_id("selectedCountTV").text
        productname = driver.find_element_by_id("productNameTV").text
        productprice = driver.find_element_by_id("priceTV").text
        productcount = driver.find_element_by_id("productCountTV").text
        prouctheji = driver.find_element_by_id("totalMoneyTV").text
        self.assertIn(u"已选1件",productselect)
        self.assertIn(u"自动商品" + str(int(suijishu)+1),productname)
        self.assertIn(u"￥150.00",productprice)
        self.assertEqual(u"3",productcount)
        self.assertEqual(u"合计 : ￥450.00",prouctheji)
        driver.find_element_by_id("cutDownIV").click()
        prouctheji1 = driver.find_element_by_id("totalMoneyTV").text
        self.assertEqual(u"合计 : ￥300.00", prouctheji1)
        driver.keyevent(4)
        productcount1 = driver.find_element_by_id("productCountTV").text
        self.assertEqual(u"2",productcount1)
    def test_user_shop_005(self):
        '商户选择商品后，检查店内搜索数据同步。预期结果：搜索结果和店铺中的数据同步'
        driver = appdef.driver
        driver.find_element_by_id("wholesalers_searchET").click()
        driver.find_element_by_id("wholesalerss_searchET").send_keys(str(int(suijishu)+1))
        driver.find_element_by_id("wholesalerss_gosearchTV").click()
        wholesalername = driver.find_element_by_id("supplierNameTV").text
        productname = driver.find_element_by_id("prodcutNameTV").text
        productprice = driver.find_element_by_id("prodcutPriceTV").text
        productcount = driver.find_element_by_id("productCountTV").text
        productheji = driver.find_element_by_id("totalMoneyTV").text
        self.assertEqual(u"自动批发商" + suijishu,wholesalername)
        self.assertIn(u"自动商品" + str(int(suijishu)+1),productname)
        self.assertEqual(u"150.00/件",productprice)
        self.assertEqual(u"2",productcount)
        self.assertEqual(u"合计 : ￥300.00",productheji)
        driver.find_element_by_id("addIV").click()
        driver.find_element_by_id("backIV").click()
        productcount1 = driver.find_element_by_id("productCountTV").text
        self.assertEqual(u"3",productcount1)
    def test_user_collect(self):
        '商户收藏/取消收藏批发商。预期结果：在首页我的收藏显示/不显示该店铺'
        driver = appdef.driver
        driver.find_element_by_id("collectIV").click()
        driver.implicitly_wait(2)
        driver.find_element_by_id("backIV").click()
        driver.find_element_by_id("wholesalerss_backIV").click()
        driver.find_element_by_name("首页").click()
        driver.find_element_by_name("我的收藏").click()
        wholesalername = driver.find_element_by_id("home_child_name").text
        self.assertEqual(u"自动批发商" + suijishu,wholesalername)
        driver.find_element_by_id("home_child_name").click()
        driver.find_element_by_id("collectIV").click()
        driver.find_element_by_id("backIV").click()
        appdef.swipeDown(1000)
        time.sleep(2)
        appdef.swipeDown(1000)
        wholesalername1 = driver.find_elements_by_id("home_child_name")
        self.assertEqual(0,len(wholesalername1))
    def test_user_order_001(self):
        '商户进入批发商店铺，选择商品下单。预期结果：可正常创建订单'
        driver = appdef.driver
        driver.find_element_by_name("批发商").click()
        driver.find_element_by_id("wholesalers_searchET").click()
        driver.find_element_by_id("wholesalerss_searchET").send_keys(suijishu)
        driver.find_element_by_id("wholesalerss_gosearchTV").click()
        driver.find_element_by_id("wholesalersi_name").click()
        driver.find_element_by_id("hopeDeliverTimeTV").click()
        appdef.swipeclickdate(1000)
        driver.find_element_by_id("confireBtn").click()
        driver.find_element_by_id("createOrderTV").click()
        datetime = driver.find_elements_by_id("determine")
        if len(datetime) == 1:
            driver.find_element_by_id("determine").click()
        suppliername = driver.find_element_by_id("supplierNameTV").text
        ordermoney = driver.find_element_by_id("orderTotalMoneyTV").text
        paymoney = driver.find_element_by_id("payDepositMoneyTV").text
        self.assertEqual(u"自动批发商" + suijishu,suppliername)
        self.assertEqual(u"订单总金额:￥450.00",ordermoney)
        self.assertEqual(u"￥90.00",paymoney)
    def test_user_order_002(self):
        '商户创建订单后，应收到系统消息。预期结果：可正常收到催付订单订金的系统消息'
        driver = appdef.driver
        driver.find_element_by_name("消息").click()
        messagetitle = driver.find_element_by_id("notifyContentTV").text
        sysmessageicon = driver.find_elements_by_id("notifyTagTV")
        self.assertEqual(u"支付订金",messagetitle)
        self.assertEqual(1,len(sysmessageicon))
        driver.find_element_by_id("notifyContentTV").click()
        messagemainbody = appdef.xiaoxi(1,"支付订金","订单已提交，请尽快付订金。")
        self.assertEqual("收到推送消息",messagemainbody)
        driver.find_element_by_id("titlebar_img_back").click()
        sysmessageicon1 = driver.find_elements_by_id("notifyTagTV")
        self.assertEqual(0, len(sysmessageicon1))
    def test_user_order_003(self):
        '商户对订单进行去店铺修改操作。预期结果：可正常修改订单'
        driver = appdef.driver
        driver.find_element_by_name("结算中心").click()
        driver.find_element_by_id("updateOrderTV").click()
        driver.find_element_by_id("cutDownIV").click()
        driver.find_element_by_id("carIV").click()
        productcount = driver.find_element_by_id("productCountTV").text
        orderstauts = driver.find_element_by_id("createOrderTV").text
        self.assertEqual(u"2",productcount)
        self.assertEqual(u"更新订单",orderstauts)
        driver.find_element_by_id("createOrderTV").click()
        datetime = driver.find_elements_by_id("determine")
        if len(datetime) == 1:
            driver.find_element_by_id("determine").click()
        ordermoney = driver.find_element_by_id("orderTotalMoneyTV").text
        paymoney = driver.find_element_by_id("payDepositMoneyTV").text
        self.assertEqual(u"订单总金额:￥300.00",ordermoney)
        self.assertEqual(u"￥60.00",paymoney)
    def test_user_order_004(self):
        '商户在待付订金时，取消订单。预期结果：可正常取消订单，订单移至交易记录-全部列表中。状态为交易关闭'
        driver = appdef.driver
        driver.find_element_by_id("cancelOrderTV").click()
        suppliername = driver.find_elements_by_id("supplierNameTV")
        self.assertEqual(0,len(suppliername))
        driver.find_element_by_name("我的").click()
        driver.find_element_by_id("merchant_lookall").click()
        driver.find_element_by_name("全部").click()
        suppliername1 = driver.find_element_by_id("supplierNameTV").text
        orderstauts = driver.find_element_by_id("transactionRecordStutasTV").text
        quanxian = driver.find_elements_by_name("联系TA")
        quanxian1 = driver.find_elements_by_name("查看详情")
        quanxian2 = driver.find_elements_by_name("再次下单")
        self.assertEqual(u"自动批发商" + suijishu,suppliername1)
        self.assertEqual(u"商户取消",orderstauts)
        self.assertEqual(1,len(quanxian))
        self.assertEqual(1,len(quanxian1))
        self.assertEqual(1,len(quanxian2))
    def test_user_order_005(self):
        '交易关闭状态的订单，查看订单。预期结果：可正常查看订单'
        driver = appdef.driver
        driver.find_element_by_id("showTransactionProductTV").click()
        title = driver.find_element_by_id("dialogTitleTV").text
        productname = driver.find_element_by_id("prodcutNameTV").text
        productprice = driver.find_element_by_id("prodcutPriceTV").text
        productnum = driver.find_element_by_id("prodcutNumTV").text
        self.assertEqual(u"查看详情",title)
        self.assertEqual(u"自动商品" + str(int(suijishu)+1),productname)
        self.assertEqual(u"￥150.00",productprice)
        self.assertEqual(u"x2",productnum)
        driver.find_element_by_id("cancelIV").click()
    def test_user_message_001(self):
        '交易关闭状态的订单，点击联系TA。预期结果：能正常发送信息，批发商能正常收到消息和阅读消息'
        driver = appdef.driver
        driver.find_element_by_id("contactTATV").click()
        messagetitle = driver.find_element_by_id("titlebar_text").text
        self.assertEqual(u"自动批发商"+suijishu,messagetitle)
        driver.find_element_by_id("rc_edit_text").send_keys(u"自动文字消息：来自自动商户"+suijishu + u",发送给自动批发商" + suijishu )
        driver.find_element_by_id("rc_send_toggle").click()
        text = driver.find_elements_by_id("text1")
        self.assertEqual(1,len(text))
        self.assertEqual(u"自动文字消息：来自自动商户"+suijishu + u",发送给自动批发商" + suijishu,text[0].text)
        driver.find_element_by_id("titlebar_img_back").click()
        time.sleep(1)
        driver.find_element_by_id("titlebar_img_back").click()
        driver.find_element_by_id("merchant_settingMIV").click()
        driver.find_element_by_id("loginOutLL").click()
        driver.find_element_by_name("批发商").click()
        driver.find_element_by_id("edit_account").send_keys(u"176230" + suijishu)
        driver.find_element_by_id("edit_pz").send_keys(u"123456")
        appdef.yzm()
        driver.find_element_by_id("tv_login").click()
        red = driver.find_elements_by_id("rtv_msg_tip")
        self.assertEqual(1,len(red))
        driver.find_element_by_name("消息").click()
        icon = driver.find_elements_by_id("rc_unread_message_icon")
        messagecount = driver.find_element_by_id("rc_unread_message").text
        wholesaler = driver.find_element_by_id("rc_conversation_title").text
        message = driver.find_element_by_id("rc_conversation_content").text
        self.assertEqual(1,len(icon))
        self.assertEqual(u"1",messagecount)
        self.assertEqual(u"自动商户" + suijishu,wholesaler)
        self.assertIn(message,u"自动文字消息：来自自动商户"+suijishu + u",发送给自动批发商" + suijishu)
        driver.find_element_by_id("rc_conversation_title").click()
        messagetitle1 = driver.find_element_by_id("titlebar_text").text
        messagetext = driver.find_elements_by_id("text1")
        self.assertEqual(1,len(messagetext))
        self.assertEqual(u"自动批发商" + suijishu,messagetitle1)
        self.assertEqual(u"自动文字消息：来自自动商户"+suijishu + u",发送给自动批发商" + suijishu,messagetext[0].text)
        driver.find_element_by_id("titlebar_img_back").click()
        red1 = driver.find_elements_by_id("rtv_msg_tip")
        self.assertEqual(0, len(red1))
        icon1 = driver.find_elements_by_id("rc_unread_message_icon")
        self.assertEqual(0, len(icon1))              #消息已读后，红点消失
    def test_user_message_002(self):
        '批发商收到消息后，可以给商户回复消息。预期结果：可正常回复消息，商户可以收到消息和阅读消息'
        driver = appdef.driver
        driver.find_element_by_id("rc_conversation_title").click()
        driver.find_element_by_id("rc_edit_text").send_keys(u"自动文字消息：来自自动批发商"+suijishu + u",发送给自动商户" + suijishu)
        driver.find_element_by_id("titlebar_img_back").click()
        driver.find_element_by_name("我的").click()
        driver.find_element_by_id("merchant_settingMIV").click()
        driver.find_element_by_id("loginOutLL").click()
        driver.find_element_by_name("商户").click()
        driver.find_element_by_id("edit_account").send_keys(u"176888" + suijishu)
        driver.find_element_by_id("edit_pz").send_keys(u"123456")
        appdef.yzm()
        driver.find_element_by_id("tv_login").click()
        driver.find_element_by_name("消息").click()
        messageicon = driver.find_elements_by_id("rc_unread_message_icon")
        messagecount = driver.find_element_by_id("rc_unread_message").text
        messagetitle = driver.find_element_by_id("rc_conversation_title").text
        messagebody = driver.find_element_by_id("rc_conversation_content").text
        self.assertEqual(1,len(messageicon))
        self.assertEqual(u"1",messagecount)
        self.assertEqual(u"自动商户" + suijishu,messagetitle)
        self.assertIn(messagebody,u"自动文字消息：来自自动商户"+suijishu + u",发送给自动批发商" + suijishu)
        driver.find_element_by_id("rc_conversation_title").click()
        messagebody1 = driver.find_elements_by_id("text1")
        self.assertEqual(2,len(messagebody1))
        self.assertEqual(u"自动文字消息：来自自动商户"+suijishu + u",发送给自动批发商" + suijishu,messagebody1[1].text)
        driver.find_element_by_id("titlebar_img_back").click()
        red1 = driver.find_elements_by_id("rtv_msg_tip")
        self.assertEqual(0, len(red1))
        icon1 = driver.find_elements_by_id("rc_unread_message_icon")
        self.assertEqual(0, len(icon1))  # 消息已读后，红点消失
    def test_user_order_006(self):
        '交易关闭状态的订单，点击再次下单。预期结果：能再次生成同样的订单'
        driver = appdef.driver
        driver.find_element_by_name("我的").click()
        driver.find_element_by_id("merchant_lookall").click()
        driver.find_element_by_name("全部").click()
        driver.find_element_by_id("reCreateOrderTV").click()
        productcount = driver.find_element_by_id("productCountTV").text
        self.assertEqual(u"2",productcount)
        driver.find_element_by_id("carIV").click()
        productcount1 = driver.find_element_by_id("productCountTV").text
        self.assertEqual(u"2", productcount1)
        driver.find_element_by_id("cleanChoosedTV").click()             #清空选择的数量
        driver.keyevent(4)
        productcount2 = driver.find_element_by_id("productCountTV").text
        self.assertEqual(u"0",productcount2)
        driver.find_element_by_id("addIV").click()
        time.sleep(1)
        driver.find_element_by_id("addIV").click()
        driver.find_element_by_id("createOrderTV").click()
        datetime = driver.find_elements_by_id("determine")
        if len(datetime) == 1:
            driver.find_element_by_id("determine").click()
        driver.find_element_by_id("titlebar_img_back").click()
        hejimoney = driver.find_element_by_id("payTotalMoneyTV").text
        self.assertEqual(u"￥0.00",hejimoney)
        driver.find_element_by_id("checkOrderFlagIV").click()                       #勾选订单
        hejimoney1 = driver.find_element_by_id("payTotalMoneyTV").text
        self.assertEqual(u"￥60.00", hejimoney1)
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Dingdan_app("test_register_wholesaler"))
    suite.addTest(Dingdan_app("test_wholesaler_login"))
    suite.addTest(Dingdan_app("test_wholesaler_setting_shop"))
    suite.addTest(Dingdan_app("test_wholesaler_setting_fenlei"))
    suite.addTest(Dingdan_app("test_wholesaler_setting_product"))
    suite.addTest(Dingdan_app("test_web_reviewproduct"))
    suite.addTest(Dingdan_app("test_wholesaler_setting_product_001"))
    suite.addTest(Dingdan_app("test_wholesaler_setting_product_002"))
    suite.addTest(Dingdan_app("test_wholesaler_setting_product_003"))
    suite.addTest(Dingdan_app("test_wholesaler_setting_product_004"))
    suite.addTest(Dingdan_app("test_user_shop_001"))
    suite.addTest(Dingdan_app("test_user_shop_002"))
    suite.addTest(Dingdan_app("test_user_shop_003"))
    suite.addTest(Dingdan_app("test_user_shop_004"))
    suite.addTest(Dingdan_app("test_user_shop_005"))
    suite.addTest(Dingdan_app("test_user_collect"))
    suite.addTest(Dingdan_app("test_user_order_001"))
    suite.addTest(Dingdan_app("test_user_order_002"))
    suite.addTest(Dingdan_app("test_user_order_003"))
    suite.addTest(Dingdan_app("test_user_order_004"))
    suite.addTest(Dingdan_app("test_user_order_005"))
    suite.addTest(Dingdan_app("test_user_message_001"))
    suite.addTest(Dingdan_app("test_user_message_002"))
    suite.addTest(Dingdan_app("test_user_order_006"))
    fp = open(u"订单主流程.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'集鲜丰自动化测试报告', description=u'APP_订单主流程 — 测试结果：',
                                           tester=u'易耀通技术部测试组')
    runner.run(suite)
    fp.close()


