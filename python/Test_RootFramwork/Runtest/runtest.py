from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

import smtplib,unittest,time,os

#=========定义发送邮件==========
def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header("自动化测试报告",'utf-8')
    smtp_server='smtp.qq.com'
    smtp=smtplib.SMTP_SSL(smtp_server,465)
    # smtp.connect(smtpserver)
    smtp.login("2463731436@qq.com","ntxkwohzexlqeaha")
    smtp.sendmail("2463731436@qq.com","1344711361@qq.com",msg.as_string())
    smtp.quit()
    print ("email has send out ")
#========检查测试报告目录，找到最新生成的测试报告文件==========
def new_report (testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+"\\"+fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new
if __name__=='__main__':
    test_dir='C:\\Users\\Administrator\\Desktop\\test\\python\\test_project\\test_case\\'
    test_report='C:\\Users\\Administrator\\Desktop\\test\\python\\test_project\\report\\'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    # now =time.strftime("%Y-%m-%d_%H_%M_%S")
    filename=test_report+'\\'+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')
    runner.run(discover)
    fp.close()

    new_report=new_report(test_report)
    send_mail(new_report)

    #通过unittest框架的discover找到匹配测试用例，有htmltestrunner的run方法执行测试用例并生成最新的测试报告
    #调用new——report函数找到测试报告目录report，下最新生成的测试报告，返回测试报告的路径
    #将得到的最新测试报告的完整路径传给send_mail函数，实现发邮件功能



