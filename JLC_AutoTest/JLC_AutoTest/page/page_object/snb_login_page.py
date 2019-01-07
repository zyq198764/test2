from JLC_AutoTest.page.page_ui_object.snb_login_page_ui import Snb_LoginPageUI
from JLC_AutoTest.model.utils import JianlcTools


#登录页面的元素
class SNB_login_page(Snb_LoginPageUI):
    """
        页面对象(PO): 注册登录页面
    """

    def get_login_close_button_Loc_page(self):
        """
            获取注册登录页面的关闭按钮
        :return:
        """
        return self.get_login_close_button_Loc.click()

    def get_login_title_Loc_page(self):
        """
            获取注册登录页面的title
        :return:
        """
        return self.get_login_title_Loc().text

    def get_login_loginbutton_Loc_page(self):
        """
            获取注册登录页面的登录按钮
        :return:
        """
        return self.get_login_loginbutton_Loc().click()

    def get_login_input_phone_Loc_text_page(self):
        """
            获取注册登录页面的手机号输入框的文案
        :return:
        """
        return self.get_login_input_phone_Loc().text

    def get_login_input_phone_Loc_page(self):
        """
            输入手机号
        :return:
        """
        return self.get_login_input_phone_Loc().send_keys('13520347057')

    def get_login_input_unregphone_Loc_page(self):
        """
            输入手机号
        :return:
        """
        return self.get_login_input_phone_Loc().send_keys(JianlcTools.createphones(self))
    def get_login_regist_agree_Loc_page(self):
        """
            获取注册登录页面的注册协议
        :return:
        """
        return self.get_login_regist_agree_Loc().text

    def get_login_jlcloginbutton_Loc_page(self):
        """
            获取注册登录页面的注册协议
        :return:
        """
        return self.get_login_jlcloginbutton_Loc().click()

    def get_login_registbutton_Loc_page(self):
        """
            点击登录页面的注册按钮
        :return:
        """
        return self.get_login_registbutton_Loc().click()

    def get_login_regist_button_Loc_page(self):
        """
           点击注册页面的注册按钮
        :return:
        """
        return self.get_login_regist_button_Loc().click()

    def get_login_verficode_Loc_text_page(self):
        """
           获取输入短信验证码输入框中的文本
        :return:
        """
        return self.get_login_verficode_Loc().text

    def get_login_verficode_Loc_page(self):
        """
           输入短信验证码
        :return:
        """
        return self.get_login_verficode_Loc().send_keys('123456')

    def get_login_Registered_Loc_page(self):
        """
           如果输入的手机号已注册，给与提示语
        :return:
        """
        return self.get_login_Registered_Loc().text

    def get_login_icon_Loc_page(self):
        """
           清除手机号码
        :return:
        """
        return self.get_login_icon_Loc().click()

    def get_login_set_passwd_title_Loc_page(self):
        """
           获取设置登录密码页面的title
        :return:
        """
        return self.get_login_set_passwd_title_Loc().text

    def get_login_set_passwd_requi_Loc_page(self):
        """
            获取设置密码的要求
        :return:
        """
        return self.get_login_set_passwd_requi_Loc().text

    def get_login_input_passwd_Loc_text_page(self):
        """
            获取密码输入框中的文案
        :return:
        """
        return self.get_login_input_passwd_Loc().text
    def get_login_input_passwd_Loc_page(self):
        """
            输入密码
        :return:
        """
        return self.get_login_input_passwd_Loc().send_keys('zyq111111')

    # def get_login_input_passwd_Loc_page(self):
    #     """
    #         输入密码
    #     :return:
    #     """
    #     return self.get_login_input_passwd_Loc().send_keys('zyq111111')

    def  get_login_input_passwd_icon_Loc_page(self):
        """
            点击图标，显示明文还是密文
        :return:
        """
        return self.get_login_input_passwd_icon_Loc().click()

    def get_login_input_passwd_icon1_Loc_page(self):
        """
            点击图标，显示明文还是密文
        :return:
        """
        return self.get_login_input_passwd_icon1_Loc()

    def  get_login_input_passwd_confirm_Loc_page(self):
        """
            点击确定按钮
        :return:
        """
        return self.get_login_input_passwd_confirm_Loc().click()

    def  get_login_reinput_passwd_Loc_page(self):
        """
            点击确定按钮
        :return:
        """
        return self.get_login_reinput_passwd_Loc().send_keys("zyq111111")