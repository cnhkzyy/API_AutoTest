from configparser import ConfigParser
from conf.conf_dir import conf_dir

#初始化类
cp = ConfigParser()
cp.read(r"{0}\env.cfg".format(conf_dir), encoding="utf-8")

#得到第一个section
mysql_section, host_section, email_section = cp.sections()


#获取mysql section的option值
def get_mysql_options():
    host = cp.get(mysql_section, "host")
    port = cp.getint(mysql_section, "port")
    db = cp.get(mysql_section, "db")
    user = cp.get(mysql_section, "user")
    password = cp.get(mysql_section, "password")
    return host, port, db, user, password


#获取host section的option值
def get_host_section():
    test_host = cp.get(host_section, "test_host")
    sql_host = cp.get(host_section, "sql_host")
    return test_host, sql_host


#获取email的option值
def get_email_section():
    From = cp.get(email_section, "From")
    to = cp.get(email_section, "to")
    subject = cp.get(email_section, "subject")
    text = cp.get(email_section, "text")
    smtp_host = cp.get(email_section, "smtp_host")
    smtp_port = cp.get(email_section, "smtp_port")
    user = cp.get(email_section, "user")
    password = cp.get(email_section, "password")
    return From, to, subject, text, smtp_host, smtp_port, user, password




#得到该session的所有option
#print(cp.options(section))

#得到该section的所有键值对
#print(cp.items(section))

#得到该section的option的值
#print(cp.get(section, "db"))



#得到该section的option的值，返回值为int类型
#print(cp.getint(section, "port"))