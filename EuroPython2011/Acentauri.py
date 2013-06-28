#!/usr/bin/python3
"""
https://code.google.com/codejam/contest/1277486/dashboard#s=p0

python Acentauri.py < IN-FILE.in > OUT-FILE.out
python -u Acentauri.py < IN-FILE.in | tee OUT-FILE.out
"""
import string

VOWELS = set('aeiouAEIOU')
CONSONANTS = set(string.ascii_letters) - VOWELS - set('yY')


def get_the_sting(country_name):
    last_char = country_name[-1]

    if last_char in set('yY'): msg = '{} is ruled by nobody.'
    elif last_char in VOWELS: msg = '{} is ruled by a queen.'
    elif last_char in CONSONANTS: msg = '{} is ruled by a king.'

    return msg.format(country_name)

def solve(num_cases):
    for i in range(1, num_cases + 1):
        name = input()
        solution = get_the_sting(name)
        print('Case #{num}: {solution}'.format(num=i, solution=solution))


if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
