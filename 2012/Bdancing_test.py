import unittest
from Bdancing import dancer_selector


class TestFoo(unittest.TestCase):
    def test_from_description(self):
        29, 20, 8, 18, 18, 21
        n_googlers, n_surprising, min_score,  *totals = \
            map(int, '6 2 8 29 20 8 18 18 21'.split())
        solved = dancer_selector(n_googlers, n_surprising, min_score, totals)
        self.assertEqual(solved, 3)

    def test_case1(self):
        n_googlers, n_surprising, min_score,  *totals = \
            map(int, '3 1 5 15 13 11'.split())
        solved = dancer_selector(n_googlers, n_surprising, min_score, totals)
        self.assertEqual(solved, 3)

    def test_case2(self):
        n_googlers, n_surprising, min_score,  *totals = \
            map(int, '3 0 8 23 22 21'.split())
        solved = dancer_selector(n_googlers, n_surprising, min_score, totals)
        self.assertEqual(solved, 2)

    def test_case3(self):
        n_googlers, n_surprising, min_score,  *totals = \
            map(int, '2 1 1 8 0'.split())
        solved = dancer_selector(n_googlers, n_surprising, min_score, totals)
        self.assertEqual(solved, 1)

    def test_case4(self):
        n_googlers, n_surprising, min_score,  *totals = \
            map(int, '6 2 8 29 20 8 18 18 21'.split())
        solved = dancer_selector(n_googlers, n_surprising, min_score, totals)
        self.assertEqual(solved, 3)

    def test_corner_cases(self):
        # obvious unreachable high limit
        n_googlers, n_surprising, min_score,  *totals = \
            map(int, '2 10 100 2 13'.split())
        solved = dancer_selector(n_googlers, n_surprising, min_score, totals)
        self.assertEqual(solved, 0)

        # all scores 0 and 0 as limit
        n_googlers, n_surprising, min_score,  *totals = \
            map(int, '2 0 0 0 0'.split())
        solved = dancer_selector(n_googlers, n_surprising, min_score, totals)
        self.assertEqual(solved, 2)

        # 0 googlers
        n_googlers, n_surprising, min_score,  *totals = \
            map(int, '0 2 1 0'.split())
        solved = dancer_selector(n_googlers, n_surprising, min_score, totals)
        self.assertEqual(solved, 0)


if __name__ == '__main__':
    unittest.main()
