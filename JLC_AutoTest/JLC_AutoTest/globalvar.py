# 项目绝对路径
# 获取App的package/activity adb logcat | grep START

# global_path = '/Users/jlc/PycharmProjects/JLC_AutoTest/'

# 服务器URL
server_url = 'http://localhost:3456/wd/hub'

# 配置iOS的参数
# ios_capabilities = {
#     # 'platformName': 'iOS',
#     # 'deviceName': 'iPhone',
#     # 'reuse':1,
#     # 'app': '//Users//jlc//Downloads//JLC_AutoTest//JLC_AutoTest//app//SimpleFinance2.app',
#     # 'udid':'4a9870983826da23f474d45f30ac7cb156d3d114',
#     # 'bundleId': 'com.jianlcvip.simplefinance.3.9.7',
#     'bundleId': 'com.jianlcvip.simplefinance.3.9.7', #应用的bundleId
#     'platformName': 'iOS',
#     'udid': '4a9870983826da23f474d45f30ac7cb156d3d114',
#     # 'udid':'0d03437a9f45e177eaf71a5caca2a59faa54461f',
#     # 'app':'//Users//jlc/Downloads//JLC_AutoTest//JLC_AutoTest//app//SimpleFinance2.app',
#     'app':'//Users//jlc/Downloads//JLC_AutoTest//JLC_AutoTest//app//SimpleFinance2.app',
#     'autoAcceptalert':'true',
#     'reuse':'3',#运行完成后保持app状态
#
# }
# #升级使用的参数
# ios_capabilities1 = {
#     # 'platformName': 'iOS',
#     # 'deviceName': 'iPhone',
#     # 'reuse':1,
#     # 'app': '//Users//jlc//Downloads//JLC_AutoTest//JLC_AutoTest//app//SimpleFinance2.app',
#     # 'udid':'4a9870983826da23f474d45f30ac7cb156d3d114',
#     # 'bundleId': 'com.jianlcvip.simplefinance.3.9.7',
#     'bundleId': 'com.jianlcvip.simplefinance.3.9.7', #应用的bundleId
#     'platformName': 'iOS',
#     'udid': '4a9870983826da23f474d45f30ac7cb156d3d114',
#     'app':'//Users//jlc/Downloads//JLC_AutoTest//JLC_AutoTest//app//SimpleFinance4.0.0zhenji.app',
#     'autoAcceptalert':'true',
#     # 'reuse':'3',#运行完成后保持app状态
#     # 0: 清楚数据并重装app。1: (默认) 卸载并重装 app。2: 仅重装 app。3: 在测试结束后保持app状态
#
# }

# 配置Android的参数
# android_capabilities = {
#     'platformName': 'android',
#     'app': 'app-debug-v3.9.0-55-jianlicai.apk',
# }
#模拟器启动App
# android_capabilities = {
#     'platformName': 'android',  # 当前用例运行的平台
#     'package': 'com.laijin.simplefinance',
#     'activity': '.ykmain.activity.YKMainActivity',
#     'app':'//Users//jlc//Downloads//JLC_AutoTest//JLC_AutoTest//app//app-debug-v3.9.8-63.apk',
#     'deviceName':'192.168.56.101:5555',
#     'reuse':0
#
# # 0: 启动并安装 app。{1 (默认): 卸载并重装 app。 2: 仅重装 app。3: 在测试结束后保持 app 状态。}
# }
#真机启动App
android_capabilities = {
    'platformName': 'android',  # 当前用例运行的平台
    # 'package': 'com.laijin.simplefinance',
    # 'activity': '.ykmain.activity.YKMainActivity',
    'app':'//Users//jlc//Downloads//JLC_AutoTest//JLC_AutoTest//app//app-debug-v3.9.8-63_398_jiagu_sign.apk',
    'reuse':3
}

# android_capabilities = {
#     'platformName': 'android',
#     'app':'//Users//jlc//Downloads//JLC_AutoTest//JLC_AutoTest//app//app-debug-v3.9.8-63.apk',
#     # 'permissionPatterns': '[\\"安装\\",\\"允许\\"]'[\"继续安装\",\"下一步\",\"好\",\"允许\",\"确定\",\"我知道\"]
#     'permissionPatterns':'[\"继续安装\",\"下一步\",\"好\",\"允许\",\"确定\",\"我知道\"]',
#     'reuse': 3
#     }
# 测试平台（android/ios）
# platform = 'ios'
platform = 'android'