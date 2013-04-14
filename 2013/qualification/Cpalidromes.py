#!/usr/bin/python3
"""
python Cpalidromes.py < IN-FILE.in > OUT-FILE.out
python -u Cpalidromes.py < IN-FILE.in | tee OUT-FILE.out
"""
from math import sqrt, ceil


def _get_fair_and_square(begin, end):
    for num in range(ceil(sqrt(begin)), ceil(sqrt(end))+1):
        str_num = str(num)
        if str_num.endswith('0'):
            continue
        if str_num == str_num[::-1]:
            root_num = num ** 2
            str_root_num = str(root_num)
            # no need to check endswith('0')
            if str_root_num == str_root_num[::-1]:
                yield root_num


cache = []  # more read optimized bTree?

# prepopulate with fair-and-square < 1000
cache = list(_get_fair_and_square(1, 1000))
cache_begin, cache_end = 1, 1000


def get_fair_and_square_count(begin, end):
    global cache_end
    if begin > cache_end or end > cache_end:
        next_cached_end = max(end, cache_end*1000)
        for num in _get_fair_and_square(cache_end+1, next_cached_end):
            cache.append(num)
        cache_end = next_cached_end
    t = 0
    for n in cache:
        if n < begin:
            continue
        if n > end:
            break
        t += 1
    return t


def solve(num_cases):
    for i in range(1, num_cases+1):
        case = input().split(' ')
        range_begin, range_end = int(case[0]), int(case[1])
        solved = get_fair_and_square_count(range_begin, range_end)
        print('Case #{num}: {solved}'.format(num=i, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
