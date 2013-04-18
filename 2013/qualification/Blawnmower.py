#!/usr/bin/python3
"""
python Blawnmower.py < IN-FILE.in > OUT-FILE.out
python -u Blawnmower.py < IN-FILE.in | tee OUT-FILE.out
"""
from collections import defaultdict


def is_doable(data):
    w, h = len(data[0]), len(data)
    if w == 1 or h == 1:
        return True

    ltp = defaultdict(set)  # Lever To Points
    for y in range(h):
        for x in range(w):
            ltp[data[y][x]].add((y, x))

    none_is_higher = lambda pts, l: all(data[p[0]][p[1]] <= l for p in pts)

    for l in sorted(ltp):
        l_points = set(ltp[l])
        while l_points:
            point = l_points.pop()
            horizontal_points = [(point[0], x) for x in range(w)]
            if none_is_higher(horizontal_points, l):
                l_points -= set(horizontal_points)
            else:
                vertical_points = [(y, point[1]) for y in range(h)]
                if none_is_higher(vertical_points, l):
                    l_points -= set(vertical_points)
                else:
                    return False

    return True


def solve(num_cases):
    for i in range(1, num_cases+1):
        case = input().split()
        num_rows, num_cols = int(case[0]), int(case[1])
        data = []
        for row_num in range(num_rows):
            row = [int(level) for level in input().split()]
            data.append(row)
        solved = 'YES' if is_doable(data) else 'NO'
        print('Case #{num}: {solved}'.format(num=i, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
