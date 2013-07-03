#!/usr/bin/python3
"""
python c.py < IN-FILE.in > OUT-FILE.out
python -u c.py < IN-FILE.in | tee OUT-FILE.out
"""
from collections import defaultdict
from itertools import combinations


def is_split_possible(pairs):
    pairs_map = defaultdict(set)
    for k, v in pairs:
        pairs_map[k].add(v)
        pairs_map[v].add(k)

    for k, l in pairs_map.items():
        if len(l) == 1:
            continue
        for j, k in combinations(l, 2):
            if k in pairs_map and j in pairs_map[k]:
                return False

    return True


def solve(num_cases):
    for i in range(1, num_cases + 1):
        num_pairs = int(input())
        pairs = [input().split(' ') for i in range(num_pairs)]
        solved = 'Yes' if is_split_possible(pairs) else 'No'
        print('Case #{num}: {solved}'.format(num=i, solved=solved))


if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
