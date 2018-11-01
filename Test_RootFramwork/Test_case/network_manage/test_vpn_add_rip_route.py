#coding:utf-8
import unittest
from selenium import webdriver
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class add_rip_route2(unittest.TestCase):
    '''添加rip路由'''
    def setUp(self):
        pass
    def test_add_rip_route3(self):
        '''界面点击'''
        add_rip_route()
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()
