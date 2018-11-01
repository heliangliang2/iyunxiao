#coding:utf-8
import requests
# r=requests.get("http://www.baidu.com")
# print(r.status_code)
#账号密码登录
url="http://172.18.9.248/mantis/login_page.php"
headers={
        "Content-Length":"72",
        "Referer":"http://172.18.9.248/mantis/login_page.php",
        "Origin":"http://172.18.9.248",
        "Upgrade-Insecure-Requests":"1",
        "Connection":"keep-alive",
        "Host":"172.18.9.248"
        }
data={"return":"index.php",
    "username":"heliangliang",
    "password":"123456",
    "secure_session":"on"
    }
# r=requests.get(url,headers=headers,verify=False)
# print(r.status_code)
s=requests.session()
r=s.post(url,data=data)
print(r.status_code)
# print(r.content) 
print (s.cookies)