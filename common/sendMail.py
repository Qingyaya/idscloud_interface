
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from common.ReadConfig import ReadConfig
from common.Log import Log

log=Log()
rc=ReadConfig()
def send_mail(report_file):
    sender=rc.get_email('sender')
    psw=rc.get_email('psw')
    receiver=rc.get_email('receiver')
    smtpserver=rc.get_email('smtp_server')
    port=rc.get_email('port')
    with open(report_file,'rb') as f:
        mailbody = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mailbody, _subtype='html', _charset='utf-8')
    msg['Subject'] = u'自动化测试报告'
    msg['from'] = sender
    msg['To'] = ', '.join(eval(receiver))
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename = "TestReport.html"'
    msg.attach(att)

    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    # 用户名密码
    try:
        smtp.login(sender, psw)
        smtp.sendmail(sender, eval(receiver), msg.as_string())
        log.info('Send mail Success!!! test report email has send out!')
    except Exception as e:
        log.error('Send Mail Failed !!! error: %s' %e)
    smtp.quit()


if __name__ == '__main__':

    report_file='E:\\IDScloud_ui_demo\\report\\20180517\\20180517100220.html'
    send_mail(report_file)
