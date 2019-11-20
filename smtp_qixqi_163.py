# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

'''
    使用自己的域名邮箱发送邮件
        管理员  qixqi@qixqi.club
        密码    a17411419150580
'''

# 第三方邮件服务器
# mail_host = 'smtp.163.com'
mail_host = 'mail.qixqi.club'
mail_port = 25
mail_user = 'qixqi@qixqi.club'
mail_pass = 'a17411419150580'


sender = 'qixqi@qixqi.club'
receivers = ['2510591928@qq.com']

message = MIMEText('利用域名邮箱发送邮件 qixqi@qixqi.club', 'plain', 'utf-8')
message['From'] = 'qixqi<qixqi@qixqi.club>'
message['To'] = '2510591928@qq.com'

subject = '利用域名邮箱发送邮件, qixqi@qixqi.club'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, mail_port)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error, 邮件发送失败')


