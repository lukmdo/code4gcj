import unittest
from Benergy import get_max_gain


class TestFoo(unittest.TestCase):
    def test_case1(self):
        max_gain = get_max_gain(5, 2, (2, 1))
        self.assertEqual(max_gain, 12)

    def test_case2(self):
        max_gain = get_max_gain(5, 2, (1, 2))
        self.assertEqual(max_gain, 12)

    def test_case3(self):
        max_gain = get_max_gain(3, 3, (4, 1, 3, 5))
        self.assertEqual(max_gain, 39)


if __name__ == '__main__':
    unittest.main()
