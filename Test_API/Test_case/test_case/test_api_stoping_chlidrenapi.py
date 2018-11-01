import unittest
import requests
from bs4 import BeautifulSoup
from test_login_function import api_vpn_login_session_cookies,stop_childrenapi,getallsubbyname
class api_stoping_childrenapi(unittest.TestCase):
	'''停止子接口'''
	def setup(self):
		print("停止子接口")
	def test_api_stoping_childrenapi(self):
		'''停止子接口'''
		api_vpn_login_session_cookies().login_session_cookies()	#用户登录session关联
		result=getallsubbyname().getallsub()#获取子接口列表
		result1=BeautifulSoup(result,"html.parser")
		aa=(result1.row.attrs['id'])#获取子接口ID
		a1=stop_childrenapi().stop_chilrenapi(aa)#停止eth2.2的地址
		result2=BeautifulSoup(a1,'html.parser')
		a2=result2.rows.msg.string
		self.assertEqual(a2,'0')
	def tearDown(self):
		pass
if __name__ == '__main__':
	unittest.main()

