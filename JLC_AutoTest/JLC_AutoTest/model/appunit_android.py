import unittest
import time
from macaca import WebDriver
from retrying import retry
from macaca  import WebElement

# desired_caps = {
#   #模拟器上的配置
#     'platformName': 'android',  # 当前用例运行的平台
#     'package': 'com.laijin.simplefinance',
#     'activity': '.ykmain.activity.YKMainActivity',
#     'app':'//Users//jlc//Downloads//JLC_AutoTest//JLC_AutoTest//app//app-debug-v3.9.9.apk',
#     'reuse':0,
#     'autoAcceptalert':'True',
#     'deviceName':'192.168.56.101:5555'
# # 0: 启动并安装 app。{1 (默认): 卸载并重装 app。 2: 仅重装 app。3: 在测试结束后保持 app 状态。}
#     }

desired_caps = {
  #真机上的配置
    'platformName': 'android',  # 当前用例运行的平台
    # 'package': 'com.laijin.simplefinance',
    # 'activity': '.ykmain.activity.YKMainActivity',
    'app':'//Users//jlc//Downloads//JLC_AutoTest//JLC_AutoTest//app//app-debug-v3.9.9-64_399_jiagu_sign.apk',
    'reuse':2,
    'autoAcceptalert':'True',
# 0: 启动并安装 app。{1 (默认): 卸载并重装 app。 2: 仅重装 app。3: 在测试结束后保持 app 状态。}
    }
server_url = {
    'hostname': 'localhost',
    'port': 3456
}

def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
    return driver

def switch_to_native(driver):
    contexts = driver.contexts
    driver.context = contexts[0]
    return driver

class MacacaTest_android(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.initDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    @retry
    def initDriver(cls):
        print("Retry connecting server...")
        cls.driver.init()
