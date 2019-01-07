import JLC_AutoTest.model.driver
from JLC_AutoTest.page.page_ui_object.version_update_page_ui import VersionUpdatePageUi

class VersionUpdatePage(VersionUpdatePageUi):


    def click_boot_page_button(self):
        """
        点击启动屏的第四张图片，进入到未登陆首页
        :return:
        """
        self.boot_age_loc().click()

    def click_unlogin_jlc_page(self):
        """
        点击未登陆首页的简理财tab
        :return:
        """
        self.enter_jlc_page().click()
    def click_unlogin_page(self):
        """
        点击未登陆首页的空白处
        :return:
        """
        self.unlogin_page_loc().click()

    def click_my_button(self):
        """
        点击我的进入到我的页面
        :return:
        """
        self.enter_my_page_loc().click()

    def click_about_button(self):
        """
        点击我的--关于进入到关于页面
        :return:
        """

        self.about_button_loc().click()


    def click_version_button(self):
        """
        点击我的--关于-版本检查进入到版本检测页面
        :return:
        """
        self.version_update_loc().click()

    def click_version_text_button(self):
        """
        点击我的--关于-版本检查进入到版本检测页面，获取text的值
        :return:
        """
        self.version_update_text().text
    def click_version_confirm_button(self):
        """
        点击我的--关于-版本检查进入到版本检测页面，点击确定按钮
        :return:
        """
        self.version_update_confirm_loc().click()

    def click_version_update_Elastic_layer(self):
        """
          点击升级中的立即体验，进入都Appstore页面
        :return:
        """
        self.version_update_Elastic_layer().click()

    def click_version_update_Remind_Me_Later(self):
        """
          点击非强制升级中的稍后提醒我，弹层消失
        :return:
        """
        self.version_update_Remind_Me_Later().text
    def click_version_app_store(self):
        """
           从Appstore中点击返回App，进入到App首页
        :return:
        """

        self.version_app_store().click()

