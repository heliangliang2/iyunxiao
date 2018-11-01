from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time,re

#引入unittest框架
class BaiduTest(unittest.TestCase):
    def setUp(self):
        #用户初始化工作，在执行每一个测试用例前先被执行，这里初始化工作定义了浏览器启动和基础URL地址
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://www.baidu.com/"
        self.verificationErrors=[]
        #脚本运行时的错误信息将被记录到这个数组中
        self.accept_next_alert=True
        #表示师傅继续接受下一个警告，初始状态为True
    def test_baidu(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
    def is_element_present(self,how,what):
        #用于查找页面元素是否存在，通过find_element来接收元素的定位方法how和定位值
        try:
            self.driver.find_element(by=how,value=what)
        except NoSuchElementException as e:
            return False
        return True
    def id_alert_present(self):
        #判断页面是否出现警告框，利用switch_to_alert,用于获取当前页面上警告框
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True
    def close_alert_and_get_its_text(self):
        #关闭警告并获得警告信息，
        try:
            alert=self.drivr.switch_to_alert()
            alert_text=alert.text 
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert=True
    def tearDown (self):
        #方法在每个测试方法执行后调用，定义了空数组，通过assertEqual()比较其是否为空，如果为空则说明用例执行的过程总没有
        #异常，否知抛出异常
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
if __name__=='__main__':
    unittest.main()
    #通过unittest.main()方法来运行当前文件中的测试方法，其默认匹配并运行以test开头的方法
