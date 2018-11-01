#!/usr/bin/python
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest,time,os,sys


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.accept_alert=True
    def test_API(self):
        try:
            driver=self.driver
            driver.get("https://172.18.8.124:8888")
            driver.find_element_by_id("user").send_keys("adm")
            driver.find_element_by_id("pwd").send_keys("adm")
            driver.find_element_by_xpath("//img[@src='image/login_btn.png']").click()
            time.sleep(3)
            print("登录成功")
            webui_api=driver.find_elements_by_class_name("l-body")
            webui_api[1].click()
            print ("接口点击成功")
            print("开始设置接口")
            time.sleep(3)
            driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'page/netManage/netInterface.html')]"))
            print ("框架切换成功")
            eth1=driver.find_element_by_id("eth1")
            eth1_dis=driver.find_element_by_id("eth1").is_displayed()
            print (eth1_dis)
            ActionChains(driver).double_click(eth1).perform()
            driver.find_element_by_id("info_type_select").click()
            time.sleep(3)
            driver.find_element_by_xpath("//option[@value='1']").click()
            print ("开始配置接口地址和掩码")
            driver.find_element_by_id("ip1").send_keys("2.2.2.2.")
            driver.find_element_by_id("ip2").send_keys("255.255.255.0")
            time.sleep(5)
            # js='document.querySelectorAll("div")[5].style.display="block";'
            # driver.execute_script(js)
            # driver.find_element_by_xpath("//button[@class='ui-state-default ui-corner-all']").click()
            button=driver.find_element_by_xpath("//button[@class='ui-state-default.ui-corner-all']")
            driver.execute_script('$(arguments[1]).fadeOut()',button)
            button.click()
           
            # eth1_api1=driver.find_element_by_xpath("//a[@href='#subInterface']")
            # eth1_api1.click()
            # print(len(webui_api))
            # driver.switch_to_alert().accept()
            # print ("处理弹出框")
        except NoSuchElementException as e:
            print (e)
        finally:
            self.vpn_screen()
            # print (e)
            # f=open('C:\\Users\\Administrator\\Desktop\\test\\python\\test_project\\log\\error.txt','rb')
            # f.write("e")
            # f.close()
            # def vpn_error_log(self):
            #     '''log日志'''
            #     f=open('error.txt','a')
    def vpn_screen(self):
        #截图配置'''
        time2=time.strftime("%Y-%m-%d %H_%M_%S")
        self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\Desktop\\test\\python\\test_project\\annex\\"+time2+'ERROR.png')
    def is_element_present(self,how,what):
        #判断元素是否存在
        try:
            self.driver.find_element(by=how,value=what)
        except NoSuchElementException as e:
            return False
            print (e)
        except:
            vpn_screen()
        # return True
    def is_alert(self):
        #判断是否有弹出框
        try:
            self.driver.swicth_to_alert()
        except NoAlertPresentException as f:
            return False
            print (f)
        return True
    def close_alert(self):
        #关闭弹出框并打印出弹出框信息
        try:
            alert=self.driver.swicth_to_alert()
            alert_text=alert.text 
            if  self.accept_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            accept_alert=True
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()
    


