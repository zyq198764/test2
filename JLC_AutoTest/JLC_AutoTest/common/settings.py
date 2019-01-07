#所有的公共参数都放在这个文件中

import  os
import nnlog  #写日志的模块

#redis的参数信息
REDIS_INFO={
        'host':'10.103.27.200',
        'port':'6379',
        'password':'123456',
        'db':'0',
        'decode_response':'True'
}


#数据库的连接信息
MY_SQL_INFO  = {
    'host':'10.103.27.10',
    'port':3306,
    'password':"123123",
    'db':'test3_product',
    'user':'',
    'charset':'utf8',
    'autocommit':True
}


#__file__ 代表的就是当前这个python文件
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #取到程序的主目录

LOG_FILE = os.path.join(BASE_PATH,'files/logs','server.log')  #写日志的路径

log = nnlog.Logger(LOG_FILE,when='S') #调用写日志的方法

#保存截图的路径
SCREENSHOT_FILE = os.path.join(BASE_PATH,'files/screenshot')

#macaca服务的端口号
MACACA_PORT=3456


REPORT_PATH = os.path.join(BASE_PATH, 'files/report')  # 获取测试报告存放的路径

CASE_PATH= os.path.join(BASE_PATH, 'test_case')  # 获取测试用例的路径

