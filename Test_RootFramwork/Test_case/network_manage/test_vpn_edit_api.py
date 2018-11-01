import unittest 
from selenium import webdriver
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class edit_api_farmwork(unittest.TestCase):
    '''编辑子接口'''
    def setUp(self):
        pass
    def test_vpn_edit_api(self):
        '''正确的IP和mask'''
        add_ipv4="1.1.1.1"
        add_mask="255.0.0.0"
        add_api(add_ipv4,add_mask)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()
