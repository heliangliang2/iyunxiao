#coding:utf-8
import unittest,time
from selenium import webdriver
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class add_dns_whitelist1(unittest.TestCase):
    '''DNS代理白名单'''
    def setUp(self):
        pass
    def test_add_dns_whitelist(self):
        add_whitelist_ip="1.1.1.1"
        add_whitelist_domain="hll.com"
        add_dns_whitelist(add_whitelist_ip,add_whitelist_domain)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()