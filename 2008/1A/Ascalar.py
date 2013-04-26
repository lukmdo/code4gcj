#!/usr/bin/python3
"""
python Ascalar.py < IN-FILE.in > OUT-FILE.out
python -u Ascalar.py < IN-FILE.in | tee OUT-FILE.out
"""


def get_min_scalar_product(vector_a, vector_b):
    vector_a_asc = sorted(vector_a)
    vector_b_desc = sorted(vector_b, reverse=True)
    return sum(n * m for n, m in zip(vector_a_asc, vector_b_desc))


def solve(num_cases):
    for i in range(1, num_cases+1):
        case = input()
        vector_a = map(int, input().split())
        vector_b = map(int, input().split())
        solved = get_min_scalar_product(vector_a, vector_b)
        print('Case #{num}: {solved}'.format(num=i, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
