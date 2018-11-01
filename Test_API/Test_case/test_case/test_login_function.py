#coding:utf-8
import requests
import urllib3
urllib3.disable_warnings()
s=requests.session()
class api_vpn_login_session_cookies():
    def login_session_cookies(self):
        username='adm'
        password='adm'
        aa=api_vpn_login().testapi_vpn_login(username,password)
        a1=api_add_cookies().api_add_cookies(aa['session_id'])
        return (a1)
class api_vpn_login():
    '''用户名，口令登录'''
    def testapi_vpn_login(self,username,password):
        header={
            "Accept":"application/json,text/javascript,*/*;q=0.01",
            "Accept-Encoding":"gzip,deflate",
            "Accept-Language":"zh-CN",
            "X-Requested-With":"XMLHttpRequest"
        }
        url="https://192.168.1.123:8888/cgi-bin/index.cgi"
        data={
            "type":"loginCheck",
            "user":username,
            "pwd":password
        }
        s=requests.session()
        r=s.post(url,headers=header,data=data,verify=False)
        print('登录界面状态码是%s'%(r.status_code))
        # print('登录后页面内容是%s'%(r.content))
        print("登录函数被调用")
        return r.json()
class api_add_cookies():
    '''添加cookies'''
    def api_add_cookies(self,data_session):
        c=requests.cookies.RequestsCookieJar()
        c.set("sw_login_user_name","adm")
        c.set("sw_login_session_id",data_session)
        c.set("sw_login_role_info","255")
        c.set("sw_login_role_name","administrator")
        s.cookies.update(c)
        print("cookies被添加")
        return s.cookies
class test_api_add():
    '''添加接口'''
    def api_add1(self,add_ip,add_msat):
        url="https://192.168.1.123:8888/cgi-bin/netManage/netInterface.cgi"
        header={
            "Accept":"application/xml,text/xml,*/*;q=0.01",
            "Accept-Encoding":"gzip,deflate",
            "Accept-Language":"zh-CN",
            "X-Requested-With":"XMLHttpRequest"
        }
        body={

            "type":"setConfigInfo",
            "eth":"eth2",
            "ip":add_ip,
            "mast":add_msat,
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
        s1=s.post(url,headers=header,data=body,verify=False)
        print("接口地址被添加")
        return s1.content
class api_vpn_add_dns_agent():
    '''添加DNS代理'''
    def add_dns_agent(self,dns_address):
        url="https://192.168.1.123:8888/cgi-bin/netManage/netDnsSet.cgi"
        header={
            "Accept":"application/json,text/javascript,*/*;q=0.01",
            "Accept-Encoding":"gzip,deflate",
            "Accept-Language":"zh-CN",
            "X-Requested-With":"XMLHttpRequest",
        }
        body={
            "type":"add_server",
            "ip":dns_address
        }
        r=s.post(url,headers=header,data=body,verify=False)
        print(r.content)
        print ("添加DNS代理函数被调用")
        return  (r.json())
class api_add_chlidrenApi():
    '''添加子接口'''
    def add_chlidren_api(self,chlidren_ip,chlidren_mask):
        url="https://192.168.1.123:8888/cgi-bin/netManage/netInterface.cgi"
        header={
            "Accept":"application/xml,text/xml,*/*;q=0.01",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN",
            "X-Requested-With":"XMLHttpRequest"
        }
        body={
            "type":"subAdd",
            "eth":"eth2",
            "ip":chlidren_ip,
            "mask":chlidren_mask
        }
        r=s.post(url,headers=header,data=body,verify=False)
        print(r.content)
        print(type(r))
        print("添加子接口函数被调用")
        
        return (r.content)
class delete_chlidrenapi():
    '''删除子接口'''
    def vpn_delete_chlidrenapi(self,eth,try_count=1):
        url="https://192.168.1.123:8888/cgi-bin/netManage/netInterface.cgi"
        header={
            "Accept":"application/xml,text/xml,*/*;q=0.01",
            "Accept-Encoding":"gzip,deflate,br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "X-Requested-With":"XMLHttpRequest"
        }
        body={
            "type":"subDelete",
            "eth":eth
        }
        json={
            "JSON":"type"
        }
        r=s.post(url,headers=header,allow_redirects=False,json=json,data=body,timeout=10)
        return r.content
class getallsubbyname():
    '''获取所有的接口信息'''
    def getallsub(self):
        url="https://192.168.1.123:8888/cgi-bin/netManage/netInterface.cgi"
        header={
            "Accept":"application/xml,text/xml,*/*;q=0.01",
            "Accept-Encoding":"gzip,deflate,br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "User-Agent":"Mozilla/5.0(Windows NT 6.1;WOW64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/67.0.3396.99Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
            }
        body={
            "type":"getAllSubByName",
            "name":"eth2"
        }
        r=s.post(url,headers=header,data=body,allow_redirects=False,verify=False,timeout=10)
        print ("成功获取子接口列表")
        return (r.content)
class edit_chlidrenapi():
    '''修改子接口配置'''
    def edit_chlidrenapi(self,edit_ip,edit_mask):
        url="https://192.168.1.123:8888/cgi-bin/netManage/netInterface.cgi"
        header={
            "Accept":"application/xml,text/xml,*/*;q=0.01",
            "Accept-Encoding":"gzip,deflate,br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "X-Requested-With":"XMLHttpRequest"
        }
        body={
            "type":"subModify",
            "eth":"eth2.0",
            "ip":edit_ip,
            "mask":edit_mask
        }
        r=s.post(url,headers=header,data=body,verify=False)
        return r.content
class stop_childrenapi():
    def stop_chilrenapi(self,stop_eth):
        url="https://192.168.1.123:8888/cgi-bin/netManage/netInterface.cgi"
        header={
            "Accept":"application/xml,text/xml,*/*;q=0.01",
            "Accept-Encoding":"gzip,deflate,br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "X-Requested-With":"XMLHttpRequest"
        }
        body={
            "type":"subStop",
            "eth":stop_eth
        }
        r=s.post(url,headers=header,data=body,verify=False)
        return r.content
class add_default_route():
    def add_route (self,route_dest,route_mast,route_nexthop,route_metric):
        url="https://192.168.1.123:8888/cgi-bin/netManage/netRouter/netRouter.cgi"
        headers={
            "Accept":"application/xml,text/xml,*/*;q=0.01",
            "Accept-Encoding":"gzip,deflate,br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "X-Requested-With":"XMLHttpRequest"
        }
        body={
            "type":"addStaticRoute",
            "dest":route_dest,
            "mast":route_mast,
            "nexthop":route_nexthop,
            "metric":route_metric,
            "eth":"eth2"
        }
        r=s.post(url,headers=headers,data=body,verify=False)
        return r.content

    