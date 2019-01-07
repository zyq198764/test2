from JLC_AutoTest.model.base import Base


class UnloginHomePageUi(Base):


    """
        页面UI对象（PUO）：未登录主页页面上半部分UI
    """
    def yindao_button_loc(self):

        """
            定位[引导页]按钮
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[7]',
            'android_by': '',
            'android_value': '',})

    def  boot_page_loc(self):
        '''
         定位引导页，启动App时，先显示引导页面，点击后引导页消失，进入到未登录首页
        :return:
        '''
        return self.selector({
            'ios_by':'xpth',
            'ios_value':'',
            'android_by':'id',
            'android_value':'id/iv_yk_app_start'
        })
    def unlogin_button_loc(self):
        """
            定位[注册登录]按钮
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[7]',
            'android_by': '',
            'android_value': '',
        })

    def sevenDayYield(self):
        """
            定位七日年华
            newInterest_sevenDayYield
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'newInterest_sevenDayYield',
            'android_by': '',
            'android_value': '',
        })

    def liaojiegengduo(self):
        """
            定位了解更多
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '了解更多',
            'android_by': '',
            'android_value': '',
        })

    def Unlogin_banner(self):
        """
            定位未登录banner
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]',
            'android_by': '',
            'android_value': '',
        })

    # def enter_my_page_loc(self):
    #
    #     """
    #         进入到我的页面
    #     :return:
    #     """
    #     return self.selector({
    #         'ios_by': 'xpath',
    #         'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeButton[4]',
    #         'android_by': '',
    #         'android_value': '',
    #     })

    # def about_button_loc(self):
    #     '''
    #      点击我的--关于
    #     :return:
    #     '''
    #     return self.selector({
    #         'ios_by':'xpth',
    #         'ios_value':'//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[12]',
    #         'android_by':'',
    #         'android_value':''
    #     })
    #
    # def version_update_loc(self):
    #     """
    #         进入到关于页面，点击版本更新
    #     :return:
    #     """
    #     return self.selector({
    #         'ios_by': 'xpath',
    #         'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[5]',
    #         'android_by': '',
    #         'android_value': '',
    #     })
    #
    # def version_update_text(self):
    #     """
    #         如果当前是最新版本,获取文本内容
    #     :return:
    #     """
    #     return self.selector({
    #         'ios_by': 'name',
    #         'ios_value': '当前已是最新版本哦',
    #         'android_by': '',
    #         'android_value': '',
    #     })
    #
    # def version_update_confirm_loc(self):
    #     """
    #         点击版本更新弹窗中的确定按钮
    #     :return:
    #     """
    #     return self.selector({
    #         'ios_by': 'xpath',
    #         'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]',
    #         'android_by': '',
    #         'android_value': '',
    #     })
