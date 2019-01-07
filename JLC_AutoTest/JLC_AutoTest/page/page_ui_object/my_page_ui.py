from JLC_AutoTest.model.base import Base


class MyPageUI(Base):
    """
        页面UI对象（PUO）：我的页面UI
    """
    def my_loc(self):
        """
            定位[我的]
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeButton[4]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/main_indicator"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]',
        })

    def rent_plan_loc(self):
        """
            定位[房租房贷]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/ll_operation"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]',
        })

    def start_rent_plan_loc(self):
        """
            定位[开启房租房贷计划]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[3]',
        })

    def money_next_button_loc(self):
        """
            定位[下一步]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'id',
            'android_value': 'com.laijin.simplefinance:id/dream_plan_saving_money_accelerate_bt',
        })

    def rent_cycle_next_button_loc(self):
        """
            定位[下一步]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'id',
            'android_value': 'com.laijin.simplefinance:id/rent_cycle_select_next_bt',
        })

    def monthday_next_button_loc(self):
        """
            定位[开始自动交房租]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'id',
            'android_value': 'com.laijin.simplefinance:id/monthday_select_submit_bt',
        })

    def confirm_button_loc(self):
        """
            定位[完成]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'id',
            'android_value': 'com.laijin.simplefinance:id/set_rent_or_mort_result_confirm_btn',
        })

    def selected_rent_plan_loc(self):
        """
            选择已存在的房租房贷计划
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'id',
            'android_value': 'com.laijin.simplefinance:id/plan_title_tv',
        })

    def rent_plan_menu_loc(self):
        """
            定位房租房贷计划菜单
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]',
        })

    def stop_rent_plan_loc(self):
        """
            定位房租房贷计划"终止计划"
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/stop_plan_tv',
        })

    def confirm_stop_rent_plan_loc(self):
        """
            定位房租房贷计划"确定终止"
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/tv_confirm',
        })

    def stop_rent_plan_complete_button_loc(self):
        """
            定位终止房租房贷计划[完成]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/complete_btn',
        })

    """ 工资计划定位元素 """

    def salary_plan_loc(self):
        """
            定位[存工资]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/ll_operation"]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]',
        })

    def salary_next_button_loc(self):
        """
            定位存工资[下一步]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/money_next_btn',
        })

    def join_salary_plan_button_loc(self):
        """
            定位[加入工资计划]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/join_salary_plan_bt',
        })

    def dialog_sure_loc(self):
        """
            定位[我知道了]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/dialog_sure_tv',
        })

    def salary_plan_menu_loc(self):
        """
            定位工资计划菜单
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]',
        })

    def stop_salary_plan_loc(self):
        """
            定位"终止计划"
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/salary_plan_stop_tv',
        })

    def confirm_stop_salary_plan_loc(self):
        """
            定位"确定终止"
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/tv_cancel',
        })

    def stop_salary_plan_complete_button_loc(self):
        """
            定位终止工资计划[完成]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/salary_plan_success_btn',
        })

    """ 信用卡还款 """

    def credit_card_loc(self):
        """
            定位[还信用卡]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/ll_operation"]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]',
        })