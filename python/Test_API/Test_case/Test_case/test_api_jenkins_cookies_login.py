#coding:utf-8
import requests
url="http://localhost:8080/login?from=%2F"
headers={
    # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
}
s=requests.session()
r=s.get(url,headers=headers)
print (s.cookies)

#添加登录的cookie

ckk=requests.cookies.RequestsCookieJar()
# ckk.set('JSESSIONID.9ab6704c','node0r22gbhf3z1pe19nmu40bqmrj664.node0')
ckk.set('JSESSIONID.9ab6704c','node0raii3vxwudqb12dbqmegy78pa70.node0')
ckk.set('screenResolution','1600x900')
ckk.set('ACEGI_SECURITY_HASHED_REMEMBER_ME_COOKIE','aGxsOjE1MzA3MDI1OTIzMTM6Nzc3ZWMyNzQ1OTBmYTM0NmJhYTEzMzIxMzFkZDNiOWRlNTNjNzMyYjA0NzY3MGExMzI5MWUwN2YzZjAwY2NhYw==')
s.cookies.update(ckk)
print (s.cookies)


