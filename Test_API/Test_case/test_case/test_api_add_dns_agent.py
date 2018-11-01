#conding:utf-8
import requests
import unittest
from test_login_function import  api_vpn_login,api_add_cookies,api_vpn_add_dns_agent
class test_add_dns_agent(unittest.TestCase):
    '''添加DNS代理'''
    def setUp(self):
        print("开始添加dns代理")
    def test_add_dns_agent(self):
        '''正确的IP地址'''
        username='adm'
        password='adm'
        result=api_vpn_login().testapi_vpn_login(username,password)
        data_session=result['session_id']
        api_add_cookies().api_add_cookies(data_session)
        dns_address="1.1.1.6"
        result2=api_vpn_add_dns_agent().add_dns_agent(dns_address)
        print(result2)
        self.assertEqual(result2['msg'],'0','添加失败')
    def tearDown(self):
        print ("dns添加结束")
if __name__=="__main__":
    unittest.main()



