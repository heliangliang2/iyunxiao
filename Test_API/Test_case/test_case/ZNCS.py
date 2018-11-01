import unittest
from HTMLTestRunner import HTMLTestRunner
from time import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://erp.jchl.com")
        self.driver.implicitly_wait(2)
#登录
    def test_something(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/span/span/input').send_keys("15018493771")
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[3]/div/div/span/span/input').send_keys("chowmin3410")
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[4]/div/div/span/button').click()
        sleep(1)
#新增凭证
        Button = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/button')
        ActionChains(self.driver).move_to_element(Button).perform()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/button').click()
#输入摘要
        a = self.driver.find_element_by_xpath('//*[@id="app-proof-of-charge"]/div[4]/div/div/div/div[1]/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div/div/ul/li/div/input')
        ActionChains(self.driver).move_to_element(a).send_keys('提现').perform()
        sleep(1)
#切换输入框
        self.driver.find_element_by_xpath('//*[@id="app-proof-of-charge"]/div[4]/div/div/div/div[1]/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div/div/ul/li/div/input').send_keys(Keys.TAB)
        sleep(1)
#输入会计科目
        self.driver.find_element_by_xpath('//*[@id="app-proof-of-charge"]/div[4]/div/div/div/div[1]/div[3]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/input').send_keys('1001 库存现金')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app-proof-of-charge"]/div[4]/div/div/div/div[1]/div[3]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/input').send_keys(Keys.ENTER)


#输入借方金额
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector('html body div#app div.edfx-app-root div.edfx-app-portal div.mk-layout.edfx-app-portal-content div.mk-layout div.mk-layout.edfx-app-portal-content-main div#app-proof-of-charge.mk-layout.app-proof-of-charge div.gridDiv div.mk-datagrid.mk-datagrid-editable.app-proof-of-charge-form-details.mk-addDel.mk-upDown div div.fixedDataTableLayout_main.public_fixedDataTable_main div.fixedDataTableLayout_rowsContainer div div.fixedDataTableRowLayout_rowWrapper div.fixedDataTableRowLayout_main.public_fixedDataTableRow_main.public_fixedDataTableRow_even.public_fixedDataTable_bodyRow div.fixedDataTableRowLayout_body div.fixedDataTableCellGroupLayout_cellGroupWrapper div.fixedDataTableCellGroupLayout_cellGroup div.fixedDataTableCellLayout_main.public_fixedDataTableCell_main input#mk-input-number.ant-input.mk-input-number.app-proof-of-charge-cell.editable-cell').send_keys('1000')
        sleep(1)
        self.driver.find_element_by_css_selector('html body div#app div.edfx-app-root div.edfx-app-portal div.mk-layout.edfx-app-portal-content div.mk-layout div.mk-layout.edfx-app-portal-content-main div#app-proof-of-charge.mk-layout.app-proof-of-charge div.gridDiv div.mk-datagrid.mk-datagrid-editable.app-proof-of-charge-form-details.mk-addDel.mk-upDown div div.fixedDataTableLayout_main.public_fixedDataTable_main div.fixedDataTableLayout_rowsContainer div div.fixedDataTableRowLayout_rowWrapper div.fixedDataTableRowLayout_main.public_fixedDataTableRow_main.public_fixedDataTableRow_even.public_fixedDataTable_bodyRow div.fixedDataTableRowLayout_body div.fixedDataTableCellGroupLayout_cellGroupWrapper div.fixedDataTableCellGroupLayout_cellGroup div.fixedDataTableCellLayout_main.public_fixedDataTableCell_main input#mk-input-number.ant-input.mk-input-number.app-proof-of-charge-cell.editable-cell').send_keys(Keys.ENTER)
        sleep(1)
        self.driver.find_element_by_css_selector('html body div#app div.edfx-app-root div.edfx-app-portal div.mk-layout.edfx-app-portal-content div.mk-layout div.mk-layout.edfx-app-portal-content-main div#app-proof-of-charge.mk-layout.app-proof-of-charge div.gridDiv div.mk-datagrid.mk-datagrid-editable.app-proof-of-charge-form-details.mk-addDel.mk-upDown div div.fixedDataTableLayout_main.public_fixedDataTable_main div.fixedDataTableLayout_rowsContainer div div.fixedDataTableRowLayout_rowWrapper div.fixedDataTableRowLayout_main.public_fixedDataTableRow_main.public_fixedDataTableRow_even.public_fixedDataTable_bodyRow div.fixedDataTableRowLayout_body div.fixedDataTableCellGroupLayout_cellGroupWrapper div.fixedDataTableCellGroupLayout_cellGroup div.fixedDataTableCellLayout_main.public_fixedDataTableCell_main input#mk-input-number.ant-input.mk-input-number.app-proof-of-charge-cell.editable-cell').send_keys(Keys.TAB)
        sleep(1)
#输入贷方金额
        self.driver.find_element_by_xpath('//*[@id="app-proof-of-charge"]/div[4]/div/div/div/div[1]/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div/div/ul/li/div/input').send_keys(Keys.TAB)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app-proof-of-charge"]/div[4]/div/div/div/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/input').send_keys('1001')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app-proof-of-charge"]/div[4]/div/div/div/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/input').send_keys(Keys.ENTER)
        self.driver.find_element_by_css_selector('html body div#app div.edfx-app-root div.edfx-app-portal div.mk-layout.edfx-app-portal-content div.mk-layout div.mk-layout.edfx-app-portal-content-main div#app-proof-of-charge.mk-layout.app-proof-of-charge div.gridDiv div.mk-datagrid.mk-datagrid-editable.app-proof-of-charge-form-details.mk-addDel.mk-upDown div div.fixedDataTableLayout_main.public_fixedDataTable_main div.fixedDataTableLayout_rowsContainer div div.fixedDataTableRowLayout_rowWrapper div.fixedDataTableRowLayout_main.public_fixedDataTableRow_main.public_fixedDataTableRow_highlighted.public_fixedDataTableRow_odd.public_fixedDataTable_bodyRow div.fixedDataTableRowLayout_body div.fixedDataTableCellGroupLayout_cellGroupWrapper div.fixedDataTableCellGroupLayout_cellGroup div.fixedDataTableCellLayout_main.public_fixedDataTableCell_main input#mk-input-number.ant-input.mk-input-number.app-proof-of-charge-cell.editable-cell').send_keys(Keys.TAB)
        self.driver.find_element_by_xpath('//*[@id="mk-input-number"]').send_keys(Keys.ENTER)
        sleep(1)
#点击保存按钮
        self.driver.find_element_by_xpath('//*[@id="app-proof-of-charge"]/div[5]/div[2]/button[2]').click()
    def tearDown(self):
        self.driver.quit()



if __name__=='__main__':
    #定义一个单元测试容器
    testunit = unittest.TestSuite()
    #将测试用例加入测试容器中
    testunit.addTest(MyTestCase("test_something"))
    #定义报告存放路径
    HTML_File = "D:/test1/Test_API/Test_report/result.html"
    # 定义测试报告
    with open(HTML_File,'wb') as fp:
        runner = HTMLTestRunner(stream = fp,title='智能财税_新增凭证测试报告',description='用例执行情况')
    #运行测试用例
        runner.run(testunit)
        # unittest.main()
        fp.close()

