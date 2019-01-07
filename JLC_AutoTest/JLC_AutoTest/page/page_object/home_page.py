from JLC_AutoTest.page.page_ui_object.home_page_ui import HomePageUI


class HomePage(HomePageUI):
    """
       页面对象(PO): 主页页面
    """
    def click_buy_button(self):
        """
            点击[买入]按钮
        :return:
        """
        self.buy_button_loc().click()

    def input_in_money(self, money):
        """
            输入买入金额
        :param money:
        :return:
        """
        self.in_money_input_loc().send_keys(money)

    def click_in_confirm_money_button(self):
        """
            点击[立即买入]按钮
        :return:
        """
        self.in_confirm_money_button_loc().click()

    def click_in_complete_button(self):
        """
            点击买入[完成]按钮
        :return:
        """
        self.in_complete_button_loc().click()

    def click_draw_button(self):
        """
            点击[转出]按钮
        :return:
        """
        self.draw_button_loc().click()

    def input_draw_money(self, money):
        """
            输入转出金额
        :param money:
        :return:
        """
        self.draw_money_input_loc().send_keys(money)

    def click_draw_confirm_money_button(self):
        """
            点击[确认转出]按钮
        :return:
        """
        self.draw_confirm_money_button_loc().click()

    def click_cancel_button(self):
        """
            点击[X]按钮
        :return:
        """
        self.cancal_button_loc().click()

    def click_remark_close_button(self):
        """
            点击选择[饮食]按钮
        :return:
        """
        self.remark_close_button_loc().click()

    def click_confirm_button(self):
        """
            点击[确认]按钮
        :return:
        """
        self.confirm_button_loc().click()

    def click_draw_complete_button(self):
        """
            点击转出[完成]按钮
        :return:
        """
        self.draw_complete_button_loc().click()

    def click_pop_text(self):
        self.pop_text_loc().click()

    def input_password(self):
        """
            验证码键盘输入支付密码
        :return:
        """
        self.driver.touch('press', {'x': 245, 'y': 1865, 'duration': 2})
        self.driver.touch('press', {'x': 725, 'y': 1865, 'duration': 2})
        self.driver.touch('press', {'x': 1200, 'y': 1865, 'duration': 2})
        self.driver.touch('press', {'x': 245, 'y': 2045, 'duration': 2})
        self.driver.touch('press', {'x': 725, 'y': 2045, 'duration': 2})
        self.driver.touch('press', {'x': 1200, 'y': 2045, 'duration': 2})

    """ 获取验证信息 """

    def get_text_assets(self):
        """
            获取"总资产"文本
        :return:
        """
        return self.text_assets_loc().text

    def get_text_profit(self):
        """
            获取"累计收益"
        :return:
        """
        return self.text_profit_loc().text