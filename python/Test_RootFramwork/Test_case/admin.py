from selenium import webdriver

#登录
def login():
    user_username=driver.find_element_by_xpath("//input[@id='user']")
    user_username.clear
    user_username.send_keys("username")
    user_password=driver.find_element_by_xpath("//input[@id='pwd']")
    user_password.clear
    user_password.send_keys("password")
    time.sleep(3)
    user_login=driver.find_element_by_xpath("//img[@src='image/login_btn.png']")
    user_login.click
    print("登录完成")
def logout():
    driver.quit()
    print("退出完成")

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://172.18.8.124:8888")
login()#调用退出模块

