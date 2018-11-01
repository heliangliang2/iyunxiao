# #coding:utf-8
# import unittest
# #导入测试文件
# import HTMLTestRunner
# import sys
# sys.path.append("D:/test1/Test_API/Test_case/test_case")#将model目录添加到系统环境变量path下
# import test_api_vpn_login
# testunit=unittest.TestSuite()
# #将测试用例加入到测试容器套件中
# testunit.addTest(unittest.makeSuite(test_api_vpn_login.api_vpn))
# #定义报告存放路径，支持相对路径
# filename='D:/test1/Test_API/Test_report/result.html'
# fp=open(filename,'wb')
# runner=HTMLTestRunner.HTMLTestRunner(
#     stream=fp,
#     title=u'接口测试报告',
#     description=u'用例执行情况'
# )
# #执行测试用例
# runner.run(testunit)
# fp.close()

