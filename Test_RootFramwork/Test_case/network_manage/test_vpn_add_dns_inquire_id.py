#coding:utf-8
import unittest,time
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class add_inquire_dns(unittest.TestCase):
    '''查询服务器'''
    def setUp(self):
        pass
    def test_add_inquire_dns(self):
        '''正确的配置'''
        dns_inquire_ip="2.2.2.3"
        vpn_dns_inquire(dns_inquire_ip)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()