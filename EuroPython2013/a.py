#!/usr/bin/python3
"""
python a.py < IN-FILE.in > OUT-FILE.out
python -u a.py < IN-FILE.in | tee OUT-FILE.out
"""


def get_cost(seq):
    num = 0
    max_str = ''

    for item in seq:
        if item >= max_str:
            max_str = item
        else:
            num += 1

    return num


def solve(num_cases):
    for i in range(1, num_cases + 1):
        case_info = int(input())
        case_data = [input() for i in range(case_info)]
        solved = get_cost(case_data)
        print('Case #{num}: {solved}'.format(num=i, solved=solved))


if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
