from JLC_AutoTest.page.page_ui_object.snb_set_passwd_page_ui import Snb_Set_Passwd_PageUI
from JLC_AutoTest.model.utils import JianlcTools


#登录页面的元素
class SNB_set_passwd_page(Snb_Set_Passwd_PageUI):
    """
        页面对象(PO): 设置支付密码的页面
    """
    def get_set_passwd_Loc_page(self):
        """
            点击设置支付密码
        :return:
        """
        return self.get_set_passwd_Loc().click()

    def get_set_passwd_title_Loc_page(self):
        """
            获取设置支付密码的title
        :return:
        """
        return self.get_set_passwd_title_Loc().text

    def get_set_passwd_01Loc_page(self):
        """
            输入支付密码1
        :return:
        """
        return self.get_set_passwd_01Loc().click()
    def get_set_passwd_02Loc_page(self):
        """
            输入支付密码2
        :return:
        """
        return self.get_set_passwd_02Loc().click()
    def get_set_passwd_03Loc_page(self):
        """
            输入支付密码3
        :return:
        """
        return self.get_set_passwd_03Loc().click()
    def get_set_passwd_04Loc_page(self):
        """
            输入支付密码4
        :return:
        """
        return self.get_set_passwd_04Loc().click()
    def get_set_passwd_05Loc_page(self):
        """
            输入支付密码5
        :return:
        """
        return self.get_set_passwd_05Loc().click()
    def get_set_passwd_06Loc_page(self):
        """
            输入支付密码6
        :return:
        """
        return self.get_set_passwd_06Loc().click()

    def get_set_passwd_confirm_Loc_page(self):
        """
            点击确认输入支付密码的弹框
        :return:
        """
        return self.get_set_passwd_confirm_Loc().click()



