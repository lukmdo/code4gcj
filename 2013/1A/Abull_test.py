import unittest
from Abull import get_num_circles


class TestFoo(unittest.TestCase):
    def test_case1(self):
        num_circles = get_num_circles(1, 9)
        self.assertEqual(num_circles, 1)

    def test_case2(self):
        num_circles = get_num_circles(1, 10)
        self.assertEqual(num_circles, 2)

    def test_case3(self):
        num_circles = get_num_circles(3, 40)
        self.assertEqual(num_circles, 3)

    def test_case4(self):
        num_circles = get_num_circles(1, 1000000000000000000)
        self.assertEqual(num_circles, 707106780)

    def test_case5(self):
        num_circles = get_num_circles(10000000000000000, 1000000000000000000)
        self.assertEqual(num_circles, 49)


if __name__ == '__main__':
    unittest.main()
