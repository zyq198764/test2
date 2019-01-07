
from JLC_AutoTest.page.page_ui_object.bankcard_page_ui import BankCardPageUI


class BankCard(BankCardPageUI):
    """
        页面对象(PO): 添加银行卡
    """
    def click_mybankcard_button_loc_(self):
        """
            点击我的银行卡
        :return:
        """
        self.mybankcard_loc().click()
    def click_addmybankcard_loc(self):
        """
            点击我的银行卡
        :return:
        """
        self.addmybankcard_loc().click()
    def get_addbankcard_title(self):
        """
           获取添加银行卡页面的title
        :return:
        """
        self.addbankcard_title().text()
