import unittest
from Dtwibet import get_num_whispers_a_day


class TestFoo(unittest.TestCase):
    def test_case1(self):
        num_whispers_a_day = get_num_whispers_a_day([2, 3, 1])
        self.assertEqual(num_whispers_a_day, [3, 3, 3])

    def test_case2(self):
        num_whispers_a_day = get_num_whispers_a_day([2, 3, 2, 1])
        self.assertEqual(num_whispers_a_day, [2, 4, 4, 1])


if __name__ == '__main__':
    unittest.main()
