# coding:utf-8
import unittest
import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def createSuite():
    testunit = unittest.TestSuite()
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py',
                                                   top_level_dir=None)
    for test_class in discover:
        for test_case in test_class:
            testunit.addTests(test_case)
    return testunit


def send_mail(new_report):
    sender = 'eddie@bertadata.com'
    receiver = 'eddie@bertadata.com'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'WebDemo Testing Result'

    f = open(new_report, 'rb')
    mail_body = f.read()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg.attach(body)
    f.close()

    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com')
    smtp.login('eddie@bertadata.com', ' ')
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

    # msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    # msg['Subject']='WebDemo Testing Result'
    # msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    # smtp = smtplib.SMTP()
    # smtp.connect('smtp.exmail.qq.com')
    # smtp.login('eddie@bertadata.com','')
    # smtp.sendmail(sender,receiver, msg.as_string())
    # smtp.quit()


def send_report(test_dir):
    rpt_dir = test_dir
    lists = os.listdir(rpt_dir)
    lists.sort(key=lambda fn: os.path.getmtime(rpt_dir + "\\" + fn))
    new_report = os.path.join(rpt_dir, lists[-1])
    send_mail(new_report)


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H.%M.%S')
    rptname = '../report/' + now + ' result.html'
    with open(rptname, 'wb') as rpt:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=rpt,
            title=u"测试报告",
            description=u"执行结果"
        )
        runner.run(createSuite())
    send_report('../report')
