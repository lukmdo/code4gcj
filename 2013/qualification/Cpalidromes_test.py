import unittest
from Cpalidromes import get_fair_and_square_count


class TestFoo(unittest.TestCase):
    def test_case1(self):
        fair_and_square_count = get_fair_and_square_count(1, 4)
        self.assertEqual(fair_and_square_count, 2)

    def test_case2(self):
        fair_and_square_count = get_fair_and_square_count(10, 120)
        self.assertEqual(fair_and_square_count, 0)

    def test_case3(self):
        fair_and_square_count = get_fair_and_square_count(100, 1000)
        self.assertEqual(fair_and_square_count, 2)


if __name__ == '__main__':
    unittest.main()
