#coding:utf-8
import unittest
from selenium import webdriver
import sys
# sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
# sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case\\log1")
from log1.logger import log
from function.test_vpn_farmwork_function import *
# log=log()
log_scenes=log()
class test_scenes(unittest.TestCase):
    def setUp(self):
        pass
    def test_add_scenes(self):
        #用户登录
        log_scenes.info("---测试用例开始---")
        log_scenes.info("---用户登录测试---")
        username="adm"
        password="adm"
        user_login(username,password)
        #添加子接口
        log_scenes.info("---开始添加子接口---")
        add_ipv4="1.1.1.36"
        add_mask="255.255.255.0"
        add_api(add_ipv4,add_mask)
        # 添加静态路由
        log_scenes.info("---开始添加静态路由---")
        add_ip="1.1.1.56"
        add_gw="1.1.1.1"
        add_metric="23"
        add_static_route(add_ip,add_gw,add_metric)
        #添加策略路由
        log_scenes.info("---开始添加策略路由---")
        add_ip1="1.1.1.6"
        add_ipmask="255.255.255.255"
        add_dstgw="1.1.1.8"        
        add_dstmask="255.255.255.255"
        add_gw="1.1.1.9"
        add_policy_route(add_ip1,add_ipmask,add_dstgw,add_dstmask,add_gw)
        #添加RIp路由
        log_scenes.info("---开始添加RIP路由---")
        add_rip_route()
        #添加ospf路由
        log_scenes.info("---开始添加OSPF路由---")
        add_route_ip="0.0.0.0"
        add_network="192.168.1.26"
        add_network_mask="24"
        add_ospf_route(add_route_ip,add_network,add_network_mask)
        #ipmac绑定
        log_scenes.info("---IPmac绑定---")
        add_mac_ip="1.1.1.13"
        add_mac="60:45:CB:61:49:17"
        netmanager_add_ipmask(add_mac_ip,add_mac)
        #修改ipmac
        log_scenes.info("---修改IPMAC---")
        edit_mac="60:45:CB:61:49:18"
        edit_ipmask(edit_mac)
        #导出文件
        log_scenes.info("---开始导出文件---")
        import_out_file()
        #扫描接口
        log_scenes.info("---开始扫描接口---")
        ipmac_scanning()
        #dns设置
        log_scenes.info("---配置DNS服务器---")
        dns1="202.103.24.68"
        dns2="114.114.114.114"
        dns3="1.1.156"
        vpn_add_dns_agent(dns1,dns2,dns3)
        #DNS代理策略
        log_scenes.info("---设置DNS代理策略---")
        vpn_add_dns_setting()
        #查询服务器
        log_scenes.info("---设置查询服务器---")
        dns_ip="1.1.1.56"
        vpn_dns_inquire(dns_ip)
        #编辑服务器
        log_scenes.info("---开始编辑服务器---")
        dns_ip_inquire="1.1.1.45"
        edit_dns_inquire(dns_ip_inquire)
        #删除dns服务器
        log_scenes.info("---删除DNS服务器---")
        del_dns_agent_ip()
        #dns黑名单
        log_scenes.info("---添加DNS黑名单---")
        domain_name="1.1.1.1"
        vpn_add_dns_backlist(domain_name)
        #删除黑名单
        log_scenes.info("---删除黑名单---")
        del_dns_backlist()
        #添加白名单
        log_scenes.info("---开始添加白名单---")
        whitelist_ip="1.1.1.14"
        whitelist_domain="hll.com"
        add_dns_whitelist(whitelist_ip,whitelist_domain)
        #修改白名单
        # log_scenes.info("---修改白名单---")
        # edit_whitelist_ip="1.1.1.15"
        # edit_whitelist_domain="hlll.com"
        # edit_dns_whitelist(edit_whitelist_ip,edit_whitelist_domain)
        #删除白名单
        log_scenes.info("---删除白名单---")
        del_dns_whitelist()
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()


