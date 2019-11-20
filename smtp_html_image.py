# -*- coding: utf-8 -*-

'''
    邮件的html文本中一般邮件服务商添加外链是无效的，正确添加图片格式如下
'''

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


# 第三方邮件服务器
mail_host = 'smtp.163.com'
mail_user = 'zhengxiang4056@163.com'
mail_pass = 'a17411419150580'

sender = 'zhengxiang4056@163.com'
receivers = ['2510591928@qq.com']

message = MIMEMultipart('related')
message['From'] = 'qixqi<zhengxiang4056@163.com>'
message['To'] = '2510591928@qq.com'
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)


mail_msg = '''
<p>Python 邮件发送测试 ...</p>
<p><a href="https://www.qixqi.club">《菊次郎的夏天》</a></p>
<p>图片演示：</p>
<p><img src="cid:image1" /></p>
<br />
<br />
<p>如果在垃圾箱可能需要移动到收件箱才可以正确显示</p>
'''
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录下
fp = open('smtp_html_image.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID, 在html文本中引用
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()
    print('邮件发送成功，请注意垃圾箱中查看')
    print('如果在垃圾箱可能需要移动到收件箱才可以正确显示')
except smtplib.SMTPException:
    print('Error, 无法发送邮件')