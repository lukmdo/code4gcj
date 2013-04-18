import unittest
from Blawnmower import is_doable


class TestFoo(unittest.TestCase):
    def test_case1(self):
        data = (
            (2, 1, 2),
            (1, 1, 1),
            (2, 1, 2))
        status = is_doable(data)
        self.assertEqual(status, True)

    def test_case2(self):
        data = (
            (2, 2, 2, 2, 2),
            (2, 1, 1, 1, 2),
            (2, 1, 2, 1, 2),
            (2, 1, 1, 1, 2),
            (2, 2, 2, 2, 2))
        status = is_doable(data)
        self.assertEqual(status, False)

    def test_case3(self):
        data = ((1, 2, 1),)
        status = is_doable(data)
        self.assertEqual(status, True)


if __name__ == '__main__':
    unittest.main()
