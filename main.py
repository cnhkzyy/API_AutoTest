import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from conf.conf_dir import testcases_dir
from common.clean import *
import time


#实例化TestSuite
suite = unittest.TestSuite()
#实例化TestLoader
loader = unittest.TestLoader()
#采用loader的discover方法收集测试用例，并将其加载到测试套件中
suite.addTests(loader.discover(testcases_dir))

#设置当前时间
curTime = time.strftime("%Y-%m-%d_%H-%M-%S")

#创建一个html文件
with open(r"{0}/API_TestReports_{1}.html".format(htmlreports_dir, curTime), "wb") as fs:
    #实例化HTMLTestRunner
    runner = HTMLTestRunner(stream=fs, title="接口自动化测试报告", tester="xiao zhai")
    #运行测试用例
    runner.run(suite)


