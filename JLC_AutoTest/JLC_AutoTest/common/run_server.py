import threading #多线程模块
import os
from JLC_AutoTest.common import settings
#启动macaca 服务
class RunServer(threading.Thread):#继承多线程类

    def __init__(self, port):#定义构造函数
        threading.Thread.__init__(self)
        self.cmd = 'macaca server -p %s --verbose' % port

    def run(self):
        os.system(self.cmd) #相当于在cmd中执行self.cmd的命令

if __name__ == '__main__':
    runServer = RunServer(settings.MACACA_PORT)
    runServer.run() #启动服务