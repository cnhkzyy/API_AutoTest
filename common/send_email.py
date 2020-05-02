import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from conf.conf_dir import htmlreports_dir
from common.read_cfg import *



#读取配置
From, to, subject, text, smtp_host, smtp_port, user, password = get_email_section()


def send_email(report_name):
    msg = MIMEMultipart()
    msg["From"] = From
    msg["To"] = to
    msg["Subject"] = subject

    #添加文本内容
    msg_sub = MIMEText(text, _charset="utf-8")
    msg.attach(msg_sub)

    #将html作为附件
    with open(f"{htmlreports_dir}/{report_name}", encoding="utf-8") as fs:
        html_content = fs.read()
        msg_html = MIMEText(html_content, "html", "utf-8")
        msg_html.add_header("Content-Disposition", "attachment", filename=report_name)
        msg.attach(msg_html)


    #邮件发送
    s = smtplib.SMTP_SSL(smtp_host, smtp_port)
    s.set_debuglevel(1)
    s.login(user, password)
    s.sendmail(msg["From"], msg["To"], msg.as_string())
    s.close()