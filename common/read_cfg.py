from configparser import ConfigParser
from conf.conf_dir import conf_dir

#初始化类
cp = ConfigParser()
cp.read(r"{0}\db.cfg".format(conf_dir))

#得到第一个section
section = cp.sections()[0]

#得到该session的所有option
#print(cp.options(section))

#得到该section的所有键值对
#print(cp.items(section))

#得到该section的option的值
#print(cp.get(section, "db"))
host = cp.get(section, "host")
port = cp.getint(section, "port")
db = cp.get(section, "db")
user = cp.get(section, "user")
password = cp.get(section, "password")


#得到该section的option的值，返回值为int类型
#print(cp.getint(section, "port"))