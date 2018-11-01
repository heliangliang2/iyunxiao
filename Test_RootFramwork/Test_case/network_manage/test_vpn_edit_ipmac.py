#coding:utf-8
import unittest,time
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from function.test_vpn_farmwork_function import *
class edit_ipmac2(unittest.TestCase):
    '''ipMAC-修改MAC'''
    def setUp(self):
        pass
    def test_del_ipmac(self):
        '''正确的配置'''
        edit_ipmac="61:45:CB:61:49:17"
        edit_ipmask(edit_ipmac)
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()