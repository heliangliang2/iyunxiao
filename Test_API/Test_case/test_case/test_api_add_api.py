#coding:utf-8
import unittest
import requests
from test_login_function import  api_vpn_login,api_add_cookies,test_api_add
class test_api_vpn(unittest.TestCase):
    '''添加接口'''
    def setup(self):
        print("开始添加接口")
        print("------------------------------------")
    def test_vpn_add_api(self):
        '''正确的IP地址和子网掩码'''
        username='adm'
        password='adm'
        result=api_vpn_login().testapi_vpn_login(username,password)
        data_session=result['session_id']
        api_add_cookies().api_add_cookies(data_session)
        add_ip="1.1.1.4"
        add_msat="255.255.224.0"
        result2=test_api_add().api_add1(add_ip,add_msat)
        print(type(result2))
        print("获取的登录界面内容是%s"%(result2))   
        self.assertEqual()
    def tearDown(self):
        print("------------------------------------")
        print("添加接口结束")
if __name__=="__main__":
    unittest.main()
