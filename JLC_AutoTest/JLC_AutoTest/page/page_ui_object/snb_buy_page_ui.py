from JLC_AutoTest.model.base import Base


class Snb_Buy_Now_PageUI(Base):
    """
        页面UI对象（PUO）：立即买入的页面
    """

    def get_buy_now_button_loc(self):
        """
            定位立即买入按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="立即买入"]',
        })

    def get_buy_now_title_loc(self):
        """
            定位立即买入页面的title
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })

    def get_buy_now_pay_method_loc(self):
        """
            定位立即买入页面的支付方式文本
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="支付方式"]',
        })

    def get_buy_now_pay_amount_loc(self):
        """
            定位立即买入页面的买入金额文本
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="买入金额"]',
        })

    def get_buy_now_pay_amount_text_loc(self):
        """
            定位立即买入页面的买入金额提示框中文本
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="最小买入金额1,000.00"]',
        })

    def get_buy_now_confirm_button_loc(self):
        """
            定位确认买入按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认买入"]',
        })

    def get_buy_now_single_box_loc(self):
        """
            定位单选框（默认是选中状态，点击后变为不可选中状态）
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="animation-wrapper"]/android.view.View[7]',
        })

    def get_buy_now_bus_rules_loc(self):
        """
            定位业务规则文本
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="同意《拾年保基金组合交易业务规则》"]',
        })

    def get_buy_now_ms_jg_loc(self):
        """
            定位民生监管文本
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="民生银行监管"]',
        })

    def get_buy_now_yf_jr_loc(self):
        """
            定位奕丰金融文本
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="奕丰金融"]',
        })

    def get_buy_now_error_msg_loc(self):
        """
            定位输入的金额小于1000时，显示提示语的文本，买入金额不能小于最小买入金额1000.00元
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="买入金额不能小于最小买入金额1,000.00元"]',
        })


    # def get_buy_now_error_msg_loc(self):
    #     """
    #         定位输入的金额小于1000时，显示提示语的文本，买入金额不能小于最小买入金额1000.00元
    #     :return:
    #     """
    #     return self.selector({
    #         'ios_by': '',
    #         'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
    #         'android_by': 'xpath',
    #         'android_value': '//*[@text="买入金额不能小于最小买入金额1,000.00元"]',
    #     })

    def get_buy_now_evaluation_loc(self):
        """
            定位风险测评中确认并进行测评的按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认并进行测评"]',
        })

    def get_buy_now_evaluation01_loc(self):
        """
            定位风险测评中第一个问题
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="闲赋在家"]',
        })

    def get_buy_now_evaluation02_loc(self):
        """
            定位风险测评中第二个问题
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="5万及以下"]',
        })

    def get_buy_now_evaluation03_loc(self):
        """
            定位风险测评中第三个问题
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="有时需要使用投资资金"]',
        })
    def get_buy_now_evaluation04_loc(self):
        """
            定位风险测评中第四个问题
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="保证本金安全"]',
        })

    def get_buy_now_evaluation05_loc(self):
        """
            定位风险测评中第五个问题
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="<5%（精打细算型）"]',
        })

    def get_buy_now_evaluation06_loc(self):
        """
            定位风险测评中第六个问题
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="从事金融行业多年"]',
        })

    def get_buy_now_evaluation_button_loc(self):
        """
            定位风险测评中完成按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="完成"]',
        })

    def get_buy_now_evaluation_confirmbutton_loc(self):
        """
            定位风险测评中的确认无误按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认无误提交"]',
        })

    def get_buy_now_evaluation_confirmres_loc(self):
        """
            定位风险测评中的确认评测结果按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认测评结果"]',
        })

    def get_buy_now_pay_pass_text_loc(self):
        """
            定位支付密码弹层中的请输入基金支付密码的文本
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入基金支付密码"]',
        })

    def get_buy_now_pay_pass_close_loc(self):
        """
            定位支付密码弹层中的关闭按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="关闭"]',
        })

    def get_buy_now_pay_pass_yf_text_loc(self):
        """
            定位支付密码弹层中文本基金销售服务由奕丰金融提供
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[1]/android.view.View[5]',
        })

    def get_buy_now_complete_loc(self):
        """
            定位买入完成页面的title
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_buy_now_complete_button_loc(self):
        """
            定位买入完成页面的完成按钮
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="完成"]',
        })