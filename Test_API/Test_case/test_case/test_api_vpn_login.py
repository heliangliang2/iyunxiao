#coding:utf-8
import unittest
import requests
import urllib3
urllib3.disable_warnings()
from test_login_function import api_vpn_login
class api_vpn(unittest.TestCase):
    '''测试登录'''
    def setUp(self):
        print("----------------------------------------------------------")
    def test_api_vpn_login1(self):
        '''测试登录，正确的账号，正确的密码'''
        username='adm'
        password='adm'
        result=api_vpn_login().testapi_vpn_login(username,password)
        self.assertEqual(result['msg'],'0',"登录失败")
    def test_api_vpn_login2(self):
        '''测试登录，正确的账号，错误的密码'''
        username='adm'
        password='am'
        result=api_vpn_login().testapi_vpn_login(username,password)
        self.assertEqual(result['msg'],"用户不存在或口令错误，请正确输入并重")
    def test_api_vpn_login3(self):
        '''测试登录，用户名密码为空'''
        # try:
        username=""
        password=""
        result=api_vpn_login().testapi_vpn_login(username,password)
        self.assertEqual(result['msg'],'用户不存在或口令错误，请正确输入并重试')
    def test_api_vpn_login4(self):
        '''登录测试，正确的用户名，密码为空'''
        # try:
        username="adm"
        password=""
        result=api_vpn_login().testapi_vpn_login(username,password)
        self.assertEqual(result['msg'],'用户不存在或口令错误，请正确输入并重试')
            #用户不存在或口令错误，请正确输入并重试',"登录失败
    def test_api_vpn_login5(self):
        '''登录测试，正确的账号，密码为数字、字母、字符、特殊字符、空格'''
        username="adm"
        password="123abc@#!$ :''''$"
        result=api_vpn_login().testapi_vpn_login(username,password)
        self.assertEqual(result['msg'],'用户不存在或口令错误，请正确输入并重试')   
    def tearDown(self):
        print ("----------------------------------------------------------")
if __name__=="__main__":
    unittest.main()


