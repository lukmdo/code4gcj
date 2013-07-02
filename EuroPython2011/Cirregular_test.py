import unittest
from Cirregular import is_valid_spell


class TestFoo(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(is_valid_spell('abracadabra'), True)

    def test_case2(self):
        self.assertEqual(is_valid_spell('kajabbamajabbajab'), True)

    def test_case3(self):
        self.assertEqual(is_valid_spell('frufrumfuffle'), False)

    def test_case4(self):
        self.assertEqual(is_valid_spell('schprexityschprex'), False)


if __name__ == '__main__':
    unittest.main()
