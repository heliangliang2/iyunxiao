#coding:utf-8
import unittest
from selenium import webdriver
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class user_login1(unittest.TestCase):
    '''用户名、密码登录测试'''
    def setUp(self):
        pass
    def test_usera_login(self):
        '''正确的用户名密码登录'''
        username="adm"
        password="adm"
        aa=user_login(username,password)
        self.assertEqual(aa,True)
    def test_userb_login(self):
        '''错误的用户名密码登录'''
        username="ad"
        password="ad"
        aa=user_login(username,password)
        self.assertIn(aa,"所使用的账户不存")
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()
    