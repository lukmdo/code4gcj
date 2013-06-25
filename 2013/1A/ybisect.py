"""Bisect based formula testing.

Implements bisect_lt, bisect_le, bisect_ge, bisect_gt from scratch using `yfun`
# http://code.google.com/codejam/contest/2418487/dashboard
>>> r, t = 10**16, 10**18
>>> yfun = lambda x: (2*(10**16) + (2*x) -1) * x
Given bisect_le(yfun, y, range(N))
>>> bisect_le(yfun, t, range(t))
49

Nice, but what if you want use dynamic yfun2 insted of static y:
>>> import math
>>> yfun1 = lambda x: 10 ** ((x-20)/10)
>>> yfun2 = lambda x: x * math.log(x)
>>> yfun  = lambda x: yfun1(x) - yfun2(x)
>>>> bisect_le(yfun, 0, range(10**3))
41

Alternative
-----------
Add a lazy `yfun` function based range data-structure
>>> yr = yrange([start], stop, [step], y=yfun)
>>> yr[x] == fun(x)
then pure bisect would be back in use:
>>> from bisect import bisect
>>> bisect(yr, t)
49

Note:
- (Range class)[https://github.com/psycopg/psycopg2/blob/master/lib/_range.py]
would have to (re)implement __getitem__(self, i): return self.yfun(i)
- py < py3 :
    >>> range(10**18)
    Python(31171,0x7fff70784180) malloc: *** mmap(size=8000000000000000000)
        failed (error code=12)
    *** error: can't allocate region
    *** set a breakpoint in malloc_error_break to debug
    ---------------------------------------------------------------------------
    MemoryError
"""


def bisect_ge(func, y, r):
    """
    Return first index from range `r` which:
    yfunc(r[i]) >= y || None

    :param yfunc: probed function as one arg callable
    :param y: value
    :param r: range with non-descending values
    :return: found value or None
    """
    lo, hi = 0, len(r)
    found = None

    while lo < hi:
        mid = (lo + hi) // 2
        if func(r[mid]) >= y:
            found = True
            hi = mid
        else:
            lo = mid + 1

    return found and lo


def bisect_gt(yfunc, y, r):
    """
    Return first index from range `r` which:
    yfunc(r[i]) > y || None

    :param yfunc: probed function as one arg callable
    :param y: value
    :param r: range with non-descending values
    :return: found value or None
    """
    lo, hi = 0, len(r)
    found = None

    while lo < hi:
        mid = (lo + hi) // 2
        if yfunc(r[mid]) > y:
            found = True
            hi = mid
        else:
            lo = mid + 1

    return found and lo


def bisect_lt(yfunc, y, r):
    """
    Return last index from range `r` which:
    yfunc(r[i]) < y || None

    :param yfunc: probed function as one arg callable
    :param y: value
    :param r: range with non-descending values
    :return: found value or None
    """
    lo, hi = 0, len(r)
    found = None

    while lo < hi:
        mid = (lo + hi) // 2
        if yfunc(r[mid]) < y:
            found = mid
            lo = mid + 1
        else:
            hi = mid

    return found


def bisect_le(yfunc, y, r):
    """
    Return last index from range `r` which:
    yfunc(r[i]) <= y || None

    :param yfunc: probed function as one arg callable
    :param y: value
    :param r: range with non-descending values
    :return: found value or None
    """
    lo, hi = 0, len(r)
    found = None

    while lo < hi:
        mid = (lo + hi) // 2

        if yfunc(r[mid]) <= y:
            found = mid
            lo = mid + 1
        else:
            hi = mid

    return found


# ======================== TESTs ===========================
import unittest


class TestBisectGreater(unittest.TestCase):

    def test_returns_none_when_all_predicate_fail(self):
        stop = 5
        seq = range(stop + 1)
        expr_func = lambda x: x
        self.assertEqual(bisect_gt(expr_func, stop, seq), None)
        self.assertEqual(bisect_gt(expr_func, stop + 1, seq), None)

    def test_returns_first_passing(self):
        seq = [2, 3, 3, 3, 5]
        expr_func = lambda x: x

        self.assertEqual(bisect_gt(expr_func, 1, seq), 0)
        self.assertEqual(bisect_gt(expr_func, 2, seq), 1)
        self.assertEqual(bisect_gt(expr_func, 3, seq), 4)
        self.assertEqual(bisect_gt(expr_func, 4, seq), 4)


class TestBisectGreaterEqual(unittest.TestCase):

    def test_returns_none_when_all_predicate_fail(self):
        stop = 5
        seq = range(stop + 1)
        expr_func = lambda x: x
        self.assertEqual(bisect_ge(expr_func, stop + 1, seq), None)

    def test_returns_first_passing(self):
        seq = [2, 3, 3, 3, 5]
        expr_func = lambda x: x

        self.assertEqual(bisect_ge(expr_func, 1, seq), 0)
        self.assertEqual(bisect_ge(expr_func, 2, seq), 0)
        self.assertEqual(bisect_ge(expr_func, 3, seq), 1)
        self.assertEqual(bisect_ge(expr_func, 4, seq), 4)
        self.assertEqual(bisect_ge(expr_func, 5, seq), 4)


class TestBisectLess(unittest.TestCase):

    def test_returns_none_when_all_predicate_fail(self):
        start, stop = 2, 5
        seq = range(start, stop + 1)
        expr_func = lambda x: x

        self.assertEqual(bisect_lt(expr_func, start, seq), None)
        self.assertEqual(bisect_lt(expr_func, start - 1, seq), None)

    def test_returns_first_passing(self):
        seq = [2, 3, 3, 3, 5]
        expr_func = lambda x: x

        self.assertEqual(bisect_lt(expr_func, 3, seq), 0)
        self.assertEqual(bisect_lt(expr_func, 4, seq), 3)
        self.assertEqual(bisect_lt(expr_func, 5, seq), 3)
        self.assertEqual(bisect_lt(expr_func, 6, seq), 4)


class TestBisectLessEqual(unittest.TestCase):

    def test_returns_none_when_all_predicate_fail(self):
        start, stop = 2, 5
        seq = range(start, stop + 1)
        expr_func = lambda x: x

        self.assertEqual(bisect_le(expr_func, start - 1, seq), None)

    def test_returns_first_passing(self):
        seq = [2, 3, 3, 3, 5]
        expr_func = lambda x: x

        self.assertEqual(bisect_le(expr_func, 2, seq), 0)
        self.assertEqual(bisect_le(expr_func, 3, seq), 3)
        self.assertEqual(bisect_le(expr_func, 4, seq), 3)
        self.assertEqual(bisect_le(expr_func, 5, seq), 4)
        self.assertEqual(bisect_le(expr_func, 6, seq), 4)


if __name__ == '__main__':
    unittest.main()
