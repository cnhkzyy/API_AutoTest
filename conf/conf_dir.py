import os

conf_dir = os.path.split(os.path.abspath(__file__))[0]

htmlreports_dir = conf_dir.replace("conf", "html_reports")

testcases_dir = conf_dir.replace("conf", "test_cases")

testdatas_dir = conf_dir.replace("conf", "test_datas")

logs_dir = conf_dir.replace("conf", "logs")
