#coding:utf-8
import unittest
import requests
from bs4 import BeautifulSoup
from  test_login_function import api_vpn_login,api_add_cookies,api_add_chlidrenApi
class chlidrenapi(unittest.TestCase):
    def setUp(self):
        print ("开始添加子接口")
    def test_add_chlidrenapi(self):
        '''正确的配置子接口'''
        username='adm'
        password='adm'
        result=api_vpn_login().testapi_vpn_login(username,password)
        data_session=result['session_id']
        api_add_cookies().api_add_cookies(data_session)
        chliren_ip="1.1.1.3"
        chlidren_mask="255.0.0.0"
        result2=api_add_chlidrenApi().add_chlidren_api(chliren_ip,chlidren_mask)
        print (result2)
        result3=BeautifulSoup(result2,"html.parser")
        chlidrenapi_string=result3.rows.msg.string
        self.assertEqual(chlidrenapi_string,'0')
    def tearDown(self):
        print ("添加子接口结束")
if  __name__=="__main__":
    unittest.main()
