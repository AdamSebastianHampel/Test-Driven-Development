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

    def test6(self):
        input = '123456789GRP'
        self.assertFalse(check_pwd(input))

    def test7(self):
        input = '1234567891ad'
        self.assertFalse(check_pwd(input))

    def test8(self):
        input = '1234567891dfad'
        self.assertFalse(check_pwd(input))

    def test9(self):
        input = 'abcdefgHIJK'
        self.assertFalse(check_pwd(input))

    def test10(self):
        input = 'abcdefBBBBB'
        self.assertFalse(check_pwd(input))

    def test11(self):
        input = "abcdef123BB"
        self.assertFalse(check_pwd(input))

    def test12(self):
        input = "abcdTRI98"
        self.assertFalse(check_pwd(input))

if __name__ == '__main__':
    unittest.main()
    