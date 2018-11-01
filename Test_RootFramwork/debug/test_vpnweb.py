# from selenium import webdriver
# import unittest,time

# class test_vpnwebUI(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         self.base_url="https://192.168.1.123:8888"
#     def test_vpn(self):
#         driver=self.driver
#         driver.get(self.base_url+"/")
#         user_name=driver.find_element_by_id("user")
#         user_name.clear()
#         user_name.send_keys("adm")
#         user_passwd=driver.find_element_by_id("pwd")
#         user_passwd.clear()
#         user_passwd.send_keys("adm")
#         driver.find_element_by_xpath("//img[@src='image/login_btn.png']").click()
#         time.sleep(2)
#         title=driver.title
#         print(title)
#         self.assertEqual(title,"MPSec-VPN3030S-AC-172.18.8.124:8888")
#     def tearDown(self):
#         self.driver.quit()
#         print("user login in success")
# if __name__=="__main__":
#     unittest.main()