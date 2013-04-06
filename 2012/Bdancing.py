#!/usr/bin/python3
"""
python Bdancing.py < IN-FILE.in > OUT-FILE.out
python Bdancing.py < IN-FILE.in | tee OUT-FILE.out
"""

def dancer_selector(n_googlers, n_surprising, min_score, totals):
    n_googlers_pass = 0
    for t in sorted(totals, reverse=True):
        div, mod = divmod(t, 3)
        if t == 0 and min_score > 0:
            continue
        if min_score <= div:
            n_googlers_pass += 1
            continue

        if mod == 0:
            if min_score == div + 1 and n_surprising and (div-1) >= 0:
                n_surprising -= 1
                n_googlers_pass += 1
        elif mod == 1:
            if min_score == div + 1:
                n_googlers_pass += 1
        elif mod == 2:
            if min_score == div + 1:
                n_googlers_pass += 1
            elif min_score == div + 2 and n_surprising:
                n_surprising -= 1
                n_googlers_pass += 1

    return n_googlers_pass


def solve(num_cases):
    for i in range(1, num_cases+1):
        case = input()
        n, s, p, *totals = map(int, case.split())
        solved = dancer_selector(n, s, p, totals)
        print('Case #{num}: {solved}'.format(num=i, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
