import unittest
from Ascalar import get_min_scalar_product

class TestFoo(unittest.TestCase):
    def test_case1(self):
        min_scalar_product = get_min_scalar_product((1, 3, -5), (-2, 4, 1))
        self.assertEqual(min_scalar_product, -25)

    def test_case2(self):
        min_scalar_product = get_min_scalar_product(
            (1, 2, 3, 4, 5), (1, 0, 1, 0, 1))
        self.assertEqual(min_scalar_product, 6)

if __name__ == '__main__':
    unittest.main()
