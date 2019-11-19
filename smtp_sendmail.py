# -*- coding: utf-8 -*-

# 创建 smtp 对象
# smtpObj = smtplib.SMTP(host, port, local_name)


# smtp 对象发送邮件
# SMTP.sendmail(from_addr, to_addr, msg)
# to_addr 字符串列表，邮件发送地址
# msg: 发送的消息，字符串，注意格式


import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 第三方的 SMTP 服务
mail_host = 'smtp.163.com'      # 服务器
mail_user = 'zhengxiang4056@163.com'      # 用户名
mail_pass = 'a17411419150580'      # 口令



sender = 'zhengxiang4056@163.com'
receivers = ['2510591928@qq.com']   # 接收者列表

# MIMEText(文本内容, 文本格式, 编码) 
message = MIMEText('Python 邮件发送中 ...', 'plain', 'utf-8')
message['From'] = Header('zhengxiang4056@163.com', 'utf-8')      # 发送者
message['To'] = Header('2510591928@qq.com', 'utf-8')          # 接收者

subject = 'Python SMTP 邮件'
message['Subject'] = Header(subject, 'utf-8')


# try:
    # smtpObj = smtplib.SMTP('localhost')
    # smtpObj.sendmail(sender, receivers, message.as_string())
    # print('邮件发送成功')

    # 使用第三方 SMTP 服务
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)      # SMTP 端口号
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
smtpObj.close()
print('邮件发送成功')
# except smtplib.SMTPException:
    # print('Error: 无法发送邮件')
