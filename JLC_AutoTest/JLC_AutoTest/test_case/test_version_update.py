from JLC_AutoTest.model.appunit import AppTest
from JLC_AutoTest.common.logger import Log
from JLC_AutoTest.page.page_object.version_update_page import VersionUpdatePage
import unittest
import time
from JLC_AutoTest.model.utils import OpMysql,delete_redis


import JLC_AutoTest.globalvar
from macaca import WebDriver
from JLC_AutoTest.model.appunit1 import MacacaTest
from JLC_AutoTest.model.appunit_android import MacacaTest_android
from retrying import retry
# from JLC_AutoTest.model.BasePage1 import  BasePage


opmysql = OpMysql(host='10.103.27.10', users='root', password='123123', port=3306, db='test3_product')  #连接数据库

class Test_JLC_Version(AppTest):


    log = Log()


 #iosVIP3.9.7版本的的升级操作

    '''def test_Ver_Update(self): #无需版本更新，是最新版本
        time.sleep(10)
        self.log.info("-------------------版本更新测试：start!--------------------")
        # 先删除vip版本在redis中的值validValue、
        delete_redis(self)

        try:
            verUpdate = VersionUpdatePage(self.driver)
            print (verUpdate)
            #获取数据库中的validValue
            version=opmysql.op_db_select("SELECT validValue FROM app_version_manager  WHERE  mobileType=4  AND  `name`='versionUpdateType' AND envType=1")[0][0]
            print(version)

            ##修改validValue的值为0，属于无需版本更新的
            validValue=opmysql.op_db_update("UPDATE app_version_manager SET   validValue='0'  , note='0:表示未知，不做任何操作1:表示是选择更新2:表示强制更新' , yn=1  WHERE  mobileType=4  AND  `name`='versionUpdateType' AND envType=1 AND validValue=%s" %(version))
            print(validValue)
            print(type(validValue))

            time.sleep(5)

            self.log.info('开始进入到App')

            # self.log.info('开始点击是否允许发送通知中的允许按钮')
            # # verUpdate.click_boot_page_button()
            # verUpdate.click_boot_page_button()
            # self.log.info('已经点允许按钮，弹层消失')
            time.sleep(3)

            
            # 向左滑动四次屏幕
            
            for i in range(4):
                # el=self.driver.element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]')
                verUpdate.swipe_left(steps=5)
                # verUpdate.left_swipe(driver=self.driver)
                # verUpdate.click_boot_page_button()
                time.sleep(1)

            self.log.info('开始点击点击进入')
            verUpdate.click_unlogin_jlc_page()
            self.log.info('已经点击完成"点击进入')
            time.sleep(3)


            self.log.info("开始点击未登陆首页的空白处")
            verUpdate.click_unlogin_page()
            self.log.info("已经点击完成")
            time.sleep(5)

            self.log.info('开始进入到"我的"页面')
            verUpdate.click_my_button()
            self.log.info('已经进入到我的页面')
            time.sleep(3)


            # 进入到我的页面，向上滑，因为关于在页面底部，要不然找不到关于

            # verUpdate.swipe_up(steps=10)
            self.log.info('开始滑动页面')
            # el=self.driver.element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]')
            verUpdate.swipe_up(steps=10)
            self.log.info("已经向上滑动")
            time.sleep(3)


            self.log.info('开始点击关于')
            verUpdate.click_about_button()
            self.log.info('已经点击关于')
            time.sleep(3)

            self.log.info('开始点击版本检测')
            verUpdate.click_version_button()
            self.log.info('已经点击版本检测')
            time.sleep(3)

            self.log.info('开始进入获取版本检测弹窗中的文本')
            el=verUpdate.click_version_text_button()
            # print(el)
            # self.log.info('获取到版本检测弹窗中的文本')
            # self.assertEqual(el, '当前已是最新版本哦')
            time.sleep(3)
            self.log.info('开始点击版本检测弹窗中的确定按钮')
            verUpdate.click_version_confirm_button()
            self.log.info('已经点击完成')

            #修改数据库中的值validValue的值为1
            opmysql.op_db_update("UPDATE app_version_manager SET   validValue='1'  , note='0:表示未知，不做任何操作1:表示是选择更新2:表示强制更新' , yn=1  WHERE  mobileType=4  AND  `name`='versionUpdateType' AND envType=1 AND validValue='0'")
            validValue = opmysql.op_db_select("SELECT validValue FROM app_version_manager  WHERE  mobileType=4  AND  `name`='versionUpdateType' AND envType=1")[0][0]
            print(validValue)
        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("------------------版本更新测试：end!--------------------")

    def test_version_Update_01(self):
        #执行非强制升级
        
            # # 进入到版本检测的页面，点击版本检测，弹出版本检测非强制升级的弹层
            # 检查非强制升级的弹层的各个元素
            # 进行覆盖安装
            # 覆盖安装后，是否可以正常启动，进入到App内
            # 再去检测版本更新，提示是最新版本
            #设置validValue的值为2
        
        time.sleep(10)
        self.log.info("-------------------版本非强制更新测试：start!--------------------")
        # 先删除vip版本在redis中的值validValue、
       delete_redis(self)
        # OpMysql.op_db_update("")
        try:
            verUpdate1 = VersionUpdatePage(self.driver)
            print(verUpdate1)


                # #弹出版本检测的弹层,点击"立刻体验"
                # time.sleep(3)
                # self.log.info("开始点击立即体验")
                # verUpdate.click_version_update_Elastic_layer()
                # self.log.info("已经点击立即体验，跳转到Appstore页面")
                # time.sleep(3)
                #
                # # self.log.info("开始点击返回app")
                # # verUpdate.click_version_app_store()
                # # self.log.info("已经点击返回App，返回到App内")
                # # time.sleep(3)
                #
                # self.log.info('开始进入到"我的"页面')
                # verUpdate.click_my_button()
                # self.log.info('已经进入到我的页面')
                # time.sleep(3)
                #
                # # 进入到我的页面，向上滑一下，因为关于在页面底部，要不然找不到关于
                #
                # # verUpdate.swipe_up(self,steps=10)
                #
                # self.log.info('开始点击关于')
                # verUpdate.click_about_button()
                # self.log.info('已经点击关于')
                # time.sleep(3)
                #
                # self.log.info('开始点击版本检测')
                # verUpdate.click_version_button()
                # self.log.info('已经点击版本检测')
                # time.sleep(3)
                #
                # # self.log.info('点击版本更新中的稍后提醒')
                # # el=verUpdate.click_version_update_Remind_Me_Later()
                # # print(el)
                # # self.assertEqual(el, '或稍后提醒我')
                # # self.log.info('已经点击版本更新中的稍后提醒')

            #进行覆盖安装
            self.log.info('开始进行覆盖安装')

            MacacaTest.setUpClass()
            MacacaTest.tearDownClass()
            MacacaTest.initDriver()

            self.log.info('已经完成覆盖安装，并启动成功')

            opmysql.op_db_update(
                    "UPDATE app_version_manager SET   validValue='2'  , note='0:表示未知，不做任何操作1:表示是选择更新2:表示强制更新' , yn=1  WHERE  mobileType=4  AND  `name`='versionUpdateType' AND envType=1 AND validValue='1'")
            validValue = opmysql.op_db_select(
                    "SELECT validValue FROM app_version_manager  WHERE  mobileType=4  AND  `name`='versionUpdateType' AND envType=1")[0][0]
            print(validValue)
        except  Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("------------------版本非强制更新测试：end!--------------------")
        #重新安装

    def test_version_Update_02(self):

        #强制升级
        time.sleep(10)
        self.log.info("-------------------版本强制更新测试：start!--------------------")
        # 先删除vip版本在redis中的值validValue、
        delete_redis(self)
        try:
            verUpdate2= VersionUpdatePage(self.driver)
            print(verUpdate2)


                    # #弹出版本检测的弹层,点击"立刻体验"
                    # time.sleep(3)
                    # self.log.info("开始点击立即体验")
                    # verUpdate.click_version_update_Elastic_layer()
                    # self.log.info("已经点击立即体验，跳转到Appstore页面")
                    # time.sleep(3)
                    #

                    # 进行覆盖安装
            self.log.info('开始进行覆盖安装')

            MacacaTest.setUpClass()
            MacacaTest.tearDownClass()
            MacacaTest.initDriver()

            self.log.info('已经完成覆盖安装，并启动成功')

            # opmysql.op_db_update(
            #             "UPDATE app_version_manager SET   validValue='2'  , note='0:表示未知，不做任何操作1:表示是选择更新2:表示强制更新' , yn=1  WHERE  mobileType=4  AND  `name`='versionUpdateType' AND envType=1 AND validValue='1'")
            # validValue = opmysql.op_db_select(
            #             "SELECT validValue FROM app_version_manager  WHERE  mobileType=4  AND  `name`='versionUpdateType' AND envType=1")[0][0]
            # print(validValue)
        except  Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("------------------版本强制更新测试：end!--------------------")
    '''

  #测试Android升级
    def test_andorid_Ver_Update(self): #无需版本更新，是最新版本

        time.sleep(10)
        self.log.info("-------------------版本更新测试：start!--------------------")
        delete_redis(self)

        try:
            android_verUpdate = VersionUpdatePage(self.driver)
            print (android_verUpdate)
            # 获取数据库中的validValue
            version=opmysql.op_db_select("SELECT validValue  FROM app_version_manager WHERE mobileType=3  AND   envType=1  AND yn=1 ORDER BY  modifyTime  DESC LIMIT 1")[0][0]
            print(version)

            # 修改validValue的值为63，属于无需版本更新的，因为当前3.9.8的versionCode为63
            validValue=opmysql.op_db_update(" UPDATE app_version_manager SET   validValue='63'  WHERE  mobileType=3  AND  `name`='versionCode'  AND envType=1  AND   yn=1  AND validValue=%s" %(version))
            print(validValue)
            #
            time.sleep(5)

            self.log.info('开始进入到App')
            time.sleep(5)

            '''
            向左滑动四次屏幕
            '''
            for i in range(3):
                print('开始执行滑动')
                self.driver.touch('drag', {'fromX': 972,'fromY': 960,'toX': 200,'toY': 960,'duration': 1})
                time.sleep(1)

            time.sleep(3)
            self.driver.element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]').click()

            time.sleep(3)
            print("开始点击简理财")
            self.driver.element_by_xpath('//*[@resource-id="com.laijin.simplefinance:id/main_indicator"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
            print('已经点击完简理财')
            time.sleep(3)
            self.log.info('开始进入到"我的"页面')
            android_verUpdate.click_my_button()
            self.log.info('已经进入到我的页面')
            time.sleep(3)


            # 进入到我的页面，向上滑，因为关于在页面底部，要不然找不到关于


            self.log.info('开始滑动页面')
            self.driver.touch('drag', {'fromX': 972, 'fromY': 960, 'toX': 972, 'toY': 300, 'duration': 1})

            time.sleep(3)
            # android_verUpdate.swipe_up_android(steps=10)
            self.log.info("已经向上滑动")
            time.sleep(3)


            self.log.info('开始点击关于')
            android_verUpdate.click_about_button()
            self.log.info('已经点击关于')
            time.sleep(3)

            self.log.info('开始点击版本检测')
            android_verUpdate.click_version_button()
            self.log.info('已经点击版本检测')
            time.sleep(3)


            # #修改数据库中的值validValue的值为64
            opmysql.op_db_update(" UPDATE app_version_manager SET   validValue='64'  WHERE  mobileType=3  AND  `name`='versionCode'  AND envType=1  AND   yn=1  AND validValue='63'")
        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("------------------版本更新测试：end!--------------------")

    def test_android_version_Update_01(self):
        # 执行非强制升级

        # # 进入到版本检测的页面，点击版本检测，弹出版本检测非强制升级的弹层
        # 检查非强制升级的弹层的各个元素
        # 进行覆盖安装
        # 覆盖安装后，是否可以正常启动，进入到App内
        # 再去检测版本更新，提示是最新版本

        time.sleep(10)
        self.log.info("-------------------版本非强制更新测试：start!--------------------")
        # 先删除vip版本在redis中的值validValue、
        delete_redis.operRedis(self)
        # OpMysql.op_db_update("")
        try:
            android_verUpdate1 = VersionUpdatePage(self.driver)
            print(android_verUpdate1)

            # #弹出版本检测的弹层,点击"立刻体验"
            # time.sleep(3)
            # self.log.info("开始点击立即体验")
            # verUpdate.click_version_update_Elastic_layer()
            # self.log.info("已经点击立即体验，跳转到Appstore页面")
            # time.sleep(3)
            #
            # # self.log.info("开始点击返回app")
            # # verUpdate.click_version_app_store()
            # # self.log.info("已经点击返回App，返回到App内")
            # # time.sleep(3)
            #
            # self.log.info('开始进入到"我的"页面')
            # verUpdate.click_my_button()
            # self.log.info('已经进入到我的页面')
            # time.sleep(3)
            #
            # # 进入到我的页面，向上滑一下，因为关于在页面底部，要不然找不到关于
            #
            # # verUpdate.swipe_up(self,steps=10)
            #
            # self.log.info('开始点击关于')
            # verUpdate.click_about_button()
            # self.log.info('已经点击关于')
            # time.sleep(3)
            #
            # self.log.info('开始点击版本检测')
            # verUpdate.click_version_button()
            # self.log.info('已经点击版本检测')
            # time.sleep(3)
            #
            # # self.log.info('点击版本更新中的稍后提醒')
            # # el=verUpdate.click_version_update_Remind_Me_Later()
            # # print(el)
            # # self.assertEqual(el, '或稍后提醒我')
            # # self.log.info('已经点击版本更新中的稍后提醒')

            # 进行覆盖安装
            self.log.info('开始进行覆盖安装')

            MacacaTest_android.setUpClass()
            MacacaTest_android.tearDownClass()
            MacacaTest_android.initDriver()

            self.log.info('已经完成覆盖安装，并启动成功')
            time.sleep(3)

            print("开始点击简理财")
            self.driver.element_by_xpath('//*[@resource-id="com.laijin.simplefinance:id/main_indicator"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
            print('已经点击完简理财')
            time.sleep(3)

            self.log.info('开始进入到"我的"页面')
            android_verUpdate1.click_my_button()
            self.log.info('已经进入到我的页面')
            time.sleep(3)

            # 进入到我的页面，向上滑，因为关于在页面底部，要不然找不到关于

            self.log.info('开始滑动页面')
            self.driver.touch('drag', {'fromX': 972, 'fromY': 960, 'toX': 972, 'toY': 300, 'duration': 1})

            time.sleep(3)
            # android_verUpdate.swipe_up_android(steps=10)
            self.log.info("已经向上滑动")
            time.sleep(3)

            self.log.info('开始点击关于')
            android_verUpdate1.click_about_button()
            self.log.info('已经点击关于')
            time.sleep(3)

            self.log.info('开始点击版本检测')
            android_verUpdate1.click_version_button()
            self.log.info('已经点击版本检测')
            time.sleep(3)



            #设置强制升级

            opmysql.op_db_update(
                "UPDATE app_version_manager SET validValue='2'  WHERE mobileType=3 AND `name`='updateType'  AND envType=1 AND validValue='1'")
            # validValue = opmysql.op_db_select(
            #     "SELECT validValue FROM app_version_manager  WHERE  mobileType=4  AND  `name`='versionUpdateType' AND envType=1")[
            #     0][0]
            # print(validValue)
        except  Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("------------------版本非强制更新测试：end!--------------------")

    def test_android_version_Update_02(self):
        Test_JLC_Version.test_andorid_Ver_Update(self)

        #强制升级
        time.sleep(10)
        self.log.info("-------------------版本强制更新测试：start!--------------------")
        # 先删除vip版本在redis中的值validValue、
        delete_redis.operRedis(self)
        try:
            andorid_verUpdate2= VersionUpdatePage(self.driver)
            print(andorid_verUpdate2)


                    # #弹出版本检测的弹层,点击"立刻体验"
                    # time.sleep(3)
                    # self.log.info("开始点击立即体验")
                    # verUpdate.click_version_update_Elastic_layer()
                    # self.log.info("已经点击立即体验，跳转到Appstore页面")
                    # time.sleep(3)
                    #

                    # 进行覆盖安装

            self.log.info('开始进行覆盖安装')

            MacacaTest_android.setUpClass()
            MacacaTest_android.tearDownClass()
            MacacaTest_android.initDriver()

            self.log.info('已经完成覆盖安装，并启动成功')
            self.log.info('开始进入到"我的"页面')
            andorid_verUpdate2.click_my_button()
            self.log.info('已经进入到我的页面')
            time.sleep(3)

            # 进入到我的页面，向上滑，因为关于在页面底部，要不然找不到关于

            self.log.info('开始滑动页面')
            self.driver.touch('drag', {'fromX': 972, 'fromY': 960, 'toX': 972, 'toY': 300, 'duration': 1})

            time.sleep(3)
            # android_verUpdate.swipe_up_android(steps=10)
            self.log.info("已经向上滑动")
            time.sleep(3)

            self.log.info('开始点击关于')
            andorid_verUpdate2.click_about_button()
            self.log.info('已经点击关于')
            time.sleep(3)

            self.log.info('开始点击版本检测')
            andorid_verUpdate2.click_version_button()
            self.log.info('已经点击版本检测')
            time.sleep(3)

            # opmysql.op_db_update(
            #             "UPDATE app_version_manager SET   validValue='2'  , note='0:表示未知，不做任何操作1:表示是选择更新2:表示强制更新' , yn=1  WHERE  mobileType=4  AND  `name`='versionUpdateType' AND envType=1 AND validValue='1'")
            # validValue = opmysql.op_db_select(
            #             "SELECT validValue FROM app_version_manager  WHERE  mobileType=4  AND  `name`='versionUpdateType' AND envType=1")[0][0]
            # print(validValue)
        except  Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("------------------版本强制更新测试：end!--------------------")






if __name__ == '__main__':
    unittest.main()

