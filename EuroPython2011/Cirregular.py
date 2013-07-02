#!/usr/bin/python3
"""
http://code.google.com/codejam/contest/1277486/dashboard#s=p2

python Cirregular.py < IN-FILE.in > OUT-FILE.out
python -u Cirregular.py < IN-FILE.in | tee OUT-FILE.out
"""
import re


SPELL_REGEX = re.compile(r"""
(?P<begin>[aeiou][^aeiou]*?[aeiou])
(?P<mid>[^aeiou]*?[aeiou]\w*?)
(?P=begin)
""", re.VERBOSE)


def is_valid_spell(word):
    return SPELL_REGEX.search(word) is not None


def solve(num_cases):
    for i in range(1, num_cases + 1):
        name = input()
        solution = 'Spell!' if is_valid_spell(name) else 'Nothing.'
        print('Case #{num}: {solution}'.format(num=i, solution=solution))


if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
