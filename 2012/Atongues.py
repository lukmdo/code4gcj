#!/usr/bin/python3
"""
python Atongues.py < IN-FILE.in > OUT-FILE.out
python Atongues.py < IN-FILE.in | tee OUT-FILE.out
"""

# import string
# MAP = dict((c, '?') for c in string.ascii_lowercase)
# _in = (
#     'ejp mysljylc kd kxveddknmc re jsicpdrysi'
#     'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
#     'de kr kd eoya kw aej tysr re ujdr lkgc jv')
# _out = (
#     'our language is impossible to understand'
#     'there are twenty six factorial possibilities'
#     'so it is okay if you want to just give up')
# DATA = zip(_in, _out)
# MAP.update(DATA)
# for key in sorted(MAP):
#     print(key, MAP[key])

TRANSLATION_TABLE = str.maketrans(
    'y n f i c w l b k u o m x s e v z p d r j g a t h a q',
    'a b c d e f g h i j k l m n o p q r s t u v y w x y z'
)


def googlerese_decode(input_str):
    return str.translate(input_str, TRANSLATION_TABLE)


def solve(num_cases):
    for i in range(1, num_cases+1):
        case = input()
        solved = googlerese_decode(case)
        print('Case #{num}: {solved}'.format(num=i, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
