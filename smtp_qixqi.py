# -*- coding: utf-8 -*-

'''
    利用 qixqi.club 服务器充当第三方邮件服务器发送邮件
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 第三方邮件服务器
mail_host = 'mail.qixqi.club'
mail_port = 25
mail_user = 'zhengxiang@qixqi.club'
mail_pass = '123456'

sender = 'zhengxiang@qixqi.club'
receivers = ['2510591928@qq.com']

message = MIMEText('qixqi.club 第三方邮件服务器发送邮件', 'plain', 'utf-8')
message['From'] = 'zhengxiang<zhengxiang@qixqi.club>'
message['To'] = '2510591928@qq.com'

subject = 'qixqi.club 第三方服务器发送邮件'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, mail_port)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功，请注意到垃圾箱中查收')
except smtplib.SMTPException:
    print('Error, 邮件发送失败')