#!/usr/bin/python3
"""
python Arotate.py < IN-FILE.in > OUT-FILE.out
python -u Arotate.py < IN-FILE.in | tee OUT-FILE.out
"""


class Winners(object):
    BOTH = 'Both'
    RED = 'Red'
    BLUE = 'Blue'


def _rotate(data):
    """basing that its NxN and search is symmetric in all directions:
    - does change the gravity
    - skip rotation
    """
    dim = len(data[0])

    rotated = []
    str_format = '{:.>' + str(dim) + '}'
    for row in data:
        non_empty = ''.join(e for e in row if e != '.')
        row_rotated = str_format.format(non_empty)
        rotated.append(row_rotated)

    return rotated


def _who_won(n, m, rotated, k):
    # k is always >= 3 - eliminates k=1 (all winners)
    dim = len(rotated[0])
    got = rotated[n][m]
    if got == '.':
        return None
    winner = Winners.RED if got == 'R' else Winners.BLUE  # too small for map

    # up
    if (n + 1) >= k:
        won = all(rotated[n - i][m] == got for i in range(1, k))
        if won:
            return winner
    # left
    if (m + 1) >= k:
        won = all(rotated[n][m - i] == got for i in range(1, k))
        if won:
            return winner
    # left-up diagonal
    if (n + 1) >= k and (m + 1) >= k:
        won = all(rotated[n - i][m - i] == got for i in range(1, k))
        if won:
            return winner
    # right-up diagonal
    if (n + 1) >= k and (k + m) <= dim:
        won = all(rotated[n - i][m + i] == got for i in range(1, k))
        if won:
            return winner


def get_winner(data, k):
    dim = len(data[0])
    if k > dim:
        return None
    r = _rotate(data)
    winners = set(_who_won(n, m, r, k) for n in range(dim) for m in range(dim))
    winners -= set([None])
    num_winners = len(winners)

    if num_winners == 2:
        return Winners.BOTH
    elif num_winners == 1:
        return winners.pop()
    else:
        return None


def solve(num_cases):
    for i in range(1, num_cases+1):
        case = input().split()
        num_rows, k = int(case[0]), int(case[1])
        data = [input() for _ in range(num_rows)]
        solved = get_winner(tuple(data), k) or 'Neither'
        print('Case #{num}: {solved}'.format(num=i, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
