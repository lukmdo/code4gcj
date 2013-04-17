import unittest
from Dtreasure import get_open_combination


class TestFoo(unittest.TestCase):
    def test_case1(self):
        open_combination = get_open_combination(
            (1,), [(1, 1,), (2, 1, 1, 3), (3, 2,), (4, 3, 2)])
        self.assertEqual(open_combination, (2, 1, 4, 3))

    def test_case2(self):
        open_combination = get_open_combination(
            (1, 1, 1), [(1, 1,), (2, 1,), (3, 1,)])
        self.assertEqual(open_combination, (1, 2, 3))

    def test_case3(self):
        open_combination = get_open_combination(
            (2,), [(1, 1, 1, 1)])
        self.assertEqual(open_combination, None)


if __name__ == '__main__':
    unittest.main()
