#coding:utf-8
import requests
url="http://localhost:8080/j_acegi_security_check "
header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
d={
    "j_username":"hll",
    "j_password":"111111",
    "from":"/",
    "Jenkins-Crumb":"d8f207fd53abcd5233aa524a4d21fa7b",
    "json":{"j_username": "hll", "j_password": "111111", "remember_me": "false", "from": "/", "Jenkins-Crumb": "d8f207fd53abcd5233aa524a4d21fa7b"},
    "Submit":"登录"
}
s=requests.session()
r=s.post(url,headers=header,data=d)
print (r.content)