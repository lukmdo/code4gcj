#!/usr/bin/python3
"""
python Abull.py < IN-FILE.in > OUT-FILE.out
python -u Abull.py < IN-FILE.in | tee OUT-FILE.out
"""


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
