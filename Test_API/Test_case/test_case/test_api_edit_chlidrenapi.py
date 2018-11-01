#coding:utf-8
import requests
import unittest
from bs4 import BeautifulSoup
from test_login_function import getallsubbyname,edit_chlidrenapi
from test_login_function import api_vpn_login_session_cookies
class api_edit_children(unittest.TestCase):
	'''修改子接口配置'''
	def setup(self):
		print("开始修改子接口配置")
	def test_api_edit_childrenapi(self):
		'''正确的IP、MASK'''
		api_vpn_login_session_cookies().login_session_cookies()
		result1=getallsubbyname().getallsub()#获取子接口列表
		result2=BeautifulSoup(result1,"html.parser")#界面HTML解析
		aa=result2.rows.row.contents
		edit_list=[]
		for i in aa:
			if i !='\n' and i.string !='启用':
				edit_list.append(i)
		print(edit_list[1].string)
		a1=edit_list[1].string
		a2=edit_list[2].string
		result3=edit_chlidrenapi().edit_chlidrenapi(a1,a2)
		result4=BeautifulSoup(result3,"html.parser")
		a3=result4.rows.msg.string
		self.assertEqual(a3,'0')
	def test_api_edit_childrenapi2(self):
		'''正确的IP、错误的MASk'''
		api_vpn_login_session_cookies().login_session_cookies()
		a4="1.1.1.4"
		a5="255.555.555.0"
		result5=edit_chlidrenapi().edit_chlidrenapi(a4,a5)
		result6=BeautifulSoup(result5,"html.parser")
		a6=result6.rows.msg.string
		self.assertNotEqual(a6,'0')
	def tearDown(self):
		print ("修改子接口配置结束")
if __name__ == '__main__':
	unittest.main()