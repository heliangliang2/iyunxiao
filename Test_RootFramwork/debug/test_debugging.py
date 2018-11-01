# #coding:utf-8
# import unittest,time
# from selenium import webdriver
# username="adm"
# password="adm"
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://172.18.21.156:8888")
# driver.find_element_by_id("user").send_keys(username)
# driver.find_element_by_id("pwd").send_keys(password)
# driver.find_element_by_xpath("//img[@src='image/login_btn.png']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='tree2']/li[5]/div/div[1]").click()#点击路由设置
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='tree2']/li[5]/ul/li[1]/div/span").click()#点击策略路由
# driver.switch_to_frame(driver.find_element_by_xpath("//*[@src='page/netManage/netRouter/netStaticRouter.html']"))#框架切换
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='add']").click()#点击添加策略路由
# driver.find_element_by_xpath("/html/body/div[6]/div[3]/button[2]").click()#确认弹出框
# driver.find_element_by_xpath("//*[@id='ip1']").send_keys(add_ip1)#源子网
# driver.find_element_by_xpath("//*[@id='ip2']").clear()
# driver.find_element_by_xpath("//*[@id='ip2']").send_keys(add_ipmask)#源mask
# driver.find_element_by_xpath("//*[@id='ip3']").send_keys(add_dstgw)#目的子网
# driver.find_element_by_xpath("//*[@id='ip4']").send_keys(add_dstmask)#目的mask
# driver.find_element_by_xpath("//*[@id='ip5']").send_keys(add_gw)#目的网关
# driver.find_element_by_xpath("/html/body/div[6]/div[3]/button[2]").click()#提交
