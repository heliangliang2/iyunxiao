#coding:utf-8
import requests
url="http://localhost:8080/j_acegi_security_check"
header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
d={
    "j_username":"hll",
    "j_password":"111111",
    "from":"/",     
    "Jenkins-Crumb":"d8f207fd53abcd5233aa524a4d21fa7b",
    "json":{"j_username": "hll", "j_password": "111111","remember_me": "false","from": "/", "Jenkins-Crumb": "d8f207fd53abcd5233aa524a4d21fa7b"},
    "Submit":"登录"
}
s=requests.session()
r=s.post(url,headers=header,allow_redirects=True,data=d)
# print (r.content)
print(r.status_code)

#登录成功后，创建项目
url2="http://localhost:8080/view/all/createItem"
data2={
    'name':'test1',
    'mode':'hudson.model.FreeStyleProject',
    'from':'',
    'Jenkins-Crumb':'9fa2269fc5a14dca69efece78d935f75',
    'json':{"name": "test1", "mode": "hudson.model.FreeStyleProject", "from": "", "Jenkins-Crumb": "9fa2269fc5a14dca69efece78d935f75"},
}
r2=s.post(url2,data=data2)
print(r2.status_code)
url3="http://localhost:8080/job/test1/configSubmit"
# data3={
#     '':'',
# }
# s.get("http://localhost:8080/view/all/checkJobName?value=test1")
# s.get("http://localhost:8080/job/test/configure")
# s.get("http://localhost:8080/job/test/descriptorByName/jenkins.branch.RateLimitBranchProperty$JobPropertyImpl/checkCount?value=1&durationName=")
print(r2.content)


# new_url=r.headers["location"]
# print(new_url)
# # 正则表达式提取账号和登录按钮
# import re
# t=re.findall(r'.注销',r.content)
# print (t)
# # print (t[1])