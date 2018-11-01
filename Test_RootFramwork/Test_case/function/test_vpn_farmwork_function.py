import unittest
from selenium import webdriver
import time,sys
from selenium.webdriver.support import expected_conditions as EC
# sys.path.append("C:\\Users\\john\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
sys.path.append("C:\\Users\\Administrator\\Desktop\\test2018\\Test_RootFramwork\\Test_case")
from log1.logger import log
log_function=log()
# url="https://192.168.1.123:8888"
url="https://172.18.21.156:8888"
# driver=webdriver.chrome()
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)
def user_quit():
    '''退出'''
    print("---程序开始退出")
    driver.quit()
def alert_accept():
    result2=EC.alert_is_present()(driver)
    if result2:
        aa=result2.text
        print(aa)
        result2.accept()
        return (aa)
    else:
        print ("on alert open")
def user_login(username,password):
    '''登录'''
    log_function.info("---用户开始登录---")
    driver.find_element_by_id("user").send_keys(username)
    log_function.info("---输入用户名---")
    driver.find_element_by_id("pwd").send_keys(password)
    log_function.info("---输入密码---")
    driver.find_element_by_xpath("//img[@src='image/login_btn.png']").click()
    log_function.info("---点击登录---")
    time.sleep(3)
    result=EC.alert_is_present()(driver)
    if result:
        bb=result.text
        print (bb)
        result.accept()
        return (bb)
    else:
        try:
            aa=driver.find_element_by_xpath("//img[@src='image/index_logo.jpg']").is_displayed()
            if aa==True:
                # print("---登录成功")
                log_function.info("---登录成功---")
            else:
                # print("---登录失败")
                log_function.info("---登录失败---")
            return(aa)
        except Exception as e:
            print(e)
    # print("---用户登录结束")
    log_function.info("---登录结束---")
def add_api(add_ipv4,add_mask):
    '''添加子接口'''
    driver.find_element_by_xpath("//*[@id='tree2']/li[2]/div/span").click()
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netInterface.html']"))
    #page/netManage/netInterface.html
    aa=driver.find_element_by_xpath("//*[@id='eth1']/td[1]")
    from selenium.webdriver import ActionChains
    actions_chains=ActionChains(driver)
    actions_chains.double_click(aa).perform()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='tabs']/ul/li[3]/a").click()
    driver.find_element_by_xpath("//*[@id='subAdd']").click()
    driver.find_element_by_xpath("//*[@id='ip4']").clear()
    driver.find_element_by_xpath("//*[@id='ip4']").send_keys(add_ipv4)
    driver.find_element_by_xpath("//*[@id='ip5']").clear()
    driver.find_element_by_xpath("//*[@id='ip5']").send_keys(add_mask)
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/button[2]").click()
    result3=EC.alert_is_present()(driver)
    if result3:
        print("alert is open")
        alert_aa=result3.text
        print(alert_aa)
        return (alert_aa)
    else:
        print("add_api no alert open")
        if driver.find_element_by_xpath("//*[@id='warning']"):
            print("进入相同配置函数")
            waring_text=driver.find_element_by_xpath("//*[@id='warning']").text#获取弹框出错的信息
            print(waring_text)#相同接口配置出错
            driver.find_element_by_xpath("/html/body/div[9]/div[1]/a/span").click()#关闭相同接口配置出错弹框
            driver.find_element_by_xpath("/html/body/div[7]/div[1]/a/span").click()#关闭弹框
            print("IP地址也被分配")
        else:
            print("没有弹出框出错的信息")
        print ("---接口添加成功")
    driver.switch_to_default_content()#切换到主框架
    print("---子接口添加成功")
def add_static_route(add_ip,add_gw,add_metric):
    '''添加静态路由'''
    # print("---开始添加静态路由")
    driver.find_element_by_xpath("//*[@id='tree2']/li[5]/div/div[1]").click()#点击路由设置
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='tree2']/li[5]/ul/li[2]/div/span").click()#点击静态路由
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netRouter/netStaticRouter.html']"))#框架切换
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='add']").click()#点击添加
    driver.find_element_by_xpath("/html/body/div[6]/div[3]/button[2]").click()#点击确认
    driver.find_element_by_xpath("//*[@id='ip6']").send_keys(add_ip)
    driver.find_element_by_xpath("//*[@id='ip7']").click()
    driver.find_element_by_xpath("//*[@id='ip8']").send_keys(add_gw)
    driver.find_element_by_xpath("//*[@id='metric']").send_keys(add_metric)
    driver.find_element_by_xpath("/html/body/div[6]/div[3]/button[2]").click()
    time.sleep(2)
    if driver.find_element_by_xpath("/html/body/div[7]/div[3]/button"):
        # print("关闭路由配置界面")
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/button").click()#点击确定
        #/html/body/div[7]/div[3]/button
        driver.find_element_by_xpath("/html/body/div[5]/div[1]/a/span").click()#关闭路由配置界面
        # print("---相同的路由已经被添加")
    else:
        pass
    driver.switch_to_default_content()#切换到主框架
    # print("---静态路由添加成功")
def add_policy_route(add_ip1,add_ipmask,add_dstgw,add_dstmask,add_gw):
    '''添加策略路由'''
    # print("---开始添加策略路由")
    str1=driver.find_element_by_xpath("//*[@id='tree2']/li[5]/div/div[1]")
    str2=str1.get_attribute("class")
    print(str2)
    if str2=="l-box l-expandable-close":
        driver.find_element_by_xpath("//*[@id='tree2']/li[5]/div/div[1]").click()#点击路由设置
        # time.sleep(2)
        driver.find_element_by_xpath("//*[@id='tree2']/li[5]/ul/li[1]/div/span").click()#点击策略路由
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netRouter/netPolicyRouter.html']"))#框架切换
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='add']").click()#点击添加策略路由
        driver.find_element_by_xpath("/html/body/div[6]/div[3]/button[2]").click()#确认弹出框
        driver.find_element_by_xpath("//*[@id='ip1']").send_keys(add_ip1)#源子网
        driver.find_element_by_xpath("//*[@id='ip2']").clear()
        driver.find_element_by_xpath("//*[@id='ip2']").send_keys(add_ipmask)#源mask
        driver.find_element_by_xpath("//*[@id='ip3']").send_keys(add_dstgw)#目的子网
        driver.find_element_by_xpath("//*[@id='ip4']").clear()
        driver.find_element_by_xpath("//*[@id='ip4']").send_keys(add_dstmask)#目的mask
        driver.find_element_by_xpath("//*[@id='ip5']").send_keys(add_gw)#目的网关
        driver.find_element_by_xpath("/html/body/div[6]/div[3]/button[2]").click()#提交
        time.sleep(2)
        if driver.find_element_by_xpath("/html/body/div[7]/div[3]/button"):
            #/html/body/div[7]/div[3]/button
            driver.find_element_by_xpath("/html/body/div[7]/div[3]/button").click()#点击确定
            driver.find_element_by_xpath("/html/body/div[5]/div[1]/a/span").click()#关闭策略路由弹出框
            # print("相同的策略路由已经被添加")
        else:
            pass
    else:
        driver.find_element_by_xpath("//*[@id='tree2']/li[5]/ul/li[1]/div/span").click()#点击策略路由
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netRouter/netPolicyRouter.html']"))#框架切换
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='add']").click()#点击添加策略路由
        driver.find_element_by_xpath("/html/body/div[6]/div[3]/button[2]").click()#确认弹出框
        driver.find_element_by_xpath("//*[@id='ip1']").send_keys(add_ip1)#源子网
        driver.find_element_by_xpath("//*[@id='ip2']").clear()
        driver.find_element_by_xpath("//*[@id='ip2']").send_keys(add_ipmask)#源mask
        driver.find_element_by_xpath("//*[@id='ip3']").send_keys(add_dstgw)#目的子网
        driver.find_element_by_xpath("//*[@id='ip4']").clear()
        driver.find_element_by_xpath("//*[@id='ip4']").send_keys(add_dstmask)#目的mask
        driver.find_element_by_xpath("//*[@id='ip5']").send_keys(add_gw)#目的网关
        driver.find_element_by_xpath("/html/body/div[6]/div[3]/button[2]").click()#提交
        time.sleep(2)
        if driver.find_element_by_xpath("/html/body/div[7]/div[3]/button"):
            driver.find_element_by_xpath("/html/body/div[7]/div[3]/button").click()#点击确定
            driver.find_element_by_xpath("/html/body/div[5]/div[1]/a/span").click()#关闭策略路由弹出框
            # print("相同的配置路由已经被添加")
        else:
            pass
    driver.switch_to_default_content()#切换到主框架
    # print("----策略路由添加成功") 
def add_rip_route():
    '''添加RIP路由'''
    # print("---开始添加RIP路由")
    rip_str1=driver.find_element_by_xpath("//*[@id='tree2']/li[5]/div/div[1]")
    rip_str2=rip_str1.get_attribute("class")
    if rip_str2=="l-box l-expandable-close":
        driver.find_element_by_xpath("//*[@id='tree2']/li[5]/div/div[1]").click()#点击路由设置
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='tree2']/li[5]/ul/li[3]/div/span").click()#点击rip路由
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netRouter/netRIPRouter.html']"))#框架切换
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='table1']/tbody/tr[1]/td[1]/fieldset/div/input[1]").click()#点击路由重分发，所有直连路由
        driver.find_element_by_xpath("//*[@id='interface']/input[1]").click()#点击eth0接口
        driver.find_element_by_xpath("//*[@id='eth0']").click()#接口配置，点击eth0
        #有滚动条，点击滚动条到提交
        js="var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='save1']").click()
    else:
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='tree2']/li[5]/ul/li[3]/div/span").click()#点击rip路由
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netRouter/netRIPRouter.html']"))#框架切换
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='table1']/tbody/tr[1]/td[1]/fieldset/div/input[1]").click()#点击路由重分发，所有直连路由
        driver.find_element_by_xpath("//*[@id='interface']/input[1]").click()#点击eth0接口
        driver.find_element_by_xpath("//*[@id='eth0']").click()#接口配置，点击eth0
        #有滚动条，点击滚动条到提交
        js="var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='save1']").click()
    driver.switch_to_default_content()#切换到主框架
    # print("---RIP路由添加成功")
def add_ospf_route(add_route_ip,add_network,add_network_mask):
    '''添加OSPF路由'''
    # print("---开始添加OSPF路由")
    ospf_str1=driver.find_element_by_xpath("//*[@id='tree2']/li[5]/div/div[1]")
    ospf_str2=ospf_str1.get_attribute("class")
    if ospf_str2=="l-box l-expandable-close":
        driver.find_element_by_xpath("//*[@id='tree2']/li[5]/div/div[1]").click()#点击路由设置
        # print("路由设置")
        driver.find_element_by_xpath("//*[@id='tree2']/li[5]/ul/li[4]/div/span").click()#点击ospf路由
        # print ("点击ospf路由")
        time.sleep(2)
        result1=EC.alert_is_present()(driver)
        if result1:
            result1.accept()
        else:
            print("no alert open")
            time.sleep(2)
            driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netRouter/netOSPFRouter.html']"))#框架切换
            driver.find_element_by_xpath("/html/body/div[5]/div[3]/button").click()
            driver.find_element_by_xpath("//*[@id='ip1']").send_keys(add_route_ip)#输入路由器IP号
            driver.find_element_by_xpath("//*[@id='ip2']").send_keys(add_network)#输入网络子网
            driver.find_element_by_xpath("//*[@id='mask']").send_keys(add_network_mask)#输入掩码
            driver.find_element_by_xpath("//*[@id='ip3']").send_keys("0.0.0.0")#输入网络所在区域
            js1="var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js1)#下拉框
            driver.find_element_by_xpath("//*[@id='add']").click()#点击添加
    else:
        driver.find_element_by_xpath("//*[@id='tree2']/li[5]/ul/li[4]/div/span").click()#点击ospf路由
        # print ("点击ospf路由")
        time.sleep(2)
        result1=EC.alert_is_present()(driver)
        if result1:
            result1.accept()
        else:
            print("no alert open")
            time.sleep(2)
            driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netRouter/netOSPFRouter.html']"))#框架切换
            driver.find_element_by_xpath("/html/body/div[5]/div[3]/button").click()
            driver.find_element_by_xpath("//*[@id='ip1']").send_keys(add_route_ip)#输入路由器IP号
            driver.find_element_by_xpath("//*[@id='ip2']").send_keys(add_network)#输入网络子网
            driver.find_element_by_xpath("//*[@id='mask']").send_keys(add_network_mask)#输入掩码
            driver.find_element_by_xpath("//*[@id='ip3']").send_keys("0.0.0.0")#输入网络所在区域
            js1="var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js1)#下拉框
            driver.find_element_by_xpath("//*[@id='add']").click()#点击添加
    driver.switch_to_default_content()#切换到主框架
    # print("---添加OSPF路由成功")
def netmanager_add_ipmask(add_mac_ip,add_mac):
    '''添加IPMac'''
    # print("---开始添加IPMAC")
    driver.find_element_by_xpath("//*[@id='tree2']/li[6]/div/span").click()#点击IPmask绑定
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netIPMac.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='add']").click()#点击添加ipmask
    driver.find_element_by_xpath("//*[@id='ip1']").send_keys(add_mac_ip)#输入IP地址
    driver.find_element_by_xpath("//*[@id='mac']").send_keys(add_mac)#输入mac
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/button[2]").click()#点击添加
    driver.switch_to_default_content()#切换到主框架
    # print("---添加IPMAC成功")
def del_ipmask():
    '''删除IPMAC'''
    # print("---开始删除IPMAC")
    driver.find_element_by_xpath("//*[@id='tree2']/li[6]/div/span").click()#点击IPmask绑定
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netIPMac.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='jqg_table_ip_mac_bind_1']").click()#选中mac列表
    driver.find_element_by_xpath("//*[@id='del']").click()#点击删除mac
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/button[2]").click()#确认删除
    driver.switch_to_default_content()#切换到主框架
    # print("---删除IPMAC成功")
def edit_ipmask(edit_mac):
    '''修改ipmac'''
    # print("---开始修改Ipmac")
    driver.find_element_by_xpath("//*[@id='tree2']/li[6]/div/span").click()#点击IPmask绑定
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netIPMac.html']"))#框架切换
    print ("22222")
    try:
        if driver.find_element_by_xpath("//*[@id='jqg_table_ip_mac_bind_1']"):
            print("1111")
            driver.find_element_by_xpath("//*[@id='jqg_table_ip_mac_bind_1']").click()#点击mac列表复选框
            #//*[@id="jqg_table_ip_mac_bind_1"]
            driver.find_element_by_xpath("//*[@id='modify']").click()#点击编辑
            driver.find_element_by_xpath("//*[@id='mac']").clear()
            driver.find_element_by_xpath("//*[@id='mac']").send_keys(edit_mac)#输入修改的值
            driver.find_element_by_xpath("/html/body/div[8]/div[3]/button[3]").click()#点击提交
            driver.switch_to_default_content()#切换到主框架    
        else:
            print("元素列表为空，无法编辑")
    except Exception as e:
        print (e)
    # print("---修改IPmac成功")
def import_out_file():
    '''导出文件'''
    # print("---开始导出文件")
    driver.find_element_by_xpath("//*[@id='tree2']/li[6]/div/span").click()#点击IPmask绑定
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netIPMac.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='out']").click()
    driver.switch_to_default_content()#切换到主框架
    # print("---导出文件成功")
def importing_files():
    '''导入文件'''
    driver.find_element_by_xpath("//*[@id='tree2']/li[6]/div/span").click()#点击IPmask绑定
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netIPMac.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='insert']").click()
    driver.switch_to_default_content()#切换到主框架
def ipmac_scanning():
    '''扫描接口'''
    # print("---开始扫描接口")
    driver.find_element_by_xpath("//*[@id='tree2']/li[6]/div/span").click()#点击IPmask绑定
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netIPMac.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='Scanning']").click()#点击扫描
    driver.find_element_by_xpath("//*[@id='select_1']").click()#选择扫描接口
    driver.find_element_by_xpath("//*[@id='select_1']/option[1]").click()#选择下拉列表eth0
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/button[2]").click()#确定提交
    time.sleep(5)
    #选择绑定项  
    aa=driver.find_elements_by_xpath("//*[@aria-describedby='table4_IP2']")#绑定项列表
    print(len(aa))
    if len(aa)>0:
        i=0
        while i < (len(aa)):
                aa[i].click()
                i=i+1
        driver.find_element_by_xpath("//*[@id='add_bind']").click()#点击绑定项
        
    else:
        print("绑定列表为空")
    driver.switch_to_default_content()#切换到主框架
    # print("--=绑定接口成功")
def vpn_add_dns_agent(dns1,dns2,dns3):
    '''DNS设置'''
    # print("---开始填写DNS")
    driver.find_element_by_xpath("//*[@id='tree2']/li[7]/div/span").click()
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netDnsSet.html']"))
    driver.find_element_by_xpath("//*[@id='ip1']").clear()
    driver.find_element_by_xpath("//*[@id='ip1']").send_keys(dns1)#首选dns服务器
    driver.find_element_by_xpath("//*[@id='ip2']").clear()
    driver.find_element_by_xpath("//*[@id='ip2']").send_keys(dns2)#备用dns服务器1
    driver.find_element_by_xpath("//*[@id='ip3']").clear()
    driver.find_element_by_xpath("//*[@id='ip3']").send_keys(dns3)#备用dns服务器2
    driver.find_element_by_xpath("//*[@id='save']").click()
    driver.switch_to_default_content()#切换到主框架
    # print("---填写DNS成功")
def vpn_add_dns_setting():
    '''DNS代理策略'''
    # print("---开始设置DNS代理策略")
    driver.find_element_by_xpath("//*[@id='tree2']/li[8]/div/span").click()#点击代理设置
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netInnerDnsService.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='text_check']").click()#明文通信开启代理
    driver.find_element_by_xpath("//*[@id='ipsec_check']").click()#ipsec开启代理
    driver.find_element_by_xpath("//*[@id='ssl_check']").click()#ssl开启代理
    driver.find_element_by_xpath("//*[@id='save']").click()#点击提交
    driver.switch_to_default_content()#切换到主框架
    # print("---设置DNS代理策略成功")
def vpn_dns_inquire(dns_ip):
    '''查询服务器'''
    # print("---开始设置查询服务器")
    driver.find_element_by_xpath("//*[@id='tree2']/li[8]/div/span").click()#点击代理设置
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netInnerDnsService.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='add']").click()#点击添加
    driver.find_element_by_xpath("//*[@id='ip1']").send_keys(dns_ip)#输入服务器地址
    driver.find_element_by_xpath("/html/body/div[9]/div[3]/button[2]").click()#点击提交
    driver.switch_to_default_content()#切换到主框架
    # print("---设置查询服务器成功")
def edit_dns_inquire(dns_ip_inquire):
    '''编辑服务器'''
    # print("---开始编辑服务器")
    driver.find_element_by_xpath("//*[@id='tree2']/li[8]/div/span").click()#点击代理设置
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netInnerDnsService.html']"))#框架切换
    if driver.find_element_by_xpath("//*[@id='server_1']/td[2]"):
        driver.find_element_by_xpath("//*[@id='server_1']/td[2]").click()#选择服务器列表
        driver.find_element_by_xpath("//*[@id='modify']").click()#点击编辑
        driver.find_element_by_xpath("//*[@id='ip1']").clear()#
        driver.find_element_by_xpath("//*[@id='ip1']").send_keys(dns_ip_inquire)#输入服务器地址
        driver.find_element_by_xpath("/html/body/div[9]/div[3]/button[3]").click() 
    else:
        print("没有服务器IP")
    driver.switch_to_default_content()#切换到主框架
    # print("--编辑服务器成功")
def del_dns_agent_ip():
    '''删除dns服务器'''
    # print("---删除dns服务器")
    driver.find_element_by_xpath("//*[@id='tree2']/li[8]/div/span").click()#点击代理设置
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netInnerDnsService.html']"))#框架切换    
    if driver.find_element_by_xpath("//*[@id='server_1']/td[2]"):
        driver.find_element_by_xpath("//*[@id='server_1']/td[2]").click()
        driver.find_element_by_xpath("//*[@id='del']").click()
    else:
        print ("没有服务器IP")
    driver.switch_to_default_content()#切换到主框架
    # print("---删除dns服务器成功")
def vpn_add_dns_backlist(domain_name):
    '''dns黑名单'''
    # print("---开始添加dns黑名单")
    driver.find_element_by_xpath("//*[@id='tree2']/li[8]/div/span").click()#点击代理设置
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netInnerDnsService.html']"))#框架切换  
    driver.find_element_by_xpath("//*[@id='add_2']").click()#点击添加黑名单
    driver.find_element_by_xpath("//*[@id='server_dns_name']").send_keys(domain_name)#添加域名后缀
    driver.find_element_by_xpath("/html/body/div[9]/div[3]/button[2]").click()
    driver.switch_to_default_content()#切换到主框架
    # print("---添加dns黑名单成功")
def del_dns_backlist():
    '''删除黑名单'''
    # print("---开始删除黑名单")
    driver.find_element_by_xpath("//*[@id='tree2']/li[8]/div/span").click()#点击代理设置
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netInnerDnsService.html']"))#框架切换
    if driver.find_element_by_xpath("//*[@id='blackList_1']/td[2]"):
        driver.find_element_by_xpath("//*[@id='blackList_1']/td[2]").click()#选中黑名单列表
        driver.find_element_by_xpath("//*[@id='del_2']").click()#点击删除
    else:
        print("dns黑名单为空")
    driver.switch_to_default_content()#切换到主框架
    # print("---删除黑名单成功")
def add_dns_whitelist(whitelist_ip,whitelist_domain):
    '''添加白名单'''
    # print("---开始添加白名单")
    driver.find_element_by_xpath("//*[@id='tree2']/li[8]/div/span").click()#点击代理设置
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netInnerDnsService.html']"))#框架切换
    #界面向下移动
    js2="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js2)
    driver.find_element_by_xpath("//*[@id='add_3']").click()#点击添加白名单
    log_function.info("---开始添加白名单---")
    driver.find_element_by_xpath("//*[@id='ip3']").send_keys(whitelist_ip)#输入主机地址
    log_function.info("---开始输入主机地址---")
    driver.find_element_by_xpath("//*[@id='server_dns_name_3']").send_keys(whitelist_domain)#输入主机yuming域名
    log_function.info("---输入主机域名---")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[9]/div[3]/button[2]").click()#点击提交
    log_function.info("---点击提交---")
    #/html/body/div[9]/div[3]/button[2]
    driver.switch_to_default_content()#切换到主框架
    # print("---添加白名单成功")
# def edit_dns_whitelist(edit_whitelist_ip,edit_whitelist_domain):
#     '''修改白名单'''
#     # print("---开始添加白名单")
#     driver.find_element_by_xpath("//*[@id='tree2']/li[8]/div/span").click()#点击代理设置
#     time.sleep(2)
#     driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netInnerDnsService.html']"))#框架切换
#     #界面向下移动
#     js3="var q=document.documentElement.scrollTop=10000"
#     driver.execute_script(js3)
#     if driver.find_element_by_xpath("//*[@id='whiteList_1']/td[2]"):
#         driver.find_element_by_xpath("//*[@id='whiteList_1']/td[2]").click()
#         driver.find_element_by_xpath("//*[@id='add_3']").click()
#         driver.find_element_by_xpath("//*[@id='ip3']").clear()
#         driver.find_element_by_xpath("//*[@id='ip3']").send_keys(edit_whitelist_ip)
#         driver.find_element_by_xpath("//*[@id='server_dns_name_3']").clear()
#         driver.find_element_by_xpath("//*[@id='server_dns_name_3']").send_keys(edit_whitelist_domain)
#         driver.find_element_by_xpath("/html/body/div[9]/div[3]/button[3]").click()
#     else:
#         print("白名单为空")
#     driver.switch_to_default_content()#切换到主框架
    # print("---添加白名单成功")
def del_dns_whitelist():
    '''删除白名单'''
    # print("---开始删除白名单")
    driver.find_element_by_xpath("//*[@id='tree2']/li[8]/div/span").click()#点击代理设置
    time.sleep(2)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netInnerDnsService.html']"))#框架切换
    #界面向下移动
    js4="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js4)
    if driver.find_element_by_xpath("//*[@id='whiteList_1']/td[2]"):
        driver.find_element_by_xpath("//*[@id='whiteList_1']/td[2]").click()
        driver.find_element_by_xpath("//*[@id='del_2']").click()
        driver.quit()
    else:
        print ("白名单为空")
    driver.switch_to_default_content()#切换到主框架
    # print("---删除白名单成功")
def add_ddns_setting():
    '''添加DDNS'''
    # print("---开始添加ddns")
    driver.find_element_by_xpath("//*[@id='tree2']/li[9]/div/span").click()#点击ddns设置
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netDDNS.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='checkbox_1']").click()#点击复选框
    driver.find_element_by_xpath("//*[@id='regist']").click()
    driver.switch_to_default_content()#切换到主框架
    # print("---添加ddns成功")
def add_ddns_services(ddns_domain,ddns_username,ddns_password):
    '''添加DDNS服务器'''
    # print("---开始添加DDNS服务器")
    driver.find_element_by_xpath("//*[@id='tree2']/li[9]/div/span").click()
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netDDNS.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='add']").click()#点击添加
    driver.find_element_by_xpath("//*[@id='text_1']").send_keys(ddns_domain)#输入域名服务器
    driver.find_element_by_xpath("//*[@id='text_2']").send_keys(ddns_username)#输入用户名
    driver.find_element_by_xpath("//*[@id='text_3']").send_keys(ddns_password)#输入密码
    driver.find_element_by_xpath("//*[@id='select_1']/option[1]").click()#选择接口
    driver.find_element_by_xpath("/html/body/div[6]/div[3]/button[2]").click()
    driver.switch_to_default_content()#切换到主框架
    # print("---添加DDNS服务器成功")
def del_ddns_services():
    '''删除ddns服务器'''
    # print("---开始删除ddns服务器")
    driver.find_element_by_xpath("//*[@id='tree2']/li[9]/div/span").click()#点击ddns设置
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netDDNS.html']"))#框架切换
    if driver.find_element_by_xpath("//*[@id='ddns_1']/td[2]"):
        driver.find_element_by_xpath("//*[@id='ddns_1']/td[2]").click()#选中服务器列表
        driver.find_element_by_xpath("//*[@id='del']").click()
    else:
        print ("ddns服务器列表为空")
    driver.switch_to_default_content()#切换到主框架
    # print("---删除ddns服务器成功")
def edit_ddns_services(add_domain,add_username,add_password):
    '''编辑ddns服务器'''
    # print("---开始编辑ddns服务器")
    driver.find_element_by_xpath("//*[@id='tree2']/li[9]/div/span").click()#点击ddns设置
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netDDNS.html']"))#框架切换
    if driver.find_element_by_xpath("//*[@id='ddns_1']/td[2]"):
        driver.find_element_by_xpath("//*[@id='ddns_1']/td[2]").click()#选中服务器列表
        driver.find_element_by_xpath("//*[@id='modify']").click()
        driver.find_element_by_xpath("//*[@id='text_1']").send_keys(add_domain)
        driver.find_element_by_xpath("//*[@id='text_2']").send_keys(add_username)
        driver.find_element_by_xpath("//*[@id='text_3']").send_keys(add_password)
        driver.find_element_by_xpath("//*[@id='select_1']/option[1]").click()
    else:
        print("---服务器列表为空")
    driver.switch_to_default_content()#切换到主框架
    # print("---编辑ddns服务器成功")
def clear_ddns_services():
    '''清空ddns服务器'''
    # print("---开始清空ddns服务器")
    driver.find_element_by_xpath("//*[@id='tree2']/li[9]/div/span").click()#点击ddns设置
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netDDNS.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='clear']").click()
    driver.switch_to_default_content()#切换到主框架
    # print("---清空ddns服务器成功")
def add_dhcp(add_start_address_pool,add_end_address_pool,add_dhcp_mask,add_dhcp_netmanage,add_dhcp_address):
    '''编辑dhcp服务器'''
    # print("---开始编辑dhcp服务器")
    driver.find_element_by_xpath("//*[@id='tree2']/li[10]/div/span").click()#点击dhcp服务器
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netDHCP.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='select2']/option[1]").click()#点击自动启用
    driver.find_element_by_xpath("//*[@id='select1']/option").click()#点击网络接口eth0
    driver.find_element_by_xpath("//*[@id='ip1']").send_keys(add_start_address_pool)#输入起始IP地址池
    driver.find_element_by_xpath("//*[@id='ip2']").send_keys(add_end_address_pool)#输入结束IP地址池
    driver.find_element_by_xpath("//*[@id='ip3']").send_keys(add_dhcp_mask)#输入子网掩码
    driver.find_element_by_xpath("//*[@id='ip4']").send_keys(add_dhcp_netmanage)#输入网关
    driver.find_element_by_xpath("//*[@id='ip5']").send_keys(add_dhcp_address)#输入dhcp服务器地址
    driver.find_element_by_xpath("//*[@id='button_1']").click()#点击启用
    driver.find_element_by_xpath("//*[@id='save']").click()#点击提交
    #进入分配列表
    driver.find_element_by_xpath("//*[@id='tabs']/ul/li[2]/a").click()
    driver.find_element_by_xpath("//*[@id='refresh']").click()
    driver.switch_to_default_content()#切换到主框架
    # print("---编辑dhcp服务器成功")
def clear_dhcp():  
    '''清空dhcp服务器'''
    # print("---开始清空dhcp服务器")
    driver.find_element_by_xpath("//*[@id='tree2']/li[10]/div/span").click()#点击dhcp服务器
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netDHCP.html']"))#框架切换
    driver.find_element_by_xpath("//*[@id='tabs']/ul/li[2]/a").click()#点击分配列表
    driver.find_element_by_xpath("//*[@id='clear']").click()#点击清空
    driver.switch_to_default_content()#切换到主框架
    # print("---清空dhcp服务器成功")
   



