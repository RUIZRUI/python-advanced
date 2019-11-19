# -*- coding: utf-8 -*-

'''
    使用第三方邮件服务器 smtp.163.com 发送带有附件的邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


# 第三方的 SMTP 服务
mail_host = 'smtp.163.com'      # 服务器
mail_user = 'zhengxiang4056@163.com'      # 用户名
mail_pass = 'a17411419150580'      # 口令

sender = 'zhengxiang4056@163.com'
receivers = ['2510591928@qq.com']

# 创建一个带有附件的实例
message = MIMEMultipart()
message['From'] = 'qixqi<zhengxiang4056@163.com>'
message['To'] = '2510591928@qq.com'
subject = 'Python SMTP 带有附件的邮件'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文
message.attach(MIMEText('这是qixqi Python 邮件发送测试 ...', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 smtp_attachment1.txt文件
attach1 = MIMEText(open('smtp_attachment1.txt', 'rb').read(), 'base64', 'utf-8')
attach1['Content-Type'] = 'application/octet-stream'
# 这里的filename可以任意写
attach1['Content-Disposition'] = 'attachment; filename="qixqi.txt"'
message.attach(attach1)

# 构造附件2，传送当前目录下的 smtp_attachment2.txt文件
attach2 = MIMEText(open('smtp_attachment2.txt', 'rb').read(), 'base64', 'utf-8')
attach2['Content-Type'] = 'application/octet-stream'
attach2['Content-Disposition'] = 'attachment; filename="zhengxiang.txt"'
message.attach(attach2)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error, 无法发送邮件')
