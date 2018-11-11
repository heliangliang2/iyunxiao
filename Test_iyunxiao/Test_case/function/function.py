import unittest
from selenium import webdriver
import sys,time
sys.path.append("C:\\Users\\Administrator\\Desktop\\iyunxiao\\iyunxiao\\Test_iyunxiao\\Test_case")
url="http://testhfs-oms.yunxiao.com/user/login"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)
from log.hfs_log import loger2
test_hfs_log=loger2()
def hfs_login(username,password):
    '''用户登录'''
    driver.find_element_by_xpath("//*[@id='app']/div/div/section/ul/li[1]/input").click()
    driver.find_element_by_xpath("//*[@id='app']/div/div/section/ul/li[1]/input").send_keys(username)
    test_hfs_log.info("输入正确的账号")
    driver.find_element_by_xpath("//*[@id='app']/div/div/section/ul/li[2]/input").click()
    driver.find_element_by_xpath("//*[@id='app']/div/div/section/ul/li[2]/input").send_keys(password)
    test_hfs_log.info("输入正确的密码")
    driver.find_element_by_xpath("//*[@id='app']/div/div/section/ul/li[3]/button").click()
    test_hfs_log.info("开始登录")
