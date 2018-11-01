#coding:utf-8
import unittest
from selenium import webdriver
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
import time
class add_ospf_route2(unittest.TestCase):
    '''添加ospf路由'''
    def  setUp(self):
        pass
    def test_add_ospf_route(self):
        '''正确的配置'''
        add_route_ip="0.0.0.0"
        add_network="1.1.1.1"
        add_network_mask="24"
        add_ospf_route(add_route_ip,add_network,add_network_mask)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()