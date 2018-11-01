import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#发送邮箱服务器
smtp_server='smtp.qq.com'
#发送邮箱
sender='2463731436@qq.com'
#接收邮箱
receiver='1344711361@qq.com'
#发送邮箱用户、密码
user='2463731436@qq.com'
password='ntxkwohzexlqeaha'
#邮箱主题
subject='python test'
#发送的附件
sendfile=open('D:\\python自动化脚本\\test_project\\test_case\\result.html','rb').read()

att=MIMEText(sendfile,'base64','utf-8')
att["Content-Type"]='application/octet-stream'
att["Content-Disposition"]='attachment; filename=="result.html"'
msgRoot=MIMEMultipart('related')
msgRoot['Subject']=subject
msgRoot.attach(att)

#连接发送邮件
# smtp=smtplib.SMTP()
smtp=smtplib.SMTP_SSL(smtp_server,465)
# smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()
print("邮件发送成功")