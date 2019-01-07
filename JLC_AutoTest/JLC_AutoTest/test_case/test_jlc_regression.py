from JLC_AutoTest.model.appunit import AppTest
from JLC_AutoTest.common.logger import Log
from JLC_AutoTest.page.page_object.login_page import LoginPage
from JLC_AutoTest.page.page_object.home_page import HomePage
from JLC_AutoTest.page.page_object.plan_page import PlanPage
from JLC_AutoTest.page.page_object.my_page import MyPage
import unittest
from time import sleep
from JLC_AutoTest.model.utils import JianlcTools
from macaca import WebDriver
import time



class Test_JLC_Regression(AppTest):

    log = Log()
    # def test_00_enterApp(self):
    #     pass


    def test_01_login(self):
        sleep(3)
        self.log.info("-------------------登录测试：start!--------------------")
        try:
            login_po = LoginPage(self.driver)

            print (login_po)

            # 点击[注册/登录]按钮
            self.log.info("点击[注册/登录]按钮")
            login_po.click_login_button()
            time.sleep(1)

            self.log.info("校验title是否显示'填写手机号'")
            title=login_po.get_full_phone_number_text()
            self.assertEqual('填写手机号', title)
            self.log.info("title是填写手机号")
            time.sleep(1)

            self.log.info("校验是否显示返回按钮")
            self.assertIsNotNone(login_po.full_phone_fanhui_button())
            self.log.info("显示返回按钮的元素")
            time.sleep(2)

            self.log.info("验证填写手机号输入框内的文本")
            self.assertEqual('请输入手机号注册或登录',login_po.get_full_phone_num_edit_text_loc())
            self.log.info("显示为请输入手机号注册或登录")
            time.sleep(2)

            self.log.info("校验是否显示平台服务协议")
            self.assertEqual("《简理财平台服务协议》",login_po.get_full_ptfwxy_text_loc())
            self.log.info("显示平台服务协议")
            time.sleep(2)

            self.log.info("是否显示简理财隐私条款")
            self.assertIsNotNone(login_po.get_full_jlcystk_text_loc())
            self.log.info("显示隐私条款元素")
            time.sleep(2)

            self.log.info("是否显示微信登录")
            self.assertIsNotNone(login_po.get_full_weixin_loc())
            self.log.info("显示微信图标")
            time.sleep(2)

            self.log.info("是否显示底部图片")
            self.assertIsNotNone(login_po.get_full_dbutton_loc())
            self.log.info("显示底部图片")
            time.sleep(2)

            # 输入用户手机号码
            self.log.info("校验填写手机号")
            phone_number = JianlcTools.createphones(self)
            self.log.info("输入用户手机号码: %s" % phone_number)
            login_po.input_user_phone(phone_number)
            time.sleep(2)

            # 点击[下一步]按钮
            self.log.info("点击[下一步]按钮")
            login_po.click_next_button()

            # 输入验证码, 验证码:123456
            time.sleep(3)
            self.log.info("输入验证码：123456")
            login_po.input_validate_code()


            # 第一次设置手势解锁码
            self.log.info("第一次设置手机解锁码")
            login_po.gesture_password()
            # 第二次设置手势解锁码
            self.log.info("第二次设置手机解锁码")
            login_po.gesture_password()
        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("-------------------登录测试：end!--------------------")
    def test_02_bank_card(self):
        pass
        # self.log.info("-------------绑卡测试：start!-------------------")
        # try:
        #     # bankcard_po=BankCard(self.driver)

    '''def test_02_buy(self):
        self.log.info("-------------------买入测试：start!--------------------")
        try:
            home_po = HomePage(self.driver)

            self.assertEqual(home_po.get_text_assets(), "总资产")
            self.assertEqual(home_po.get_text_profit(), "累计收益")
            # 点击[买入]按钮
            self.log.info("点击[买入]按钮")
            home_po.click_buy_button()
            home_po.click_buy_button()
            # 输入买入的金额, 金额：100
            self.log.info("输入买入的金额, 金额：100")
            home_po.input_in_money(100)
            # 点击[立即买入]按钮
            self.log.info("点击[立即买入]按钮")
            home_po.click_in_confirm_money_button()
            # 输入支付密码
            self.log.info("输入支付密码")
            sleep(2)
            home_po.input_password()
            # 点击买入[完成]按钮
            self.log.info("点击买入[完成]按钮")
            home_po.click_in_complete_button()
        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("-------------------买入测试：end!--------------------")

    def test_03_draw(self):
        self.log.info("-------------------转出测试：start!--------------------")
        try:
            home_po = HomePage(self.driver)
            # 点击[转出]按钮
            self.log.info("点击[转出]按钮")
            home_po.click_draw_button()
            # 输入转出金额， 金额100
            self.log.info("输入转出金额， 金额100")
            home_po.input_draw_money(100)
            # 点击[确认转出]按钮
            self.log.info("点击[确认转出]按钮")
            home_po.click_draw_confirm_money_button()
            # 输入支付密码
            self.log.info("输入支付密码")
            sleep(2)
            home_po.input_password()
            # 点击[x]
            self.log.info("点击[x]")
            home_po.click_remark_close_button()
            # 点击转出[完成]按钮
            self.log.info("点击转出[完成]按钮")
            home_po.click_draw_complete_button()
        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("-------------------转出测试：end!--------------------")

    def test_04_dream_plan(self):
        self.log.info("-------------------梦想计划测试：start!--------------------")
        try:
            plan_po = PlanPage(self.driver)
            self.log.info("-------------------添加/开启梦想计划--------------------")
            # 点击[计划]图标
            self.log.info("点击[计划]图标")
            plan_po.click_plan_tab()
            # 点击[梦想计划]
            self.log.info("点击[梦想计划]")
            plan_po.click_dream_plan_img()
            # 选择梦想计划
            self.log.info("选择梦想计划")
            plan_po.click_select_dream_plan()
            # 点击[下一步]按钮
            self.log.info("点击[下一步]按钮")
            plan_po.click_next_button()
            # 点击[自动开启梦想]
            self.log.info("点击[自动开启梦想]")
            plan_po.click_auto_dream_button()
            sleep(2)
            # 点击[确定]按钮
            self.log.info("点击[确定]按钮")
            plan_po.click_confirm_button()
            # 输入支付密码
            self.log.info("输入支付密码")
            sleep(2)
            plan_po.input_password()
            # 点击[完成]按钮
            self.log.info("点击[完成]按钮")
            plan_po.click_complete_button()
            self.log.info("-------------------梦想计划终止--------------------")
            # 点击梦想计划菜单
            self.log.info("点击梦想计划菜单")
            plan_po.click_dream_plan_menu()
            # 点击梦想计划[终止计划]
            self.log.info("点击梦想计划[终止计划]")
            plan_po.click_stop_dream_plan()
            # 点击确认梦想计划[残忍终止]
            self.log.info("点击确认梦想计划[残忍终止]")
            plan_po.click_confirm_stop_dream()
            # 输入支付密码
            self.log.info("输入支付密码")
            sleep(2)
            plan_po.input_password()
            # 点击梦想计划终止[完成]
            self.log.info("点击梦想计划终止[完成]")
            plan_po.click_stop_dream_plan_complete_button()
        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("-------------------梦想计划测试：end!--------------------")

    def test_05_rent_plan(self):
        self.log.info("-------------------房租房贷计划测试：start!--------------------")
        try:
            my_po = MyPage(self.driver)
            self.log.info('-------------------添加/开启房屋房贷计划---------------------')
            # 点击[我的]图标
            self.log.info("点击[我的]图标")
            my_po.click_my()
            # 点击[房屋房贷]图标
            self.log.info("点击[房屋房贷]图标")
            my_po.click_rent_plan()
            # 点击[开启房租房贷计划]
            self.log.info("点击[开启房租房贷计划]")
            my_po.click_start_rent_plan()
            # 点击交房租金额[下一步]按钮
            self.log.info("点击交房租金额[下一步]按钮")
            my_po.click_money_next_button()
            # 点击交房租周期[下一步]
            self.log.info("点击交房租周期[下一步]")
            my_po.click_rent_cycle_next_button()
            # 点击[开始自动交房租]按钮
            self.log.info("点击[开始自动交房租]按钮")
            my_po.click_monthday_next_button()
            # 输入支付密码
            self.log.info("输入支付密码：123456")
            my_po.input_password()
            # 点击[完成]按钮
            self.log.info("点击交房租设置[完成]按钮")
            my_po.click_confirm_button()
            self.log.info('-------------------终止房屋房贷计划---------------------')
            # 点击已存在的"交房租计划"
            self.log.info('点击已存在的"交房租计划"')
            my_po.click_selected_rent_plan()
            # 点击房租房贷计划菜单
            self.log.info("点击房租房贷计划菜单")
            my_po.click_rent_plan_menu()
            # 点击房屋房贷[终止计划]
            self.log.info("点击房屋房贷[终止计划]")
            my_po.click_stop_rent_plan()
            # 点击房屋房贷[确认终止]
            self.log.info("点击房屋房贷[确认终止]")
            my_po.click_confirm_stop_rent_plan()
            # 输入支付密码
            self.log.info("输入支付密码：123456")
            my_po.input_password()
            # 点击房屋房贷终止计划[完成]按钮
            self.log.info("点击房屋房贷终止计划[完成]按钮")
            my_po.click_stop_rent_plan_complete_button()
        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("-------------------房租房贷计划测试：end!--------------------")

    def test_06_salary_plan(self):
        self.log.info("-------------------工资计划测试：start!--------------------")
        try:
            my_po = MyPage(self.driver)
            self.log.info("------------添加/开启工资计划---------------")
            # 点击[我的]图标
            self.log.info("点击[我的]图标")
            my_po.click_my()
            # 点击[存工资]图标
            self.log.info("点击[存工资]图标")
            my_po.click_salary_plan()
            # 点击存入金额[下一步]按钮
            self.log.info("点击存入金额[下一步]按钮")
            my_po.click_salary_next_butto()
            # 点击[加入工资计划]按钮
            self.log.info("点击[加入工资计划]按钮")
            my_po.click_join_salary_plan_button()
            # 输入支付密码
            self.log.info("输入支付密码：123456")
            my_po.input_password()
            # 点击[我知道了]
            self.log.info("点击[我知道了]")
            my_po.click_dialog_sure()
            self.log.info("-------------------终止工资计划----------------------")
            # 点击工资计划菜单
            self.log.info("点击工资计划菜单")
            my_po.click_salary_plan_menu().click()
            # 点击[终止计划]
            self.log.info("点击[终止计划]")
            my_po.click_stop_salary_plan()
            # 点击"确定终止"
            self.log.info("点击'确定终止'")
            my_po.click_confirm_stop_salary_plan()
            # 输入支付密码
            self.log.info("输入支付密码：123456")
            my_po.input_password()
            #  点击终止工资计划[完成]按钮
            self.log.info(" 点击终止工资计划[完成]按钮")
            my_po.click_stop_salary_plan_complete_button()
        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("-------------------工资计划测试：end!--------------------")

    def test_07_credit_card(self):
        self.log.info("-------------------信用卡还款测试：start!--------------------")
        self.log.info("-------------------信用卡还款测试：end!--------------------")

    def test_08_change_message(self):
        self.log.info("-------------------修改手机号码、修改支付密码、找回支付密码测试：start!--------------------")
        self.log.info("-------------------修改手机号码、修改支付密码、找回支付密码测试：end!--------------------")
'''

if __name__ == '__main__':
    unittest.main()
