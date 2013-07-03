import unittest
from c import is_split_possible


class TestFoo(unittest.TestCase):
    def test_case1(self):
        pairs = [('Dead_Bowie', 'Fake_Thomas_Jefferson')]
        self.assertEqual(is_split_possible(pairs), True)

    def test_case2(self):
        pairs = [
            ('Dead_Bowie', 'Fake_Thomas_Jefferson'),
            ('Fake_Thomas_Jefferson', 'Fury_Leika'),
            ('Fury_Leika', 'Dead_Bowie')]
        self.assertEqual(is_split_possible(pairs), False)


if __name__ == '__main__':
    unittest.main()
