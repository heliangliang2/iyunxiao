from selenium import webdriver
import unittest
import time
from  HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    '''百度搜索测试'''
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url="http://www.baidu.com"
    def test_baidu_search(self):
        '''搜索关键字 HTMLTestRunner'''
        driver=self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys('unittest')
        driver.find_element_by_id("su").click()
        time.sleep(2)
        # title=driver.title
        # self.assertEqual(title,"unittest_百度搜索")
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()
    # testunit=unittest.TestSuite()
    # testunit.addTest(Baidu("test_baidu_search"))
    # #按照一定格式获取当前时间
    # now=time.strftime("%Y-%m-%d %H-%M-%S")
    # #定义报告存放路径
    # filename='D:\\python自动化脚本\\test_project\\report\\'+now+' result.html'
    # fp=open(filename,'wb')
    # #定义测试报告
    # runner = HTMLTestRunner(stream=fp , 
    #                 title = '百度搜索测试报告' , description = ' 用例执行情况：')
    # runner.run(testunit)#运行测试用例
    # fp.close()
    #代码分析：首先将htmltestrunner模块用import导入进来 2.通过open方法以二进制写模式代开当前目录下的result。html 
    #如果没有则自动创建该文件，最后通过HTMLTestRunner的run（）方法来运行测试套件中所组装的测试用例。最后通过close关闭测试报告文件

