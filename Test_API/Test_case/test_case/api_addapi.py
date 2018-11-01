# #conding:utf-8
# import requests
# # #禁用安全请求警告
# import urllib3
# urllib3.disable_warnings()
# url="https://192.168.1.123:8888/cgi-bin/index.cgi"
# #url地址   https://172.18.8.167:8888/cgi-bin/index.cgi
# header={
#     "Accept":"application/json,text/javascript,*/*;q=0.01",
#     "Accept-Encoding":"gzip,deflate",
#     "Accept-Language":"zh-CN",
#     "X-Requested-With":"XMLHttpRequest"
# }
# data={
#     "type":"loginCheck",
#     "user":"adm",
#     "pwd":"adm"
# }
# s=requests.session()
# r=s.post(url,headers=header,data=data,verify=False)
# print (r.content)
# # #,json=jension
# # # print('网页的状态码是%s'%(r.status_code))
# # print('网页的内容是%s'%(r.content))
# # print(type(r.content))
# # # #字节流转化字典
# # str1=str(r.content,encoding="utf-8")
# # # # print(type(str1))
# # print ('字节流转化成字符串%s'%(str1))
# # data2=eval(str1)
# # # # print(type(data2))
# # print('字符串转化成字典%s'%(data2))
# # print(data2['session_id'])
# # # # 添加cookies
# # c=requests.cookies.RequestsCookieJar()
# # c.set("sw_login_user_name","adm")
# # c.set("sw_login_session_id",data2['session_id'])
# # c.set("sw_login_role_info","255")
# # c.set("sw_login_role_name","administrator")
# # s.cookies.update(c)
# # print(s.cookies)


# # # # 添加接口
# # url2="https://172.18.8.167:8888/cgi-bin/netManage/netInterface.cgi"
# # header={
# #     "Accept": "application/json, text/javascript, */*; q=0.01",
# #     "Accept-Encoding": "gzip, deflate",
# #     "Accept-Language": "zh-CN",
# #     # "User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
# #     "X-Requested-With": "XMLHttpRequest"
# # }
# # body={
# #     "type":"setConfigInfo",
# #     "eth":"eth2",
# #     "ip":"2.2.10.50",
# #     "mast":"255.255.255.0",
# #     "gateway":"0.0.0.0",
# #     "linkWeight":"0",
# #     "userName":"N",
# #     "password":"N",
# #     "br":"null",
# #     "onBoot":"1",
# #     "mtu":"0",
# #     "mac":"00:00:00:00:00:00",
# #     "mode":"1",
# #     "probe_addr":"0.0.0.0"
# # }
# # s2=s.post(url2,data=body,verify=False)
# # print('添加接口页面的状态码%s'%(s2.status_code))
# # print('添加接口页面内容是%s'%(s2.content))



# # # #页面刷新保存
# # # # url3="https://172.18.8.167:8888/cgi-bin/netManage/netInterface.cgi"
# # # # body3={
# # # #     "type":"tableRefresh"
# # # # }
# # # # s3=s.post(url3,data=body3,verify=False)
# # # # print ('页面状态码是%s'%(s3.status_code))

# # # #添加路由
# # # url3="https://192.168.1.123:8888/cgi-bin/netManage/netRouter/netRouter.cgi"
# # # #https://172.18.8.167:8888/cgi-bin/netManage/netRouter/netRouter.cgi
# # # # header2={
# # # #     "Accept": "application/xml, text/xml, */*; q=0.01",
# # # #     "Accept-Encoding": "gzip,deflate",
# # # #     "Accept-Language": "zh-CN",
# # # #     # "User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
# # # #     "X-Requested-With": "XMLHttpRequest"
# # # # }
# # # data3={
# # #     "type":"addStaticRoute",
# # #     "nexthop":"2.2.34.89",
# # #     "metric":"23",
# # #     "mast":"255.255.255.255",
# # #     "eth":"eth0",
# # #     "dest":"1.1.1.5"
# # # }
# # # addroute=s.post(url3,data=data3,verify=False)
# # # print('添加路由界面状态码为%s'%(addroute.status_code))
# # # print('添加路由界面内容为%s'%(addroute.content))


# # # #添加DNS代理
# # # url4="https://192.168.1.123:8888/cgi-bin/netManage/netDnsSet.cgi"
# # # data4={
# # #     "type":"add_server",
# # #     "ip":"2.2.3.2"
# # # }
# # # DNSagi=s.post(url4,data=data4,verify=False)
# # # print('DNS代理设置%s'%(DNSagi.content))
