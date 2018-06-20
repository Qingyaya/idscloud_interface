
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from public.Log import Log
from datas.setting import *

log=Log()
def send_mail(report_file):
    with open(report_file,'rb') as f:
        mailbody = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mailbody, _subtype='html', _charset='utf-8')
    msg['Subject'] = u'自动化测试报告'
    msg['from'] = Sender
    msg['To'] = ', '.join(Receiver)
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename = "TestReport.html"'
    msg.attach(att)

    try:
        smtp = smtplib.SMTP_SSL(SMTP_server, Port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(SMTP_server, Port)
    # 用户名密码
    try:
        smtp.login(Sender, Psw)
        smtp.sendmail(Sender, Receiver, msg.as_string())
        log.info('Send mail Success!!! test report email has send out!')
    except Exception as e:
        log.error('Send Mail Failed !!! error: %s' %e)
    smtp.quit()


