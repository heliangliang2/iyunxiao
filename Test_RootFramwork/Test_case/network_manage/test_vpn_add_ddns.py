#coding:utf-8
import unittest,time
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from selenium import webdriver
from function.test_vpn_farmwork_function import *
class add_ddns2(unittest.TestCase):
    '''添加希网ddns服务'''
    def setUp(self):
        pass
    def test_add_ddns(self):
        '''正确的配置'''
        add_ddns_domain="hll.com"
        add_dns_username="aa"
        add_dns_password="aa"
        add_ddns_services(add_ddns_domain,add_dns_username,add_dns_password)
    def test_add_ddns1(self):
        '''域名为空,正确的用户名密码'''
        add_ddns_domain1=""
        add_dns_username1="aa"
        add_dns_password1="aa"
        add_ddns_services(add_ddns_domain1,add_dns_username1,add_dns_password1)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()