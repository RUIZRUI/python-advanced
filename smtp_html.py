# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

'''
    使用第三方邮件服务器 smtp.163.com 发送hmtl格式的邮件
'''


# 第三方的 SMTP 服务
mail_host = 'smtp.163.com'      # 服务器
mail_user = 'zhengxiang4056@163.com'      # 用户名
mail_pass = 'a17411419150580'      # 口令

sender = 'zhengxiang4056@163.com'
receivers = ['2510591928@qq.com']

mail_msg = '''
<p>Python 邮件发送测试...</p>
<p><a href="https://www.qixqi.club">《菊次郎的夏天》</a></p>
'''

message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = 'qixqi<zhengxiang4056@163.com>'
message['To'] = '2510591928@qq.com'

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')



try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()
    print('邮件发送成功，请注意垃圾箱查看')
except smtplib.SMTPException:
    print('Error: 无法发送邮件')