#!/usr/bin/python3
"""
python Auniverse.py < IN-FILE.in > OUT-FILE.out
python Auniverse.py < IN-FILE.in | tee OUT-FILE.out
"""


def get_min_switch_count(engines, queries):
    # prior ordering engines by global rating does not bring any effect

    def best_local_engine(queries, engines):
        def next_switch_at(e):
            try:
                pos = queries.index(e)
            except ValueError:
                pos = len(queries) + 1
            return pos
        return max(engines, key=next_switch_at)

    switch_count = 0
    current_engine = best_local_engine(queries, engines)
    for i, q in enumerate(queries):
        if q == current_engine:
            switch_count += 1
            current_engine = best_local_engine(queries[i:], engines)

    return switch_count


def solve(num_cases):
    for i in range(1, num_cases + 1):

        num_search_engines = int(input())
        search_engines = [input() for i in range(num_search_engines)]
        num_search_queries = int(input())
        search_queries = [input() for i in range(num_search_queries)]

        solved = get_min_switch_count(search_engines, search_queries)
        print('Case #{num}: {solved}'.format(num=i, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
