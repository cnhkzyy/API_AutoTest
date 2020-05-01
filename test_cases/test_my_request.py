import unittest
import ddt
import re
import json
from jsonpath import jsonpath
from common.do_excel import DoExcel
from common.replace_variable import ReplaceVariable
from common.context import Context
from common.my_request import *


@ddt.ddt
class TestMyRequest(unittest.TestCase):
    do_excel = DoExcel(r"E:\virtual_workshop\Python_API\test_datas\api_info.xlsx")
    all_case_data = do_excel.read_all_caseData()


    @ddt.data(*all_case_data)
    def test_my_request(self, case_data):

       for i in range(len(case_data["case_id"])):

            #替换请求参数
            request_data = json.loads(ReplaceVariable.replace_variable(case_data["request_data"][i]))


            #请求数据反射
            request_extract = case_data["request_extract"][i]
            if request_extract:
                key, express = request_extract.split("=")
                setattr(Context, key, jsonpath(request_data, express)[0])


            if case_data["method"][i].lower() == "get":
                result = send_request(case_data["method"][i], case_data["url"][i], params=request_data)
            elif case_data["method"][i].lower() == "post":
                result = send_request(case_data["method"][i], case_data["url"][i], data=request_data)


            #响应数据反射
            response_extract = case_data["response_extract"][i]
            if response_extract:
                key, express = response_extract.split("=")
                setattr(Context, key, str(jsonpath(result, express)[0]))


            #断言
            for key, value in case_data["check"][i].items():
                #替换期望结果
                value = ReplaceVariable.replace_variable(value)
                self.assertEqual(str(jsonpath(result, key)[0]), value)


