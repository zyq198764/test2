from JLC_AutoTest.model.appunit import AppTest
from JLC_AutoTest.common.logger import Log
from JLC_AutoTest.page.page_object.Unlogin_home_page import UnloginHomePage
import unittest
import  time

#测试点击引导页


class Test_JLC_Regression(AppTest):

    log = Log()


    def test_01_Unlogin_home_page(self):

        self.log.info("-------------------点击引导页测试：start!--------------------")
        try:
            #time.sleep(10)
            # html = self.driver.source
            # print (html)
            Boot_page_po = UnloginHomePage(self.driver)
            #time.sleep(10)

            # self.driver \
            #     .touch('drag', {
            #     'fromX': 300,
            #     'fromY': 200,
            #     'toX': 50,
            #     'toY': 50,
            #     'steps': 100
            # })
            # time.sleep(2)
            # self.driver \
            #     .touch('drag', {
            #     'fromX': 300,
            #     'fromY': 200,
            #     'toX': 50,
            #     'toY': 50,
            #     'steps': 100
            # })
            # time.sleep(2)
            # self.driver \
            #     .touch('drag', {
            #     'fromX': 300,
            #     'fromY': 200,
            #     'toX': 50,
            #     'toY': 50,
            #     'steps': 100
            # })
            #
            # time.sleep(2)
            self.log.info("点击引导页进入首页")
            Boot_page_po.click_boot_page_loc()
            # 点击[注册/登录]按钮
            # time.sleep(5)



        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("-------------------引导页测试：end!--------------------")



if __name__ == '__main__':
    unittest.main()
