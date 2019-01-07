from JLC_AutoTest.model.base import Base


class LoginPageUI(Base):
    """
        页面UI对象（PUO）：登录页面UI
    """

    def login_button_loc(self):
        """
            定位[注册/登录]按钮,未登陆首页
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/iv_register_or_login',
        })

    def login_title(self):
        """
           校验登陆页面的title是否是'填写手机号'
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '填写手机号',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/login_input_et',
        })
    def user_phone_input_loc(self):
        """
            定位用户手机输入框,输入手机号
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeTextField[1]',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/login_input_et',
        })

    def next_button_loc(self):
        """
            点击[下一步]
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'login next normal',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/login_next_btn',
        })
    def enter_valid_loc(self):
        """
          输入验证码1
        :return:
        """
        return self.selector({
            'ios_by':'xpath',
            'ios_value':'//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeTextField[1]',
            'android_by':'',
            'android_value':'',
        })

    """ 验证信息 """

    def full_phone_number_text_loc(self):
        """
            定位"填写手机号"文本
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeTextField[1]',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/trans_title_prompt_tv',
        })
    def full_phone_fanhui_button(self):
        """
            返回按钮的定位
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/trans_bt_left_btn',
        })

    def full_phone_num_edit_text_loc(self):
        """
            获取"输入手机号输入框中的文本"
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/login_input_et',
        })

    def full_ptfwxy_text_loc(self):
        """
           获取是否显示平台服务协议
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@text="《简理财平台服务协议》"]',
        })

    def full_jlcystk_text_loc(self):
        """
            获取是否显示简理财隐私条款
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/protocolList_ll"]/android.widget.LinearLayout[2]',
        })
    def full_weixin_loc(self):
        """
            是否显示微信登录
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/wechat_login_iv',
        })

    def full_dbutton_loc(self):
        """
            是否显示底部图片
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/content_container"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]',
        })

    def full_validate_code_text_loc(self):
        """
            定位"输入验证码"文本
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/trans_title_prompt_tv',
        })

    def gesture_password_one_text_loc(self):
        """
            定位"请 绘 制 手 势 图 案"文本
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/gesture_title_tv',
        })

    def gesture_password_two_text_loc(self):
        """
            定位"请 再 次 绘 制 手 势 图 案 进 行 确 认"文本
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/gesture_title_tv',
        })