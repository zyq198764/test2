from JLC_AutoTest.model.base import Base


class PlanPageUI(Base):
    """
        页面UI对象（PUO）：计划页面UI
    """

    def plan_loc(self):
        """
            定位[计划]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/main_indicator"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView',
        })

    def dream_plan_loc(self):
        """
            定位[梦想计划]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="android:id/list"]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]',
        })

    def select_dream_plan_loc(self):
        """
            选择梦想计划
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@text="去泰国玩"]',
        })

    def next_button_loc(self):
        """
            定位[下一步]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'id',
            'android_value': 'com.laijin.simplefinance:id/money_next_btn',
        })

    def auto_dream_button_loc(self):
        """
            定位[自动开启梦想]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'id',
            'android_value': 'com.laijin.simplefinance:id/dream_plan_auto_set_btn',
        })

    def confirm_button_loc(self):
        """
            定位[确定]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'id',
            'android_value': 'com.laijin.simplefinance:id/dream_plan_confirm_bt',
        })

    def complete_button_loc(self):
        """
            定位[完成]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'id',
            'android_value': 'com.laijin.simplefinance:id/complete',
        })

    """ 终止梦想计划 """

    def dream_plan_menu_loc(self):
        """
            定位梦想计划菜单
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]',
        })

    def stop_dream_plan_loc(self):
        """
            定位梦想计划[终止计划]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'id',
            'android_value': 'com.laijin.simplefinance:id/tv_stop_dream',
        })

    def confirm_stop_dream_loc(self):
        """
            定位梦想计划[残忍终止]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'id',
            'android_value': 'com.laijin.simplefinance:id/btn_stop',
        })

    def stop_dream_plan_complete_button_loc(self):
        """
            定位终止梦想计划[完成]
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/btn_complete',
        })