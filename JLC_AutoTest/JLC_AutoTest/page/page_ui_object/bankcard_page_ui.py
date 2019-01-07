from JLC_AutoTest.model.base import Base


class BankCardPageUI(Base):
    """
        页面UI对象（PUO）：绑卡页面UI
    """
    def mybankcard_loc(self):
        """
            定位我的银行卡
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/my_bank_ll',
        })
    def addmybankcard_loc(self):
        """
            点击添加银行卡
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/add_bank_card_view_holer',
        })

    def addmybankcard_loc(self):
        """
            点击添加银行卡
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/add_bank_card_view_holer',
        })
    def addbankcard_title(self):
        """
           获取添加银行卡的title
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@text="添加银行卡"]',
        })
    def get_back_button_loc(self):
        """
          获取返回按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.TextView[1]',
        })
    def get_kefu_button_loc(self):
        """
           获取呼叫客服的图标
        :return:
        """

        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]',
        })
    def  get_up_content_loc(self):
        """
           获取持卡人上方的文案为"绑卡验证服务由通联支付提供"
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/tv_bind_card_tips',
        })
    def get_name_loc(self):
        """
           获取持卡人的文本输入框
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/et_input_name',
        })
    def get_id_card_no_loc(self):
        """
          获取身份证号的文本输入框
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/et_input_id_card_no',
        })

    def get_bank_no_loc(self):
        """
          获取卡号
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/et_input_bank_no',
        })