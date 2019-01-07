from JLC_AutoTest.model.base import Base


class SetPageUI(Base):
    """
        页面UI对象（PUO）：设置页面UI
    """
    def set_button_loc(self):
        """
            定位[设置]按钮
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '',
            'android_by': 'wait_id',
            'android_value': 'com.laijin.simplefinance:id/setting_iv',
        })