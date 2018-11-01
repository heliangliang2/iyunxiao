# from calculator2 import Count
# import unittest
# class TestAdd(unittest.TestCase):
#     def setUp(self):
#         print("test add start")

#     def test_add(self):
#         j=Count(2,3)
#         self.assertEqual(j.add(),5)
#     def test_add2(self):
#         j=Count(41,76)
#         self.assertEqual(j.add(),117)
#     def tearDown(self):
#         print ("test add end")
# class TestSub(unittest.TestCase):
#     def setUp(self):
#         print ("test sub start")
#     def test_sub(self):
#         j=Count(2,3)
#         self.assertEqual(j.sub(),-1)
#     def test_sub2(self):

#         j=Count(71,46)
#         self.assertEqual(j.sub(),25)
#     def tearDown(self):
#         print ("test sub end")
# if __name__=='__main__':
#     #构造测试集
#     suite=unittest.TestSuite()
#     suite.addTest(TestAdd("test_add"))
#     suite.addTest(TestAdd("test_add2"))
#     suite.addTest(TestSub("test_sub"))
#     suite.addTest(TestSub("test_sub2"))
#     #运行测试用例
#     runner=unittest.TextTestRunner()
#     runner.run(suite)