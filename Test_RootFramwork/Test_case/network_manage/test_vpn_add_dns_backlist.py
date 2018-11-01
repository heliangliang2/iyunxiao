#coding:utf-8
import unittest,time
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class add_dns_backlist(unittest.TestCase):
    '''dns代理黑名单'''
    def setUp(self):
        pass
    def test_add_dns_backlist(self):
        '''正确的配置'''
        add_domain="hll.com"
        vpn_add_dns_backlist(add_domain)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()