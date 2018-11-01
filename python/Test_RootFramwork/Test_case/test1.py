import unittest
class Test(unittest.TestCase):
    def setUp(self):
        number=input("Eneter a number")
        self.number=int(mumber)
    
    def test_case(self):
        self.assertEqual(self.number,10,msg="your input is not 1o")
    
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()