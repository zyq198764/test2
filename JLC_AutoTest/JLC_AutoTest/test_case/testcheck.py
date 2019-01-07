from JLC_AutoTest.model.appunit import AppTest
from JLC_AutoTest.common.logger import Log
from JLC_AutoTest.page.page_object.Unlogin_home_page import UnloginHomePage
from JLC_AutoTest.page.page_ui_object.Unlogin_home_page_ui import UnloginHomePageUi
# UnloginHomePageUifrom JLC_AutoTest.page.page_object.version_update_page import VersionUpdatePage
import unittest
import time
from macaca import WebDriver





class Test_JLC_Regression(AppTest):

    log = Log()


    # def test_Ver_Update(self):
    #     time.sleep(20)
    #     self.log.info("-------------------版本更新测试：start!--------------------")
    #     try:
    #         login_po = UnloginHomePage(self.driver)
    #         print (login_po)
    #
    #         login_po.enter_my_page_loc()
    #         # time.sleep(3)
    #
    #         # login_po.click_about_button()
    #         # time.sleep(3)
    #         #
    #         # login_po.click_version_button()
    #         # time.sleep(3)
    #         #
    #         # login_po.version_update_loc()
    #         # time.sleep(3)
    #         # # verUpdate.version_update_text()
    #         # # self.assertEqual(verUpdate.version_update_text(), '当前已是最新版本哦')
    #         # time.sleep(3)
    #         # login_po.version_update_confirm_loc()
    #
    #     except Exception as msg:
    #         self.log.info("异常信息：%s" % msg)
    #     self.log.info("------------------版本更新测试：end!--------------------")

    def test_Un_login(self):
        time.sleep(20)
        self.log.info("-------------------未登录首页测试：start!--------------------")
        try:
            login_po = UnloginHomePage(self.driver)
            print (login_po)
            #点击未登录首页的banner

            self.driver.touch('drag', {'fromX': 300,'fromY': 200,'toX': 50,'toY': 50,'steps': 100})
            time.sleep(2)
            self.driver.touch('drag', {'fromX': 300,'fromY': 200,'toX': 50,'toY': 50,'steps': 100})
            time.sleep(2)
            self.driver \
                .touch('drag', {
                'fromX': 300,
                'fromY': 200,
                'toX': 50,
                'toY': 50,
                'steps': 100
            })

            time.sleep(2)

            # 点击[注册/登录]按钮
            self.log.info("点击引导页进入首页")
            login_po.unlogin_button_loc()
            # 输入用户手机号码



        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("-------------------登录测试：end!--------------------")



if __name__ == '__main__':
    unittest.main()
