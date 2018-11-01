#coding:utf-8
import unittest,time
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class edit_dns_ip2(unittest.TestCase):
    '''修改修改查询服务器'''
    def setUp(self):
        pass
    def test_edit_dns_agent(self):
        '''正确的配置'''
        edit_dns="2.2.2.2"
        edit_dns_inquire(edit_dns)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()