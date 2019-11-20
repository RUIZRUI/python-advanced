# -*- coding: utf-8 -*-

'''
    利用自己的服务器 qixqi.club 服务器本地发送邮件
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'qixqi@qixqi.club'
receivers = ['2510591928@qq.com']

message = MIMEText('qixqi.club 服务器发送邮件测试', 'plain', 'utf-8')
message['From'] = 'qixqi<qixqi@qixqi.club>'
message['To'] = '2510591928@qq.com'

subject = 'qixqi.club 发送邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功，请注意垃圾箱查看')
except smtplib.SMTPException:
    print('Error, 邮件发送失败')