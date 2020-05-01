from common.random_generate import *
from common.context import *
import re


class ReplaceVariable:

    def replace_variable(params):
        if params.find("${") != -1:
            replace_string = eval("RandomGenerate().random_{0}()".format(re.sub("\d+", "", re.findall("\${(\\w+)}", params)[0])))
            params = re.sub("\${\\w+}", replace_string, params)
        elif params.find("{{") != -1:
            replace_string = eval("Context.{0}".format(re.findall("{{(\\w+)}}", params)[0]))
            params = re.sub("{{\\w+}}", replace_string, params)
        return params