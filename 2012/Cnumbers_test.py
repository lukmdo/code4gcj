import unittest
from Cnumbers import get_recycled_num_count



class TestFoo(unittest.TestCase):
    def test_case1(self):
        recycled_count = get_recycled_num_count(1, 9)
        self.assertEqual(recycled_count, 0)

    def test_case2(self):
        recycled_count = get_recycled_num_count(10, 40)
        self.assertEqual(recycled_count, 3)

    def test_case3(self):
        recycled_count = get_recycled_num_count(100, 500)
        self.assertEqual(recycled_count, 156)

    def test_case4(self):
        recycled_count = get_recycled_num_count(1111, 2222)
        self.assertEqual(recycled_count, 287)


if __name__ == '__main__':
    unittest.main()
