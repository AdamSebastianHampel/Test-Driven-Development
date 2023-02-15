import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
  
    def test1(self):
        input = ''
        self.assertFalse(check_pwd(input))
    
    def test2(self):
        input = '1234567'
        self.assertFalse(check_pwd(input))

    def test3(self):
        input = '123456789012345678901'
        self.assertFalse(check_pwd(input))
    
    def test4(self):
        input = '1234567890123456789012'
        self.assertFalse(check_pwd(input))
    
    def test5(self):
        input = '123456789'
        self.assertFalse(check_pwd(input))
    

if __name__ == '__main__':
    unittest.main()