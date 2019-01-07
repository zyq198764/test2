from JLC_AutoTest.model.base import Base


class HomePageUI(Base):
    """
        页面UI对象（PUO）：主页页面UI
    """

    def buy_button_loc(self):
        """
            定位[买入]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/bt_home_fragment_turn_in',
        })

    def in_money_input_loc(self):
        """
            定位"买入金额"输入框
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/et_turn_in_money',
        })

    def in_confirm_money_button_loc(self):
        """
            定位[立即买入]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/bt_turn_in_confirms',
        })

    def in_complete_button_loc(self):
        """
            定位买入[完成]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/turn_in_result_confirm_back_btn',
        })

    def draw_button_loc(self):
        """
            定位[转出]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/bt_home_fragment_with_draw',
        })

    def draw_money_input_loc(self):
        """
            定位"转出金额"输入框
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/withdraw_et_money',
        })

    def draw_confirm_money_button_loc(self):
        """
            定位[确认转出]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/withdraw_bt_confirm',
        })

    def cancal_button_loc(self):
        """
            定位调查[X]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/pop_cancel_iv',
        })

    def remark_close_button_loc(self):
        """
            定位[X]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/remark_close_iv',
        })

    def confirm_button_loc(self):
        """
            选择[确认]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/confirm_bt',
        })

    def draw_complete_button_loc(self):
        """
            定位转出[完成]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/withdraw_result_confirm_back_btn',
        })

    def pop_text_loc(self):
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/text',
        })

    """ 验证信息 """
    def text_assets_loc(self):
        """
            定位"总资产"
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@text="总资产"]',
        })

    def text_profit_loc(self):
        """
            定位"总资产"
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@text="累计收益"]',
        })
