from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

#登录测试
driver=webdriver.Chrome()
driver.get("https://172.18.8.124:8888/")
print("开始进入主界面")
#IE浏览器元素
# driver.find_element_by_id("continueToSite").click()
# driver.find_element_by_id("overridelink").click()
# print ("点击成功")
driver.switch_to_default_content()
print ("开始输入账号")
ele_user=driver.find_element_by_xpath("//input[@name='textfield']")
ele_user.clear()
ele_user.send_keys("adm")
print ("开始输入密码")
ele_pwd=driver.find_element_by_xpath("//input[@id='pwd']")
size=driver.find_element_by_xpath("//input[@id='pwd']").size
result=driver.find_element_by_xpath("//input[@id='pwd']").is_displayed()
print(result)
ele_pwd.clear()
ele_pwd.send_keys("adm")
ele_sub=driver.find_element_by_xpath("//img[@src='image/login_btn.png']")
text=driver.find_element_by_xpath("//img[@src='image/login_btn.png']").text
print (text)
attribute=driver.find_element_by_xpath("//img[@src='image/login_btn.png']").get_attribute('type')
print(attribute)
ele_sub.click()
sleep(3)
print ("账号密码登录成功")
print ("请开始你的表演")

#设置浏览器大小
# print("设置浏览器宽480，高800显示")
# driver.set_window_size(480,800)
# sleep(3)

#控制浏览器后退前进
# driver.back()
# print("控制浏览器回退")
# sleep(3)
# driver.forward()
# print ("控制浏览器前进")

#模拟浏览器刷新
# driver.refresh()
# print ("刷新浏览器")
# sleep(3)
# driver.quit()



#网络接口

print ("开始设置网络接口")
bro=driver.find_elements_by_class_name("l-body")
result2=driver.find_element_by_class_name("l-body").is_displayed()
print(result2)
bro[1].click()
sleep(3)
print ("点击接口")
#设置接口eth1
# driver.switch_to_frame("0")
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'page/netManage/netInterface.html')]"))
print ("框架切换点击成功")
eth1=driver.find_element_by_id("eth1")
eth1_dis=driver.find_element_by_id("eth1").is_displayed()
print (eth1_dis)
ActionChains(driver).double_click(eth1).perform()
eth1_api1=driver.find_element_by_xpath("//a[@href='#subInterface']")
eth1_api1.click()
print ("点击子接口")
print ("开始添加子接口,4.4.4.4.,255.255.255.0")
eth1_api2=driver.find_element_by_xpath("//input[@id='subAdd']")
eth1_api2.click()
eth1_ip4=driver.find_element_by_xpath("//input[@id='ip4']")
eth1_ip4.clear()
eth1_ip4.send_keys("4.4.4.4")
eth1_ip5=driver.find_element_by_xpath("//input[@id='ip5']")
eth1_ip5.clear()
eth1_ip5.send_keys("255.255.255.0")
sleep(3)
eth1_sub=driver.find_elements_by_xpath("//button[@class='ui-state-default.ui-corner-all']")
# eth1_sub_type=driver.find_elements_by_xpath("//button[@class='ui-state-default.ui-corner-all']").size
# print (eth1_sub_type)
eth1_sub[1].click()
print ("eth1接口添加成功")

#设置接口eth2
#设置接口eth3
# driver.quit()
