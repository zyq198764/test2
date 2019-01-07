from JLC_AutoTest.model.appunit import AppTest
from JLC_AutoTest.common.logger import Log
# from JLC_AutoTest.page.page_object.Unlogin_home_page_01 import UnloginHomePage01
from JLC_AutoTest.page.page_object.home_page import HomePage
from JLC_AutoTest.page.page_object.plan_page import PlanPage
from JLC_AutoTest.page.page_object.my_page import MyPage
import unittest
from time import sleep



class Test_Unlogin_home_page(AppTest):

    log = Log()


    def test_01_Unlogin_home_page(self):


    # try:
        # login_po = UnloginHomePage01(self.driver)
        # print(login_po)
        sleep(20)

        # 点击[注册/登录]按钮
        # self.log.info("点击[注册/登录]按钮")
        # login_po.click_Unlogin_banner_button()
        # 输入用户手机号码
        #phone_number = 15929898888

        #self.assertEqual(login_po.get_full_phone_number_text(), '填写手机号')
        #self.log.info("输入用户手机号码: %s" % phone_number)
        #login_po.input_user_phone(phone_number)
        # 点击[下一步]按钮
        #self.log.info("点击[下一步]按钮")
        #login_po.click_next_button()
        # 输入验证码, 验证码:123456
        #self.log.info("输入验证码：123456")
        #self.assertEqual(login_po.get_full_validate_code_text(), '输入验证码')
        #login_po.input_validate_code()
        # 第一次设置手势解锁码
        #self.log.info("第一次设置手机解锁码")
        #login_po.gesture_password()
        # 第二次设置手势解锁码
        #self.log.info("第二次设置手机解锁码")
        #login_po.gesture_password()
    # except Exception as msg:
      # self.log.info("异常信息：%s" % msg)
    # self.log.info("-------------------登录测试：end!--------------------")

if __name__ == '__main__':
    unittest.main()