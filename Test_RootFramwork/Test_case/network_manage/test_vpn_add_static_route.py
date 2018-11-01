#coding:utf-8
import unittest
from selenium import webdriver
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class add_static_route2(unittest.TestCase):
    '''添加静态路由'''
    def setUp(self):
        pass
    def test_add_static_route(self):
        '''正确的配置'''
        add_ip="1.1.1.1"
        add_gw="1.1.1.2"
        add_mertic="12"
        add_static_route(add_ip,add_gw,add_mertic)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()