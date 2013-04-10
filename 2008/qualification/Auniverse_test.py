import unittest
from Auniverse import get_min_switch_count


class TestFoo(unittest.TestCase):
    def test_case1(self):
        min_switch_count = get_min_switch_count(
            ('Yeehaw', 'NSM', 'Dont Ask', 'B9', 'Googol'),
            ('Yeehaw', 'Yeehaw', 'Googol', 'B9', 'Googol', 'NSM', 'B9', 'NSM',
             'Dont Ask', 'Googol')
        )
        self.assertEqual(min_switch_count, 1)

    def test_case2(self):
        min_switch_count = get_min_switch_count(
            ('Yeehaw', 'NSM', 'Dont Ask', 'B9', 'Googol'),
            ('Googol', 'Dont Ask', 'NSM', 'NSM', 'Yeehaw', 'Yeehaw', 'Googol')
        )
        self.assertEqual(min_switch_count, 0)


if __name__ == '__main__':
    unittest.main()
