# -*- coding: utf-8 -*-

'''
    使用第三方邮件服务器 smtp.qq.com 发送邮件
'''


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


# 第三方邮件服务器
mail_host = 'smtp.qq.com'
mail_port = '465'
mail_user = '2826791069@qq.com'
mail_pass = 'qcyagwzeklerdhcg'      # 授权码

sender = '2826791069@qq.com'
receivers = '2510591928@qq.com'

message = MIMEText('第三方邮件服务器 smtp.qq.com', 'plain', 'utf-8')
message['From'] = formataddr(['qixqi', sender])     # 发件人昵称，发件人邮箱
message['To'] = formataddr(['翼婕', receivers])      # 收件人昵称，收件人邮箱
message['Subject'] = 'qixqi 发送邮件测试'             # 邮件的主题

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)   # ssl
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, [receivers,], message.as_string())
    smtpObj.quit()
    print('邮件发送成功')
except Exception:
    print('Error, 邮件发送失败')