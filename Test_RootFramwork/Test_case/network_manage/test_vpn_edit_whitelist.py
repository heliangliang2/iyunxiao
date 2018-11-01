#coding:utf-8
import unittest,time
from selenium import webdriver
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class edit_whitelist(unittest.TestCase):
    '''修改白名单'''
    def setUp(self):
        pass
    def test_edit_whitelist2(self):
        '''正确的配置'''
        edit_whitelist_ip2="3.3.3.3"
        edit_whitelist_domain2="hll2.com"
        edit_dns_whitelist(edit_whitelist_ip2,edit_whitelist_domain2)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()