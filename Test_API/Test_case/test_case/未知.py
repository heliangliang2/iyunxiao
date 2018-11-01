# #conding:utf-8
# import requests
# import urllib3
# urllib3.disable_warnings()
# # # class api_vpn_login():
# # #     def testapi_vpn_login(self,username,password):
# # #         header={
# # #             "Accept":"application/json,text/javascript,*/*;q=0.01",
# # #             "Accept-Encoding":"gzip,deflate",
# # #             "Accept-Language":"zh-CN",
# # #             "X-Requested-With":"XMLHttpRequest"
# # #         }
# # #         url="https://172.18.21.156:8888/cgi-bin/index.cgi"
# # #         data={
# # #             "type":"loginCheck",
# # #             "user":username,
# # #             "pwd":password
# # #         }
# # #         s=requests.session()
# # #         r=s.post(url,headers=header,data=data,verify=False)
# # #         # print('登录界面状态码是%s'%(r.status_code))
# # #         # print('登录后页面内容是%s'%(r.content))
# # #         print("调试1")
# # #         # str1=r.json()
# # #         # print('获取到的session_ID是%s'%(str1['session_id']))
# # #         return r.json()
# # # class api_add_cookies():
# # #     def api_add_cookies(self,data_session):
# # #         c=requests.cookies.RequestsCookieJar()
# # #         c.set("sw_login_user_name","adm")
# # #         c.set("sw_login_session_id",data_session)
# # #         c.set("sw_login_role_info","255")
# # #         c.set("sw_login_role_name","administrator")
# # #         s=requests.session()
# # #         s.cookies.update(c)
# # #         # print("第二步添加cookies")
# # #         print("调试2")
# # #         return s.cookies
# # # class test_api_add():
# # #     def api_add1(self,add_ip,add_msat):
# # #         username='adm'
# # #         password='adm'
# # #         r=api_vpn_login().testapi_vpn_login(username,password)
# # #         data_session=r['session_id']
# # #         print("开始登录")
# # #         r1=api_add_cookies().api_add_cookies(data_session)
# # #         print(r1)
# # #         url="https://172.18.21.156:8888/cgi-bin/netManage/netInterface.cgi"
# # #         header={
# # #             "Accept":"application/xml,text/xml,*/*;q=0.01",
# # #             "Accept-Encoding":"gzip,deflate",
# # #             "Accept-Language":"zh-CN",
# # #             "X-Requested-With":"XMLHttpRequest"
# # #         }
# # #         body={

# # #             "type":"setConfigInfo",
# # #             "eth":"eth2",
# # #             "ip":add_ip,
# # #             "mast":add_msat,
# # #             "gateway":"0.0.0.0",
# # #             "linkWeight":"0",
# # #             # "userName":"N",
# # #             # "password":"N",
# # #             "br":"null",
# # #             "onBoot":"1",
# # #             "mtu":"0",
# # #             "mac":"00:00:00:00:00:00",
# # #             "mode":"1",
# # #             # "probe_addr":"0.0.0.0"
# # #         }
# # #         s=requests.post(url,headers=header,data=body,verify=False)
# # #         # print("开始添加接口地址")
# # #         print("调试3")
# # #         return s.content

# # #         #成功添加接口
# # #         # url="https://172.18.8.167:8888/cgi-bin/index.cgi"
# # #         # header={
# # #         #     "Accept":"application/json,text/javascript,*/*;q=0.01",
# # #         #     "Accept-Encoding":"gzip,deflate",
# # #         #     # "User-Agent":"Mozilla/5.0(Windows NT 6.1;WOW64;Trident/7.0;rv:11.0)likeGecko",
# # #         #     "Accept-Language":"zh-CN",
# # #         #     "X-Requested-With":"XMLHttpRequest"
# # #         # }
# # #         # data={
# # #         #     "type":"loginCheck",
# # #         #     "user":"adm",
# # #         #     "pwd":"adm"
# # #         # }
# # #         # jension={
# # #         #     "JSON":"type"
# # #         # }
# # #         # s=requests.session()
# # #         # r=s.post(url,headers=header,json=jension,data=data,verify=False)
# # #         # data2=r.json()
# # #         # print('获取的session_id是%s'%(data2['session_id']))
# # #         # c=requests.cookies.RequestsCookieJar()
# # #         # c.set("sw_login_user_name","adm")
# # #         # c.set("sw_login_session_id",data2['session_id'])
# # #         # c.set("sw_login_role_info","255")
# # #         # c.set("sw_login_role_name","administrator")
# # #         # s.cookies.update(c)
# # #         # print(s.cookies)


# # #         # # 添加接口
# # #         # url2="https://172.18.8.167:8888/cgi-bin/netManage/netInterface.cgi"
# # #         # header={
# # #         #     "Accept": "application/json, text/javascript, */*; q=0.01",
# # #         #     "Accept-Encoding": "gzip, deflate",
# # #         #     "Accept-Language": "zh-CN",
# # #         #     # "User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
# # #         #     "X-Requested-With": "XMLHttpRequest"
# # #         # }
# # #         # body={
# # #         #     "type":"setConfigInfo",
# # #         #     "eth":"eth2",
# # #         #     "ip":add_ip,
# # #         #     "mast":add_msat,
# # #         #     "gateway":"0.0.0.0",
# # #         #     "linkWeight":"0",
# # #         #     "userName":"N",
# # #         #     "password":"N",
# # #         #     "br":"null",
# # #         #     "onBoot":"1",
# # #         #     "mtu":"0",
# # #         #     "mac":"00:00:00:00:00:00",
# # #         #     "mode":"1",
# # #         #     "probe_addr":"0.0.0.0"
# # #         # }
# # #         # s2=s.post(url2,data=body,verify=False)
# # #         # print('添加接口页面的状态码%s'%(s2.status_code))
# # #         # print('添加接口页面内容是%s'%(s2.content))
# # #         # return s2.content
# url="https://192.168.1.123:8888/cgi-bin/index.cgi"
# #url地址   https://172.18.8.167:8888/cgi-bin/index.cgi
# header1={
#     "Accept":"application/json,text/javascript,*/*;q=0.01",
#     "Accept-Encoding":"gzip,deflate",
#     "User-Agent":"Mozilla/5.0(Windows NT 6.1;WOW64;Trident/7.0;rv:11.0)likeGecko",
#     "Accept-Language":"zh-CN",
#     "X-Requested-With":"XMLHttpRequest"
# }
# data1={
#     "type":"loginCheck",
#     "user":"adm",
#     "pwd":"adm"
# }
# # data={
# #     "type":"loginCheck",
# #     "pwd":"adm",
# #     "user":"adm"
# # }

# s=requests.session()
# r=s.post(url,headers=header1,data=data1,verify=False)
# print (r.json())
# #,json=jension
# # print('网页的状态码是%s'%(r.status_code))
# print('网页的内容是%s'%(r.content))
# print(type(r.content))
# # #字节流转化字典
# str1=str(r.content,encoding="utf-8")
# # # print(type(str1))
# print ('字节流转化成字符串%s'%(str1))
# data2=eval(str1)
# # # print(type(data2))
# print('字符串转化成字典%s'%(data2))
# print(data2['session_id'])
# # # 添加cookies
# c=requests.cookies.RequestsCookieJar()
# c.set("sw_login_user_name","adm")
# c.set("sw_login_session_id",data2['session_id'])
# c.set("sw_login_role_info","255")
# c.set("sw_login_role_name","administrator")
# s.cookies.update(c)
# print(s.cookies)
# url_1="https://192.168.1.123:8888/cgi-bin/netManage/netInterface.cgi"
#     # https://192.168.1.123:8888/cgi-bin/netManage/netInterface.cgi
#     # "https://192.168.1.123:8888/cgi-bin/netManage/netInterface.cgi"
# header2={
#     "Accept":"application/xml,text/xml,*/*;q=0.01",
#     "Accept-Encoding":"gzip,deflate,br",
#     "Accept-Language":"zh-CN,zh;q=0.9",
#     # "User-Agent":"Mozilla/5.0(Windows NT 6.1;WOW64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/67.0.3396.99Safari/537.36",
#     "X-Requested-With":"XMLHttpRequest"
# }
# body={
#     "type":"subDelete",
#     "eth":"eth2:0"
# }
# r1=s.post(url_1,headers=header2,data=body)
# # return r.content
# print (r1.content)





# #     