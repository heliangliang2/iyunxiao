#coding:utf-8
import unittest,time
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class add_dns_agent(unittest.TestCase):
    '''dns设置'''
    def setUp(self):
        pass
    def test_add_dns_agent(self):
        '''正确的配置'''
        dns1="114.114.114.114"
        dns2="202.103.24.68"
        dns3="1.1.1.1"
        vpn_add_dns_agent(dns1,dns2,dns3)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()