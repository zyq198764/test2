#!/usr/bin/env python
#coding=utf-8
#运行所有的测试用例
import os
import threading
import unittest
import time
from JLC_AutoTest.common.HTMLTestRunner_jpg import HTMLTestRunner
from JLC_AutoTest.common.run_server import RunServer
from JLC_AutoTest.common.settings import  log,MACACA_PORT,REPORT_PATH,CASE_PATH



if __name__ == '__main__':
    # # 启动服务
    #
    # log.info('开始启动服务')
    # RunServer(MACACA_PORT).run()
    # time.sleep(10)
    # print("3232")


    discover = unittest.defaultTestLoader.discover(CASE_PATH, "snb*.py")#运行所有以snb开头的用例
    print("11")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    file_name = now + 'resut.html'
    run = HTMLTestRunner(title='拾年宝 UI自动化测试报告',
                         description='业务回归测试',
                         stream=open(REPORT_PATH + '/' + file_name, 'wb'),
                         retry=1)

    run.run(discover)

