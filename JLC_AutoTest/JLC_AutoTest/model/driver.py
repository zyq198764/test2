from macaca import WebDriver #启动macaca测试用例需要导入webdriver
import JLC_AutoTest.globalvar

def drivers(): #定义一个driver的方法
    """
    根据全局平台参数返回对应的驱动
    :return: WebDriver对象
    """
    desired_caps = {} #定义一个空字典
    if JLC_AutoTest.globalvar.platform == 'ios':
        # 把iOS字典的键/值对更新到desired_caps里
        desired_caps.update(JLC_AutoTest.globalvar.ios_capabilities)  #如果平台是ios，就把ios的配置更新到字典中
    elif JLC_AutoTest.globalvar.platform == 'android':
        # 把Android字典的键/值对更新到desired_caps里
        desired_caps.update(JLC_AutoTest.globalvar.android_capabilities)
    else:
        pass
    # 修改字典中已有键/值对
    # desired_caps['app'] = globalvar.global_path + 'app/' + desired_caps['app']
    # 配置所需的功能和服务器URL的WebDriver对象
    driver = WebDriver(desired_caps, JLC_AutoTest.globalvar.server_url) #初始化webdriver服务器
    return driver
