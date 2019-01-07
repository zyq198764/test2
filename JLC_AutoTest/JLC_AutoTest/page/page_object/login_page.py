from JLC_AutoTest.page.page_ui_object.login_page_ui import LoginPageUI


#登录页面的元素
class LoginPage(LoginPageUI):
    """
        页面对象(PO): 登录页面
    """

    def click_login_button(self):
        """
            点击未登陆首页的[注册/登录]按钮
        :return:
        """
        return self.login_button_loc().click()

    def input_user_phone(self, phone_number):
        """
            输入用户手机号
        :param phone_number:
        :return:
        """
        return self.user_phone_input_loc().send_keys(phone_number)


    def click_next_button(self):
        """
            点击[下一步]按钮
        :return:
        """
        return self.next_button_loc().click()

    def input_validate_code(self):
        """
            验证码键盘输入
        :return:
        """
        self.driver.keys('send keys: ${Keys.NUMPAD1}')
        self.driver.keys('send keys: ${Keys.NUMPAD2}')
        self.driver.keys('send keys: ${Keys.NUMPAD3}')
        self.driver.keys('send keys: ${Keys.NUMPAD4}')
        self.driver.keys('send keys: ${Keys.NUMPAD5}')
        self.driver.keys('send keys: ${Keys.NUMPAD6}')

    def gesture_password(self):
        """
            解锁手势密码
        :return:
        """
        # self.driver.touch([{'type': 'drag', 'fromX': 400, 'fromY': 880, 'toX': 970, 'toY': 880, 'steps': 200}, \
        #                    {'type': 'drag', 'toX': 425, 'toY': 1490, 'duration': 3}, \
        #                    {'type': 'drag', 'toX': 970, 'toY': 1490, 'duration': 200}])

        self.driver.touch([{'type': 'drag', 'fromX': 290, 'fromY': 756, 'toX': 798, 'toY': 756, 'steps': 200}, \
                           {'type': 'drag', 'toX': 425, 'toY': 1240, 'duration': 3}, \
                           {'type': 'drag', 'toX': 800, 'toY': 1240, 'duration': 200}])

    """ 获取验证信息 """


    def get_full_phone_number_text(self):
        """
            获取文本"填写手机号"
        :return:
        """
        return self.full_phone_number_text_loc().text

    def get_full_phone_fanhui_button(self):
        """
             返回按钮元素的获取
        :return:
        """
        return self.full_phone_fanhui_button()

    def get_full_phone_num_edit_text_loc(self):
        """
             获取手机号输入框中文本
        :return:
        """
        return self.full_phone_num_edit_text_loc().text

    def get_full_ptfwxy_text_loc(self):
        """
             获取是否显示平台服务协议
        :return:
        """
        return self.full_ptfwxy_text_loc().text

    def get_full_jlcystk_text_loc(self):
        """
             获取是否显示简理财隐私条款
        :return:
        """
        return self.full_jlcystk_text_loc()
    def get_full_weixin_loc(self):
        """
            是否显示微信登录
        :return:
        """
        return  self.full_weixin_loc()

    def get_full_dbutton_loc(self):
        """
            是否显示底部图片
        :return:
        """
        return self.full_dbutton_loc()

    def get_full_validate_code_text(self):
        """
           获取文本"输入验证码"
        :return:
        """
        return self.full_validate_code_text_loc().text

    def get_gesture_password_one_text(self):
        """
            获取文本"请 绘 制 手 势 图 案"
        :return:
        """
        return self.get_gesture_password_one_text().text

    def get_gesture_password_two_text(self):
        """
            获取文本"请 再 次 绘 制 手 势 图 案 进 行 确 认"
        :return:
        """
        return self.gesture_password_two_text_loc().text
