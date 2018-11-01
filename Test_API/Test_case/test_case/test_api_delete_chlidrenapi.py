#coding:utf-8
import requests 
import unittest
import re
from bs4 import BeautifulSoup
from test_login_function import  api_vpn_login,api_add_cookies,delete_chlidrenapi,getallsubbyname
class childrenapi(unittest.TestCase):
    def setup(self):
        print ("开始删除子接口")
    def test_delete_childrenapi(self):
        '''删除单个子接口'''
        username='adm'
        password='adm'
        result=api_vpn_login().testapi_vpn_login(username,password)
        #用户名密码登录
        data_session=result['session_id']
        api_add_cookies().api_add_cookies(data_session)
        #关联sessionID
        #子接口界面刷新
        result2=getallsubbyname().getallsub()
        #删除子接口
        data2=BeautifulSoup(result2,"html.parser")
        number=0
        data1=[]#将row列表添加到序列
        aa=[]#row string添加到列表
        a1=[]#修改子接口格式byte eth.x 到序列
        aa_children='.'
        for i in data2.rows.contents:
            data1.append(i)
            if number==0:
                pass
            else:
                aa.append(data1[number].cell.string)
            number=number+1
            for i1 in aa:#修改字节流的格式
                a1_eth=i1.split(':')[0]
                a1_eth2=i1.split(':')[1]
                a1_eth3=a1_eth+aa_children+a1_eth2
                a1.append(a1_eth3)
            print('添加a1%s'%a1)
        if aa !=[]:
            eth=a1[0]
            r1=delete_chlidrenapi().vpn_delete_chlidrenapi(eth)
            print (r1)
        else:
            print ("子接口为空")
    def tearDown(self):
        print("删除子接口结束")
if __name__=="__main__":
    unittest.main()
