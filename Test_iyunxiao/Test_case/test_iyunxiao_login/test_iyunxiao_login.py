import unittest
import sys,time
from selenium import webdriver
sys.path.append("C:\\Users\\Administrator\\Desktop\\iyunxiao\\iyunxiao\\Test_iyunxiao\\Test_case")
from function.function import hfs_login
class test_hfs_center_login(unittest.TestCase):
    '''测试账号登录'''
    def setUp(self):
        print("------开始执行账号登录测试------")
    def test_hfs_login(self):
        username="heliangliang"
        password="123456"
        hfs_login(username,password)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()