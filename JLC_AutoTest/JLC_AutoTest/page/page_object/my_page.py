from JLC_AutoTest.page.page_ui_object.my_page_ui import MyPageUI


class MyPage(MyPageUI):
    """
        页面对象(PO): 我的页面
    """

    """ 房租房贷计划 """

    def click_my(self):
        """
            点击"我的"
        :return:
        """
        self.my_loc().click()

    def click_rent_plan(self):
        """
            点击"房屋房贷"
        :return:
        """
        self.rent_plan_loc().click()

    def click_start_rent_plan(self):
        """
            点击"开启房租房贷计划"
        :return:
        """
        self.start_rent_plan_loc().click()

    def click_money_next_button(self):
        """
            点击[下一步]按钮
        :return:
        """
        self.money_next_button_loc().click()

    def click_rent_cycle_next_button(self):
        """
            点击[下一步]按钮
        :return:
        """
        self.rent_cycle_next_button_loc().click()

    def click_monthday_next_button(self):
        """
            点击[开始自动交房租]按钮
        :return:
        """
        self.monthday_next_button_loc().click()

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

    def click_confirm_button(self):
        """
            点击[完成]按钮
        :return:
        """
        self.confirm_button_loc().click()

    def click_selected_rent_plan(self):
        """
            点击已存在的房租房贷计划
        :return:
        """
        self.selected_rent_plan_loc().click()

    def click_rent_plan_menu(self):
        """
            点击房租房贷计划菜单
        :return:
        """
        self.rent_plan_menu_loc().click()

    def click_stop_rent_plan(self):
        """
            点击房屋房贷[终止计划]
        :return:
        """
        self.stop_salary_plan_loc().click()

    def click_confirm_stop_rent_plan(self):
        """
            点击房屋房贷[确认终止]
        :return:
        """
        self.confirm_stop_rent_plan_loc()

    # 输入支付密码

    def click_stop_rent_plan_complete_button(self):
        """
            点击房屋房贷终止计划[完成]按钮
        :return:
        """
        self.stop_rent_plan_complete_button_loc().click()

    """ 工资计划 """

    def click_salary_plan(self):
        """
            点击[存工资]图标
        :return:
        """
        self.salary_plan_loc().click()

    def click_salary_next_butto(self):
        """
            点击存入金额[下一步]按钮
        :return:
        """
        self.salary_next_button_loc().click()

    def click_join_salary_plan_button(self):
        """
            点击[加入工资计划]按钮
        :return:
        """
        self.join_salary_plan_button_loc().click()

    # 输入支付密码

    def click_dialog_sure(self):
        """
            点击[我知道了]
        :return:
        """
        self.dialog_sure_loc().click()

    def click_salary_plan_menu(self):
        """
            点击工资计划菜单
        :return:
        """
        self.salary_plan_menu_loc().click()

    def click_stop_salary_plan(self):
        """
            点击[终止计划]
        :return:
        """
        self.stop_salary_plan_loc().click()

    def click_confirm_stop_salary_plan(self):
        """
            点击"确定终止"
        :return:
        """
        self.confirm_stop_salary_plan_loc().click()

    def click_stop_salary_plan_complete_button(self):
        """
            点击终止工资计划[完成]按钮
        :return:
        """
        self.stop_salary_plan_loc().click()