from JLC_AutoTest.model.base import Base


class VersionUpdatePageUi(Base):


    """
        页面UI对象（PUO）：关于版本更新页面的UI

    """
    def boot_age_loc(self):
        """
            进入到启动页面，滑完四张启动屏幕时，点击页面，进入到未登陆首页页面
        :return:
        """
        return  self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]',
            'android_by': 'xpath',
            'android_value': '//android.widget.FrameLayout[1]',
        })
    def  enter_jlc_page(self):
        """
          点击底部的简理财的按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'main bottombar home normal',
            'android_by': '',
            'android_value': '',
        })
    def unlogin_page_loc(self):
        """
          在未登陆首页，点击空白处
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[6]',
            'android_by': '',
            'android_value': '',
        })

    def enter_my_page_loc(self):

        """
            进入到我的页面
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'main bottombar account normal',
            'android_by': 'xpath',
            'android_value': '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView[1]',
        })

    def about_button_loc(self):
        '''
         点击我的--关于
        :return:
        '''
        return self.selector({
            'ios_by':'xpath',
            'ios_value':'//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[12]',
            'android_by':'xpath',
            'android_value':'//*[@resource-id="com.laijin.simplefinance:id/about_ll"]'
        })

    def version_update_loc(self):
        """
            进入到关于页面，点击版本更新
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[5]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/setting_check_update_ll"]',
        })

    def version_update_text(self):
        """
            如果当前是最新版本,获取文本内容
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]',
            'android_by': '',
            'android_value': '',
        })

    def version_update_confirm_loc(self):
        """
            点击版本更新弹窗中的确定按钮
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]',
            'android_by': '',
            'android_value': '',
        })

    def version_update_Elastic_layer(self):
        """
            设置版本非强制升级后，进入到App首页，弹出非强制升级的弹层
            定位弹层中的"立即体验按钮"
        :return:
        """
        return  self.selector({
            'ios_by':'name',
            'ios_value':'versionupdate button normal',
            'android_by':'',
            'android_value':'',
        })

    def version_update_Remind_Me_Later(self):
        """
            点击非强制升级弹层中的"稍后提醒我"，弹层消失
        :return:
        """
        self.selector({
            'ios_by': 'name',
            'ios_value': '或稍后提醒我',
            'android_by': '',
            'android_value': '',
        })
    def version_app_store(self):
        """
          进入到appstore,点击返回主包-3.9.7，返回到app 内
        :return:
        """
        self.selector({
            'ios_by': 'name',
            'ios_value': '返回“主包-3.9.8”',
            'android_by': '',
            'android_value': '',
        })