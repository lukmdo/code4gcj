import unittest
from a import get_cost


class TestFoo(unittest.TestCase):
    def test_case1(self):
        cost = get_cost(['Oksana Baiul', 'Michelle Kwan'])
        self.assertEqual(cost, 1)

    def test_case2(self):
        cost = get_cost([
            'Elvis Stojko', 'Evgeni Plushenko', 'Kristi Yamaguchi'])
        self.assertEqual(cost, 0)

    def test_case3(self):
        cost = get_cost(['1', '3', '4', '2'])
        self.assertEqual(cost, 1)



if __name__ == '__main__':
    unittest.main()
