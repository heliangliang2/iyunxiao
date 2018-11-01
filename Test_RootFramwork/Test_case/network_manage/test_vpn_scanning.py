#coding:utf-8
import unittest
import time
from selenium import webdriver
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
# sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class ipmask_scanning2(unittest.TestCase):
    '''IPMac扫描和绑定'''
    def setUp(self):
        pass
    def test_ipmask_scanning(self):
        
        ipmac_scanning()
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()