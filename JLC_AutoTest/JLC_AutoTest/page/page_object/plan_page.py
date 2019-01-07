from JLC_AutoTest.page.page_ui_object.plan_page_ui import PlanPageUI


class PlanPage(PlanPageUI):
    """
        页面对象(PO): 计划页面
    """
    def click_plan_tab(self):
        """
            点击[计划]图标
        :return:
        """
        self.plan_loc().click()

    def click_dream_plan_img(self):
        """
            点击[梦想计划]
        :return:
        """
        self.dream_plan_loc().click()

    def click_select_dream_plan(self):
        """
            选择梦想计划
        :return:
        """
        self.select_dream_plan_loc().click()

    def click_next_button(self):
        """
            点击[下一步]按钮
        :return:
        """
        self.next_button_loc().click()

    def click_auto_dream_button(self):
        """
            点击[自动开启梦想]
        :return:
        """
        self.auto_dream_button_loc().click()

    def click_confirm_button(self):
        """
            点击[确定]按钮
        :return:
        """
        self.confirm_button_loc().click()

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

    def click_complete_button(self):
        """
            点击[完成]按钮
        :return:
        """
        self.complete_button_loc().click()

    def click_dream_plan_menu(self):
        """
            点击梦想计划菜单
        :return:
        """
        self.dream_plan_menu_loc().click()

    def click_stop_dream_plan(self):
        """
            点击梦想计划[终止计划]
        :return:
        """
        self.stop_dream_plan_loc().click()

    def click_confirm_stop_dream(self):
        """
            点击确认梦想计划[残忍终止]
        :return:
        """
        self.confirm_stop_dream_loc().click()

    # 输入支付密码

    def click_stop_dream_plan_complete_button(self):
        """
            点击梦想计划终止[完成]
        :return:
        """
        self.stop_dream_plan_complete_button_loc().click()
