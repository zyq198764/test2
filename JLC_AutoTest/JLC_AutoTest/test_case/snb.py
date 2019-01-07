from JLC_AutoTest.model.appunit import AppTest
import unittest
import time
from JLC_AutoTest.common.settings import log
from JLC_AutoTest.page.page_object.snb_unlogin_page import  SNB_Unlogin_page
from JLC_AutoTest.model.base import Base
from JLC_AutoTest.page.page_object.snb_login_page import SNB_login_page
from JLC_AutoTest.page.page_object.snb_bank_card_page import SNB_bank_card_page
from JLC_AutoTest.page.page_object.snb_set_password_page import SNB_set_passwd_page
from JLC_AutoTest.page.page_object.snb_buy_page import SNB_Buy_now_page




class Test_SNB_Regression(AppTest):

    """def test_01_unlogin(self):
        time.sleep(3)
        log.info("-------------未登陆首页测试：start！-------------")
        try:
            Snb_Unlogin_po = SNB_Unlogin_page(self.driver)

            time.sleep(3)
            #以下是页面元素的校验
            log.info("获取未登陆首页的title")
            title=Snb_Unlogin_po.get_Unlogin_Title_Loc_page()
            print(title)
            self.assertEqual('拾年保',title)
            time.sleep(1)

            log.info("获取文案低风险基金组合产品")
            print(Snb_Unlogin_po.get_unlogin_lowriskfundtext_loc_page())
            self.assertEqual('低风险基金组合产品',Snb_Unlogin_po.get_unlogin_lowriskfundtext_loc_page())
            time.sleep(1)

            log.info("获取基金销售合作文案")
            print(Snb_Unlogin_po.get_unlogin_lic_fundsales_loc_page())
            self.assertEqual("与正规持牌机构奕丰金融基金销售合作",Snb_Unlogin_po.get_unlogin_lic_fundsales_loc_page())
            time.sleep(1)

            log.info("获取证书编码的文案")
            self.assertEqual("(证书编码：000000381)",Snb_Unlogin_po.get_unlogin_certicode_loc_page())
            time.sleep(1)

            log.info("获取低风险的文案")
            self.assertEqual("低风险 低手续费 500元起投",Snb_Unlogin_po.get_unlogin_midtext_loc_page())
            time.sleep(1)

            log.info("获取历史年华收益率")
            self.assertEqual("7.43%",Snb_Unlogin_po.get_unlogin_lssyltext_loc_page())
            time.sleep(1)

            log.info("获取赎回无限制的文案")
            self.assertEqual("赎回无限制",Snb_Unlogin_po.get_unlogin_reedmunlimited_loc_page())
            time.sleep(1)

            #需要执行一下向上滑动页面
            log.info('开始向上滑动页面')
            for i in range(3):
                Snb_Unlogin_po.swipe_up_new(duration=1)

            time.sleep(2)

            log.info("获取历史平均万元日收益的文案")
            self.assertEqual("历史平均万元日收益(元)",Snb_Unlogin_po.get_unlogin_Histor_loc_page())
            time.sleep(1)

            log.info("获取历史正收益天数占比的文案")
            self.assertEqual("历史正收益天数占比",Snb_Unlogin_po.get_unlogin_historicalpos_loc_page())
            time.sleep(1)

            log.info('开始向下滑动页面')
            for i in range(3):
                Snb_Unlogin_po.swipe_down_new(duration=1)

            #以下是元素的元素的操作
            log.info("点击立即买入按钮")
            Snb_Unlogin_po.get_unlogin_buynow_button_loc_page()
            log.info('已经点击立即买入按钮')
            time.sleep(2)
            log.info("点击登录页面的关闭按钮")
            self.driver.element_by_xpath('//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.TextView[1]').click()
            time.sleep(2)

            #再次进入到未登录首页
            self.driver.element_by_id('com.laijin.simplefinance:id/plan_item_join_bt').click()
            time.sleep(2)
            log.info("点击你有10元奖学金可领取")
            Snb_Unlogin_po.get_unlogin_scholarship_loc_page()
            log.info('已经点击你有10元奖学金可领取')
            time.sleep(2)
            log.info('点击关闭按钮')
            self.driver.element_by_xpath('//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.TextView[1]').click()
            time.sleep(2)

            self.driver.element_by_id('com.laijin.simplefinance:id/plan_item_join_bt').click()
            time.sleep(2)
            log.info("开始点击banner")
            Snb_Unlogin_po.get_unlogin_banner_loc_page()
            log.info("已经点击banner")
            time.sleep(2)
            log.info("点击关闭按钮")
            self.driver.element_by_xpath('//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.TextView[1]').click()
            time.sleep(2)

            # 进入到未登陆首页
            time.sleep(2)
            self.driver.element_by_id('com.laijin.simplefinance:id/plan_item_join_bt').click()
            time.sleep(2)
            log.info("点击立即买入按钮")
            Snb_Unlogin_po.get_unlogin_buynow_button_loc_page()
            log.info('已经点击立即买入按钮')
            time.sleep(2)

        except Exception as msg:
            log.info("异常信息：%s" % msg)
        log.info("-------------------未登陆首页测试：end!--------------------")"""


        #登录脚本
    """
    def test_02_login(self):

        log.info("-------------注册登录测试：start!-------------------")

        try:
            Snb_login_po=SNB_login_page(self.driver)



            #以下是数据的校验
            time.sleep(2)
            log.info("校验登录注册页面的title是否是注册登录")
            self.assertEqual("注册/登录",Snb_login_po.get_login_title_Loc_page())
            time.sleep(2)

            log.info("校验输入手机号输入框中的文本是否是请输入手机号")
            self.assertEqual("请输入手机号码",Snb_login_po.get_login_input_phone_Loc_text_page())
            time.sleep(2)

            log.info("校验是否显示注册协议")
            self.assertEqual("注册即同意《拾年保服务协议》和《拾年保隐私条款》",Snb_login_po.get_login_regist_agree_Loc_page())
            time.sleep(2)

            #以下是操作
            log.info('开始点击登录按钮')
            Snb_login_po.get_login_loginbutton_Loc_page()
            log.info("已经点击登录按钮，进入到登录页面")
            time.sleep(2)
            log.info("开始点击注册页面的，注册按钮")
            Snb_login_po.get_login_registbutton_Loc_page()
            log.info("已经点击注册按钮，进入到注册页面")
            time.sleep(2)

            log.info("输入已注册的手机号")
            Snb_login_po.get_login_input_phone_Loc_page()
            log.info("已经输入注册的手机号")
            time.sleep(2)

            log.info("开始点击注册按钮")
            Snb_login_po.get_login_regist_button_Loc_page()
            log.info("已经点击注册按钮")
            time.sleep(2)

            log.info("校验是否弹出提示语")
            self.assertEqual("该号码已注册",Snb_login_po.get_login_Registered_Loc_page())
            time.sleep(2)

            log.info("清除输入的手机号码")
            Snb_login_po.get_login_icon_Loc_page()
            log.info("已经清除完成")
            time.sleep(2)

            log.info("输入未注册的手机号")
            Snb_login_po.get_login_input_unregphone_Loc_page()
            log.info("已经输入未注册的手机号")
            time.sleep(2)

            log.info("开始点击注册按钮")
            Snb_login_po.get_login_regist_button_Loc_page()
            log.info("已经点击注册按钮")
            time.sleep(2)

            log.info("校验短信验证码输入框中文案")
            self.assertEqual("请输入短信验证码",Snb_login_po.get_login_verficode_Loc_text_page())
            time.sleep(2)

            log.info("输入短信验证码")
            Snb_login_po.get_login_verficode_Loc_page()
            log.info("已经输入短信验证码")
            time.sleep(2)

            log.info("开始点击注册按钮")
            Snb_login_po.get_login_regist_button_Loc_page()
            log.info("已经点击注册按钮")
            time.sleep(2)

            #以下是设置登录密码的操作
            log.info("校验设置登录密码页面的title")
            self.assertEqual("设置登录密码",Snb_login_po.get_login_set_passwd_title_Loc_page())
            time.sleep(2)

            log.info("检验设置密码的要求文案")
            self.assertEqual("8-20位英文与数字组合并区分大小写",Snb_login_po.get_login_set_passwd_requi_Loc_page())
            time.sleep(2)

            log.info("获取输入密码时，输入框中的文案")
            self.assertEqual("请设置登录密码",Snb_login_po.get_login_input_passwd_Loc_text_page())
            time.sleep(2)

            log.info("输入密码")
            Snb_login_po.get_login_input_passwd_Loc_page()
            time.sleep(2)

            log.info("点击是明文还是密文的密码")
            Snb_login_po.get_login_input_passwd_icon_Loc_page()
            time.sleep(2)

            log.info("点击确定按钮")
            Snb_login_po.get_login_input_passwd_confirm_Loc_page()
            time.sleep(2)

            log.info("点击是明文还是密文的密码")
            Snb_login_po.get_login_input_passwd_icon1_Loc_page()
            time.sleep(2)

            #重新输入登录密码
            log.info("再次输入登录密码")
            Snb_login_po.get_login_reinput_passwd_Loc_page()
            time.sleep(2)

            log.info("点击确定按钮")
            Snb_login_po.get_login_input_passwd_confirm_Loc_page()
            time.sleep(2)

            #进入到登录页面

            # log.info("开始点击简理财登录")
            # Snb_login_po.get_login_jlcloginbutton_Loc_page()
            # log.info("已经点击简理财登录按钮，跳转到简理财登录页面")
        except Exception as msg:

            log.info("异常信息：%s"%msg)

        log.info("-----------------注册登录测试：end!-------------------")   """


    #添加银行卡脚本
    """def test_03_add_bank_card(self):
        log.info("-------------添加银行卡测试：start!-------------------")

        try:
            Snb_add_bank_card_po = SNB_bank_card_page(self.driver)

            #点击我的tab
            # log.info("开始点击我的tab")
            # Snb_add_bank_card_po.get_my_tab_Loc_page()
            # log.info('已经进入到我的页面')
            # time.sleep(2)
            #
            # #点击我的银行卡
            # log.info("开始点击我的银行卡")
            # Snb_add_bank_card_po.get_my_bank_card_Loc_page()
            # log.info("已经进入到我的银行卡页面")
            # time.sleep(4)

            # 以下是添加银行卡的操作
            log.info("校验添加银行卡的title是否是添加银行卡")
            self.assertEqual("添加银行卡",Snb_add_bank_card_po.get_add_bank_card_title_Loc_page())
            time.sleep(2)

            log.info("校验获取的持卡人文本")
            self.assertEqual("持卡人",Snb_add_bank_card_po.get_add_bank_card_name_text_Loc_page())
            time.sleep(2)

            log.info("点击持卡人旁边的图标")
            Snb_add_bank_card_po.get_add_bank_card_name_icon_Loc_page()
            time.sleep(2)

            log.info("点击持卡人弹层中的我知道了按钮")
            Snb_add_bank_card_po.get_add_bank_card_name_icon_button_Loc_page()
            time.sleep(2)
            #
            log.info("输入持卡人姓名")
            Snb_add_bank_card_po.get_add_bank_card_name_Loc_page()
            log.info("已经输入持卡人姓名")
            time.sleep(2)

            log.info("校验身份证号的文本")
            self.assertEqual("身份证号",Snb_add_bank_card_po.get_add_bank_card_id_text_Loc_page())
            time.sleep(2)

            log.info("开始输入身份证号")
            Snb_add_bank_card_po.get_add_bank_card_id_Loc_page()
            log.info("已经输入完身份证号码")
            time.sleep(2)


            #点击弹窗中的关闭按钮

            log.info("校验卡号的文本")
            self.assertEqual("卡号",Snb_add_bank_card_po.get_add_bank_card_num_Loc1_page())
            time.sleep(2)

            log.info("输入银行卡号")
            Snb_add_bank_card_po.get_add_bank_card_num_Loc_page()
            log.info("已经输入了银行卡号")
            time.sleep(2)

            log.info("校验银行卡文本")
            self.assertEqual("银行卡",Snb_add_bank_card_po.get_add_bank_card_text__Loc_page())
            time.sleep(2)

            log.info("点击选择银行卡")
            Snb_add_bank_card_po.get_add_bank_card__Loc_page()
            time.sleep(2)

            log.info("选择中国农业银行")
            Snb_add_bank_card_po.get_add_bank_card_list_pop__Loc_page()
            log.info("已经选择中国农业银行")
            time.sleep(2)

            log.info("校验银行预留手机号文本")
            self.assertEqual("银行预留手机号",Snb_add_bank_card_po.get_add_bank_card_phone_text_Loc_page())
            time.sleep(2)

            log.info("输入银行预留手机号码")
            Snb_add_bank_card_po.get_add_bank_card_phone_Loc_page()
            log.info("已经输入完手机号码")
            time.sleep(2)

            log.info("校验短信验证码文本")
            self.assertEqual("短信验证码",Snb_add_bank_card_po.get_add_bank_card_vercode_text_Loc_page())
            time.sleep(2)

            log.info("点击获取验证码")
            Snb_add_bank_card_po.get_add_bank_card_clickvercode_Loc_page()
            time.sleep(2)

            log.info("向上滑动下页面")
            Snb_add_bank_card_po.swipe_up_new(duration=1)


            log.info("输入短信验证码")
            Snb_add_bank_card_po.get_add_bank_card_vercode_Loc_page()
            time.sleep(2)

            log.info("点击确认添加按钮")
            Snb_add_bank_card_po.get_add_bank_card_confirm_button_Loc_page()
            time.sleep(2)

        except Exception as msg:
            log.info('异常信息：%s'%msg)
        log.info("---------------添加银行卡测试：end!-------------------") """

    #设置支付密码
    """def test_04_set_passwd(self):
        log.info("-------------设置支付密码测试：start!-------------------")

        try:
            Snb_set_passwd_po = SNB_set_passwd_page(self.driver)

            # 点击我的tab
            # log.info("开始点击我的tab")
            # Snb_set_passwd_po.get_my_tab_Loc_page()
            # log.info('已经进入到我的页面')
            # time.sleep(2)

            log.info("点击设置支付密码")
            Snb_set_passwd_po.get_set_passwd_Loc_page()
            log.info("已经点击设置支付密码")
            time.sleep(2)

            log.info("校验获取的页面标题")
            self.assertEqual("设置支付密码",Snb_set_passwd_po.get_set_passwd_title_Loc_page())
            time.sleep(2)

            log.info("输入设置的支付密码")
            Snb_set_passwd_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_03Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_06Loc_page()
            time.sleep(2)
            log.info("已设置支付密码123456")

            Snb_set_passwd_po.get_set_passwd_confirm_Loc_page()
            time.sleep(2)

            log.info("再次输入设置的支付密码")
            Snb_set_passwd_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_03Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_06Loc_page()
            time.sleep(2)
            log.info("已设置支付密码成功，跳转到")

        except Exception as msg:
            log.info('异常信息：%s' % msg)
            log.info("---------------设置支付密码测试：end!-------------------")"""

    #立即买入
    def test_05_buy_now(self):
        log.info("-------------立即买入测试：start!-------------------")
        try:
            Snb_buy_now_po=SNB_Buy_now_page(self.driver)

            log.info("点击首页的立即买入按钮")
            Snb_buy_now_po.get_buy_now_button_loc_page()
            log.info("已经进入到立即买入按钮")
            time.sleep(2)

            log.info("校验买入页面的title")
            self.assertEqual("单笔买入",Snb_buy_now_po.get_buy_now_title_loc_page())
            time.sleep(2)

            log.info("校验买入页面的支付方式")
            self.assertEqual("支付方式",Snb_buy_now_po.get_buy_now_pay_method_loc_page())
            time.sleep(2)

            log.info("校验买入金额的文本")
            self.assertEqual("买入金额",Snb_buy_now_po.get_buy_now_pay_amount_loc_page())
            time.sleep(2)

            log.info("校验买入金额输入框中的提示语文本")
            self.assertEqual("最小买入金额1,000.00",Snb_buy_now_po.get_buy_now_pay_amount_text_loc_page())
            time.sleep(2)

            log.info("点击金额输入框")
            Snb_buy_now_po.get_buy_now_pay_amount_click_page()
            time.sleep(2)

            log.info("输入买入金额小于10000")
            Snb_buy_now_po.get_buy_now_pay_amount_input_page()
            time.sleep(2)

            log.info("查看金额小于1000的提示语")
            self.assertEqual("买入金额不能小于最小买入金额1000.00元",Snb_buy_now_po.get_buy_now_error_msg_loc_page())
            time.sleep(2)

            log.info("点击单选框")
            Snb_buy_now_po.get_buy_now_single_box_loc_page()
            log.info("点击完成后是未被选中的状态")
            time.sleep(2)

            log.info("再次点击单选框")
            Snb_buy_now_po.get_buy_now_single_box_loc_page()
            log.info("点击完成后是选中的状态")
            time.sleep(2)

            log.info("校验业务规则的文本")
            self.assertEqual("同意《拾年保基金组合交易业务规则》",Snb_buy_now_po.get_buy_now_bus_rules_loc_page())
            time.sleep(2)

            log.info("校验民生监管的文本")
            self.assertEqual("民生银行监管",Snb_buy_now_po.get_buy_now_ms_jg_loc_page())
            time.sleep(2)

            log.info("点击奕丰金融文本")
            Snb_buy_now_po.get_buy_now_yf_jr_loc_page()
            log.info("已经弹出弹层")
            time.sleep(2)

            log.info("再次点击奕丰金融弹层")
            Snb_buy_now_po.get_buy_now_ms_jg_loc_click_page()
            log.info("弹层消失")
            time.sleep(2)


            log.info("输入买入的金额大于1000")
            Snb_buy_now_po.get_buy_now_pay_amount_inputmore_page()
            log.info("已经输入买入金额")
            time.sleep(2)

            log.info("点击确认买入按钮")
            Snb_buy_now_po.get_buy_now_confirm_button_loc_page()
            time.sleep(2)

            log.info("点击风险测评中的确认评测按钮")
            Snb_buy_now_po.get_buy_now_evaluation_loc_page()
            time.sleep(2)

            log.info("点击风险测评中的第一个问题")
            Snb_buy_now_po.get_buy_now_evaluation01_loc_page()
            time.sleep(2)

            log.info("点击风险测评中的第二个问题")
            Snb_buy_now_po.get_buy_now_evaluation02_loc_page()
            time.sleep(2)

            log.info("点击风险测评中的第三个问题")
            Snb_buy_now_po.get_buy_now_evaluation03_loc_page()
            time.sleep(2)

            log.info("点击风险测评中的第四个问题")
            Snb_buy_now_po.get_buy_now_evaluation04_loc_page()
            time.sleep(2)

            log.info("点击风险测评中的第五个问题")
            Snb_buy_now_po.get_buy_now_evaluation05_loc_page()
            time.sleep(2)

            log.info("点击风险测评中的第六个问题")
            Snb_buy_now_po.get_buy_now_evaluation06_loc_page()
            time.sleep(2)

            log.info("点击风险测评中的完成按钮")
            Snb_buy_now_po.get_buy_now_evaluation_button_loc_page()
            time.sleep(2)

            log.info("点击风险测评中的确认无误按钮")
            Snb_buy_now_po.get_buy_now_evaluation_confirmbutton_loc_page()
            time.sleep(2)

            log.info("点击评测结果按钮")
            Snb_buy_now_po.get_buy_now_evaluation_confirmres_loc_page()
            time.sleep(2)

            log.info("点击立即买入按钮，进入到买入页面")
            Snb_buy_now_po.get_buy_now_button_loc_page()
            log.info("已经进入到立即买入页面")

            log.info("输入买入的金额")
            Snb_buy_now_po.get_buy_now_pay_amount_inputmore_page()
            log.info("已经输入买入金额")
            time.sleep(2)

            log.info("点击确认买入按钮")
            Snb_buy_now_po.get_buy_now_confirm_button_loc_page()
            time.sleep(2)

            log.info("输入支付密码")



        except Exception as msg:
            log.info("异常信息：%s"%msg)
            log.info("------------立即买入测试：end!------------------")


            
# if __name__ == '__main__':
#     unittest.main()
