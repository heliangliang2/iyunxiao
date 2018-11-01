# #!/usr/bin/python
# #coding:utf-8
# from selenium import webdriver
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import UnexpectedAlertPresentException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as  EC 
# import unittest,time

# class test_to_parameterize(unittest.TestCase):
#     '''参数化登录vpn测试'''
#     def setUp(self):
#         self.driver=webdriver.Chrome()
#         self.driver.maximize_window()
#         print ("开始测试")
#     def test_parameterize(self):
#         try:
#             user_file=open("user_info.txt",encoding="gbk")
#             lines=user_file.readlines()
#             user_file.close()
#             stroage={}
#             for line in lines:
#                 username=line.split(',')[0]
#                 password=line.split(',')[1]
#                 stroage[username]=password
#             print("打印字典内容如下%s"%stroage)
#             for username_members in stroage.keys():
#                 driver=self.driver
#                 driver.get("https://172.18.8.124:8888")
#                 print("开始打印字典 %s" % stroage)
#                 user_name=driver.find_element_by_id("user")
#                 user_pwd=driver.find_element_by_id("pwd")
#                 user_login=driver.find_element_by_xpath("//img[@src='image/login_btn.png']")
#                 user_name.clear()
#                 user_name.send_keys(username_members)
#                 user_pwd.clear()
#                 user_pwd.send_keys(stroage[username_members])
#                 user_login.click()
#                 # driver.implicitly_wait(10)
#                 tex=driver.switch_to_alert().text
#                 print(tex)
#                 self.assertIsNone(tex,"用户不存在或口令错误，请正确输入并重试")
#                 driver.switch_to_alert().dismiss()
#         except NoAlertPresentException as e:
#             # pass
#             print(e)
#             return False
#         # except UnexpectedAlertPresentException as f:
#         #     print(f)
#         #     return False
#         finally:
#             print("登录参数化测试")
#     def tearDown(self):
#         self.driver.quit()
# if __name__=="__main__":
#     unittest.main()