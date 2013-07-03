#!/usr/bin/python3
"""
python b.py < IN-FILE.in > OUT-FILE.out
python -u b.py < IN-FILE.in | tee OUT-FILE.out
"""
import math


def get_angle(v, d):
    """
    :param v: velocity int
    :param d: distance int
    :return: angle float
    """
    return 90 * math.asin(d * 98 / (10 * v**2 )) / math.pi


def solve(num_cases):
    for i in range(1, num_cases + 1):
        v_str, d_str = input().split(' ')
        solved = get_angle(int(v_str), int(d_str))
        print('Case #{num}: {solved}'.format(num=i, solved=solved))


if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
