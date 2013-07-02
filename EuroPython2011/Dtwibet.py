#!/usr/bin/python3
"""
http://code.google.com/codejam/contest/1277486/dashboard#s=p2

python Dtwibet.py < IN-FILE.in > OUT-FILE.out
python -u Dtwibet.py < IN-FILE.in | tee OUT-FILE.out
"""
from collections import defaultdict


def get_num_whispers_a_day(followers):
    out = []
    num_followers = len(followers)
    tree = defaultdict(set)

    # build linked nodes tree
    for i, f in enumerate(followers, 1):
        tree[f].add(i)


    for i in range(1, num_followers + 1):
        new, old = tree[i].copy(), set([i])

        while new:
            item = new.pop()
            old.add(item)
            to_add = tree[item]
            to_add_not_old = to_add - old
            new = new.union(to_add_not_old)

        out.append(len(old))

    return out


def solve(num_cases):
    for i in range(1, num_cases + 1):
        print('Case #{num}:'.format(num=i))
        followers_number = input()
        followers_string = input()
        followers = list(map(int, followers_string.split(' ')))
        solution = get_num_whispers_a_day(followers)
        for s in solution:
            print(s)


if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
