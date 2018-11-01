#conding:utf-8
import unittest
import requests
from bs4 import BeautifulSoup
from test_login_function import api_vpn_login_session_cookies,add_default_route
class api_add_default_route(unittest.TestCase):
	'''添加静态路由'''
	def setup(self):
		print("添加静态路由")
	def test_api_add_default_route(self):
		'''正确的dest/mast/nexthop/metric'''
		api_vpn_login_session_cookies().login_session_cookies()
		dest="3.3.3.9"
		mast="255.255.255.255"
		nextthop="3.3.3.6"
		metric="25"
		result=add_default_route().add_route(dest,mast,nextthop,metric)
		result1=BeautifulSoup(result,"html.parser")
		self.assertEqual(result1.rows.msg.string,'0')
	def tearDown(self):
		pass
if __name__ == '__main__':
	unittest.main()