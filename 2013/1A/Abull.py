#!/usr/bin/python3
"""
python Abull.py < IN-FILE.in > OUT-FILE.out
python -u Abull.py < IN-FILE.in | tee OUT-FILE.out
"""
import math


def bisect_le(yfunc, y, r):
    """from https://gist.github.com/lukmdo/5855284"""
    lo, hi = 0, len(r)
    if callable(y):
        yfunc2 = y
    else:
        yfunc2 = lambda x, y=y: y

    found = None

    while lo < hi:
        mid = (lo + hi) // 2

        if yfunc(r[mid]) <= yfunc2(r[mid]):
            found = mid
            lo = mid + 1
        else:
            hi = mid

    return found


def get_num_circles(first_r, paint):
    paint_per_n = lambda n, r=first_r: 2*(n)**2 + 2*r*n - n
    return bisect_le(paint_per_n, paint, range(paint))


def solve(num_cases):
    for i in range(1, num_cases+1):
        case = input().split(' ')
        first_r, paint = int(case[0]), int(case[1])
        solved = get_num_circles(first_r, paint)
        print('Case #{num}: {solved}'.format(num=i, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
