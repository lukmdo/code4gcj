#!/usr/bin/python3
"""
python Cnumbers.py < IN-FILE.in > OUT-FILE.out
python -u Cnumbers.py < IN-FILE.in | tee OUT-FILE.out
"""


def get_recycled_num_count(begin, end):
    count = 0
    for n in range(begin, end):
        n_set = set()
        n_str = str(n)

        for i in range(1, len(n_str)):
            new_num = int(n_str[i:] + n_str[:i])
            if n < new_num <= end:
                n_set.add(new_num)
        count += len(n_set)
    return count


def solve(num_cases):
    for i in range(1, num_cases+1):
        case = input().split(' ')
        range_begin, range_end = int(case[0]), int(case[1])
        solved = get_recycled_num_count(range_begin, range_end)
        print('Case #{num}: {solved}'.format(num=i, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
