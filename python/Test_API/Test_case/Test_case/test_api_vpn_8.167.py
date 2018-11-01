#conding:utf-8
import requests
#禁用安全请求警告

#登录Jenkins

url="https://172.18.8.167:8888/cgi-bin/index.cgi"
header={
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN",
    # "User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "X-Requested-With": "XMLHttpRequest"
}
data={
    "type":"loginCheck",
    "user":"adm",
    "pwd":"adm"
}
jension={
    "JSON":"type"
}
s=requests.session()
r=s.post(url,headers=header,json=jension,data=data,verify=False)
print(r.status_code)
print(r.content)
print(s.cookies)


#添加cookies
# c=requests.cookies.RequestsCookieJar()
# c.set("sw_login_user_name","adm")
# c.set("sw_login_session_id","1678151169")
# c.set("sw_login_role_info","255")
# c.set("sw_login_role_name","administrator")
# s.cookies.update(c)
# print(s.cookies)


#添加接口
url2="https://172.18.8.167:8888/cgi-bin/netManage/netInterface.cgi"
header={
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN",
    # "User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "X-Requested-With": "XMLHttpRequest"
}
body={
    "type":"setConfigInfo",
    "eth":"eth2",
    "ip":"2.2.5.2",
    "mast":"255.255.255.0",
    "gateway":"0.0.0.0",
    "linkWeight":"0",
    "userName":"N",
    "password":"N",
    "br":"null",
    "onBoot":"1",
    "mtu":"0",
    "mac":"00:00:00:00:00:00",
    "mode":"1",
    "probe_addr":"0.0.0.0"
}
jens={
    "JSON":"type"
}
r2=requests.session()
s2=r2.post(url2,headers=header,json=jens,data=body,verify=False)
print(s2.status_code)
print(s2.content)
print(s2.cookies)


