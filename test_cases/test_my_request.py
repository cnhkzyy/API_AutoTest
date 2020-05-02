import unittest
import ddt
import json
from jsonpath import jsonpath
from common.do_excel import DoExcel
from common.replace_variable import ReplaceVariable
from common.context import Context
from common.my_request import *
from common.my_logging import *
from common.read_cfg import *
import logging


@ddt.ddt
class TestMyRequest(unittest.TestCase):
    do_excel = DoExcel(r"{0}\api_info.xlsx".format(testdatas_dir))
    all_case_data = do_excel.read_all_caseData()
    #读取配置文件
    test_host, sql_host = get_host_section()

    @ddt.data(*all_case_data)
    def test_my_request(self, case_data):


        logging.info("用例『{0}』测试开始了".format(case_data["case_desc"][0]))
        for i in range(len(case_data["case_id"])):

            #拼接url
            if case_data["host"][i] == "test":
                case_data["url"][i] = self.test_host + case_data["url"][i]
            elif case_data["host"][i] == "sql":
                case_data["url"][i] = self.sql_host + case_data["url"][i]

            #替换请求参数
            request_data = json.loads(ReplaceVariable.replace_variable(case_data["request_data"][i]))
            logging.info("请求数据: {0}".format(request_data))

            #请求数据反射
            request_extract = case_data["request_extract"][i]
            if request_extract:
                key, express = request_extract.split("=")
                setattr(Context, key, jsonpath(request_data, express)[0])


            if case_data["method"][i].lower() == "get":
                result = send_request(case_data["method"][i], case_data["url"][i], params=request_data)
            elif case_data["method"][i].lower() == "post":
                result = send_request(case_data["method"][i], case_data["url"][i], data=request_data)
            logging.info("响应结果: {0}".format(result))

            #响应数据反射
            response_extract = case_data["response_extract"][i]
            if response_extract:
                key, express = response_extract.split("=")
                setattr(Context, key, str(jsonpath(result, express)[0]))


            #断言
            for key, value in case_data["check"][i].items():
                #替换期望结果
                actual = str(jsonpath(result, key)[0])
                expect = ReplaceVariable.replace_variable(value)
                logging.info("实际结果: {0}".format(actual))
                logging.info("期望结果: {0}".format(expect))
                self.assertEqual(actual, expect)

        logging.info("\n\n")






