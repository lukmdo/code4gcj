#!/usr/bin/python3
"""
https://code.google.com/codejam/contest/1277486/dashboard#s=p1

python Bmusic.py < IN-FILE.in > OUT-FILE.out
python -u Bmusic.py < IN-FILE.in | tee OUT-FILE.out
"""


def get_substrings(t):
    length = len(t)
    return set(t[b:e] for b in range(length) for e in range(length, b, -1))


def get_titles_queries(titles):
    if len(titles) == 1:
        return [(titles[0], '')]

    title_query_pairs = []

    title_substring = [get_substrings(str.upper(t)) for t in titles]
    substring_is_duplicate_map = dict()
    for ts in title_substring:
        for s in ts:
            substring_is_duplicate_map[s] = s in substring_is_duplicate_map
    substring_duplicates = set(
        k for k, v in substring_is_duplicate_map.items() if v is True)

    for i, title in enumerate(titles):
        substring_options = set(title_substring[i]).difference(substring_duplicates)
        sorted_substring_options = sorted(
            substring_options, key=lambda s: (len(s), s))
        if sorted_substring_options:
            query = sorted_substring_options[0]
        else:
            query = None
        title_query_pairs.append((title, query))

    return title_query_pairs


def solve(num_cases):
    for i in range(1, num_cases+1):
        num_titles = input()
        titles = [input() for i in range(int(num_titles))]

        print('Case #{num}:'.format(num=i))

        title_query_pairs = get_titles_queries(titles)
        for title, query in title_query_pairs:
            if query is None:
                print(':(')
            else:
                print('"{}"'.format(query))


if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
