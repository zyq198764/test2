from JLC_AutoTest.page.page_ui_object.snb_bank_card_ui import Snb_Bank_Card_PageUI
from JLC_AutoTest.model.utils import JianlcTools
from JLC_AutoTest.model.utils import bank_number,card_number,gener_name


#登录页面的元素
class SNB_bank_card_page(Snb_Bank_Card_PageUI):
    """
        页面对象(PO): 我的银行卡页面
    """

    def get_my_tab_Loc_page(self):
        """
            获取我的tab
        :return:
        """
        return self.get_my_tab_Loc().click()

    def get_my_bank_card_Loc_page(self):
        """
            点击我的银行卡
        :return:
        """
        return self.get_my_bank_card_Loc().click()

    def get_add_bank_card_title_Loc_page(self):
        """
            获取添加银行卡页面的title
        :return:
        """
        return self.get_add_bank_card_title_Loc().text

    def get_add_bank_card_name_text_Loc_page(self):
        """
            获取添加银行卡页面持卡人文本
        :return:
        """
        return self.get_add_bank_card_name_text_Loc().text

    def get_add_bank_card_name_icon_Loc_page(self):
        """
            点击持卡人旁边的icon
        :return:
        """
        return self.get_add_bank_card_name_icon_Loc().click()

    def get_add_bank_card_name_icon_button_Loc_page(self):
        """
            点击持卡人弹层中的我知道了按钮
        :return:
        """
        return self.get_add_bank_card_name_icon_button_Loc().click()

    def get_add_bank_card_name_Loc_page(self):
        """
            获取添加银行卡页面持卡人文本
        :return:
        """
        return self.get_add_bank_card_name_Loc().send_keys(gener_name())

    def get_add_bank_card_id_text_Loc_page(self):
        """
            获取添加银行卡页面身份证号码文本
        :return:
        """
        return self.get_add_bank_card_id_text_Loc().text
    def get_add_bank_card_id_Loc_page(self):
        """
            输入身份证号码
        :return:
        """
        return self.get_add_bank_card_id_Loc().send_keys(card_number())

    def get_add_bank_card_list_Loc_page(self):
        """
            查看支持的银行卡列表
        :return:
        """
        return self.get_add_bank_card_list_Loc().click()


    def get_add_bank_card_list_button_Loc_page(self):
        """
            查看支持的银行卡列表
        :return:
        """
        return self.get_add_bank_card_list_button_Loc().click()

    def get_add_bank_card_text__Loc_page(self):
        """
            查看银行卡号文本
        :return:
        """
        return self.get_add_bank_card_text__Loc().text
    def get_add_bank_card_num_Loc1_page(self):
        """
            查看银行卡号文本
        :return:
        """
        return self.get_add_bank_card_num_Loc().text

    def get_add_bank_card_num_Loc_page(self):
        """
            输入银行卡号
        :return:
        """
        return self.get_add_bank_card_num__Loc().send_keys(bank_number())

    def get_add_bank_card__Loc_page(self):
        """
            点击银行卡列表
        :return:
        """
        return self.get_add_bank_card__Loc().click()

    def get_add_bank_card_text__Loc_page(self):
        """
           获取银行卡文本
        :return:
        """
        return self.get_add_bank_card_text__Loc().text

    def get_add_bank_card_list_pop__Loc_page(self):
        """
            点击农业银行
        :return:
        """
        return self.get_add_bank_card_list_pop__Loc().click()

    def get_add_bank_card_phone_text_Loc_page(self):
        """
            获取银行预留手机号
        :return:
        """
        return self.get_add_bank_card_phone_text_Loc().text

    def get_add_bank_card_phone_Loc_page(self):
        """
            输入银行预留手机号码
        :return:
        """
        return self.get_add_bank_card_phone_Loc().send_keys(JianlcTools.createphones(self))
    def get_add_bank_card_vercode_text_Loc_page(self):
        """
            获取短信验证码文本
        :return:
        """
        return self.get_add_bank_card_vercode_text_Loc().text

    def get_add_bank_card_vercode_Loc_page(self):
        """
            输入短信验证码
        :return:
        """
        return self.get_add_bank_card_vercode_Loc().send_keys('888888')

    def get_add_bank_card_clickvercode_Loc_page(self):
        """
            点击获取短信验证码
        :return:
        """
        return self.get_add_bank_card_clickvercode_Loc().click()

    def get_add_bank_card_confirm_button_Loc_page(self):
        """
            点击确认添加按钮
        :return:
        """
        return self.get_add_bank_card_confirm_button_Loc().click()

