from JLC_AutoTest.common import  settings
import os

# curt_path=os.path.dirname(os.path.abspath(__file__))  #获取当前路径的父目录/Users/jlc/Downloads/JLC_AutoTest/JLC_AutoTest/common


#定义保存截图的函数
def save_img(driver=None, file_name=None):
    """
    截图并保存到图片目录
    :param driver: WebDriver对象
    :param file_name: 截图文件名
    """
    # 将多个路径组合成截图存放路径
    file_path = settings.SCREENSHOT_FILE+'/'+file_name + '.png'

    # 将截图保存到本地
    driver.save_screenshot(file_path)
