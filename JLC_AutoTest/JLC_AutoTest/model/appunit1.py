from retrying import retry
import unittest
from macaca import WebDriver
#进行版本升级安装的版本
# from JLC_AutoTest.model.driver import drivers
desired_caps = {
    # 'platformName': 'iOS',
    # 'deviceName': 'iPhone',
    # 'reuse':1,
    # 'app': '//Users//jlc//Downloads//JLC_AutoTest//JLC_AutoTest//app//SimpleFinance2.app',
    # 'udid':'4a9870983826da23f474d45f30ac7cb156d3d114',
    # 'bundleId': 'com.jianlcvip.simplefinance.3.9.7',
    'bundleId': 'com.jianlcvip.simplefinance.3.9.7',  # 应用的bundleId
    'platformName': 'iOS',
    'udid': '4a9870983826da23f474d45f30ac7cb156d3d114',
    # 'udid':'0d03437a9f45e177eaf71a5caca2a59faa54461f',
    'app': '//Users//jlc/Downloads//JLC_AutoTest//JLC_AutoTest//app//SimpleFinance4.0.0zhenji.app',
    'autoAcceptalert': 'true',
    'reuse':'2',#运行完成后保持app状态

}




server_url = {
    'hostname': 'localhost',
    'port': 3456
}

#unittest来组织测试用例
class MacacaTest(unittest.TestCase):
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