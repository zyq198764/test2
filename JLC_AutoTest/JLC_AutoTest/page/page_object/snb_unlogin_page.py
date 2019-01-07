from JLC_AutoTest.page.page_ui_object.snb_unlogin_page_ui import Snb_UnLoginPageUI


#登录页面的元素
class SNB_Unlogin_page(Snb_UnLoginPageUI):
    """
        页面对象(PO): 未登陆首页
    """

    def get_Unlogin_Title_Loc_page(self):
        """
            获取未登陆首页title
        :return:
        """
        return self.get_Unlogin_Title_Loc().text

    def get_unlogin_banner_loc_page(self):
        """
            获取未登陆首页banner
        :return:
        """
        return self.get_unlogin_banner_loc().click()


    def get_unlogin_lowriskfundtext_loc_page(self):
        """
            获取"低风险基金组合产品"的文案
        :return:
        """
        return self.get_unlogin_lowriskfundtext_loc().text

    def get_unlogin_lic_fundsales_loc_page(self):
        """
            获取"与正规持牌机构奕丰金融基金销售合作"文案
        :return:
        """
        return self.get_unlogin_lic_fundsales_loc().text

    def get_unlogin_certicode_loc_page(self):
        """
           获取证书编码
        :return:
        """
        return self.get_unlogin_certicode_loc().text



    def get_unlogin_midtext_loc_page(self):
        """
            获取"低风险 低手续费 500元起投"文案
        :return:
        """
        return self.get_unlogin_midtext_loc().text

    def get_unlogin_lssyltext_loc_page(self):
        """
             获取7.43%文案
        :return:
        """
        return self.get_unlogin_lssyltext_loc().text

    def get_unlogin_reedmunlimited_loc_page(self):
        """
             获取赎回无限制的文本
        :return:
        """
        return self.get_unlogin_reedmunlimited_loc().text

    def get_unlogin_buynow_button_loc_page(self):
        """
             点击立即买入按钮
        :return:
        """
        return self.get_unlogin_buynow_button_loc().click()

    def get_unlogin_scholarship_loc_page(self):
        """
             获取"你有10元奖学金可领取"按钮,可点击
        :return:
        """
        return self.get_unlogin_scholarship_loc().click()
    def get_unlogin_Histor_loc_page(self):
        """
        定位"历史平均万元日收益"文案
        :return:
        """
        return  self.get_unlogin_Histor_loc().text

    def get_unlogin_historicalpos_loc_page(self):
        """
            获取"历史正收益天数占比"文案
        :return:
        """
        return self.get_unlogin_historicalpos_loc().text

