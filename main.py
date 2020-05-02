import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from conf.conf_dir import testcases_dir
from common.clean import *
from common.send_email import *
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
report_name = "API_TestReports_{0}.html".format(curTime)
with open(r"{0}/{1}".format(htmlreports_dir, report_name), "wb") as fs:
    #实例化HTMLTestRunner
    runner = HTMLTestRunner(stream=fs, title="接口自动化测试报告", tester="xiao zhai")
    #运行测试用例
    runner.run(suite)

send_email(report_name)


