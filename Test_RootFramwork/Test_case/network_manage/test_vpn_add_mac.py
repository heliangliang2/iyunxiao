#coding:utf-8
import time
import unittest
from  selenium import webdriver
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class add_ipmask(unittest.TestCase):
    '''添加IPMac'''
    def setUp(self):
        pass
    def test_add_ipmask(self):
        '''正确的格式'''
        add_ip="2.2.2.2"
        add_mac="60:45:CB:61:49:17"
        netmanager_add_ipmask(add_ip,add_mac)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()