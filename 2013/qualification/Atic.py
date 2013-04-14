#!/usr/bin/python3
"""
python Atic.py < IN-FILE.in > OUT-FILE.out
python -u Atic.py < IN-FILE.in | tee OUT-FILE.out
"""

GAME_DIM = 4

class GameState(object):
    X_WON = 'X won'
    O_WON = 'O won'
    DRAW = 'Draw'
    NOT_COMPLETED = 'Game has not completed'

_X_ROW = ('X', 'X', 'X', 'X')
_O_ROW = ('O', 'O', 'O', 'O')

_X_WIN_COMBINATIONS = set([_X_ROW])
_O_WIN_COMBINATIONS = set([_O_ROW])
for t_pos in range(GAME_DIM):
    new_x_win_row = list(_X_ROW)
    new_x_win_row[t_pos] = 'T'
    _X_WIN_COMBINATIONS.add(tuple(new_x_win_row))

    new_o_win_row = list(_O_ROW)
    new_o_win_row[t_pos] = 'T'
    _O_WIN_COMBINATIONS.add(tuple(new_o_win_row))


def get_game_state(game_matrix):
    def who_won(searie):
        searie = tuple(searie)
        if searie in _X_WIN_COMBINATIONS:
            return GameState.X_WON
        if searie in _O_WIN_COMBINATIONS:
            return GameState.O_WON

    # horizontal
    for row in game_matrix:
        winner = who_won(row)
        if winner:
            return winner
    # vertical
    for col_num in range(GAME_DIM):
        col = [game_matrix[row_num][col_num] for row_num in range(GAME_DIM)]
        winner = who_won(col)
        if winner:
            return winner

    # diagonal
    diag_one = [game_matrix[num][num] for num in range(GAME_DIM)]
    diag_two = [game_matrix[num][GAME_DIM-1-num] for num in range(GAME_DIM)]
    for diag in [diag_one, diag_two]:
        winner = who_won(diag)
        if winner:
            return winner

    elements = set()
    for row in game_matrix:
        elements.update(row)
    is_completed = '.' not in elements

    # no winner then just draw or not complete
    return GameState.DRAW if is_completed else GameState.NOT_COMPLETED



def solve(num_cases):
    for i in range(1, num_cases+1):
        game_matrix = [tuple(input()) for row_num in range(GAME_DIM)]
        solved = get_game_state(game_matrix)
        print('Case #{num}: {solved}'.format(num=i, solved=solved))
        sep_line = input()

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
