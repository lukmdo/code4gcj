import unittest
from b import get_angle

DELTA = 10**-6


class TestFoo(unittest.TestCase):
    def test_case1(self):
        self.assertAlmostEqual(get_angle(98, 980), 45.0000000, delta=DELTA)

    def test_case2(self):
        self.assertAlmostEqual(get_angle(98, 490), 15.0000000, delta=DELTA)

    def test_case3(self):
        self.assertAlmostEqual(get_angle(299, 1234), 3.8870928, delta=DELTA)


if __name__ == '__main__':
    unittest.main()
