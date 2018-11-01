#coding:utf-8
import unittest
from selenium import webdriver
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
import time
class add_policy_route2(unittest.TestCase):
    '''添加策略路由'''
    def setUp(self):
        pass
    def test_add_policy_route(self):
        '''正确的格式配置'''
        username="adm"
        password="adm"
        user_login(username,password)
        add_src_ip="1.1.1.1"
        add_src_mask="255.255.255.255"
        add_dst_ip="1.1.1.5"
        add_dst_mask="255.255.255.255"
        add_gateway="1.1.1.9"
        add_policy_route(add_src_ip,add_src_mask,add_dst_ip,add_dst_mask,add_gateway)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()