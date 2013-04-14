import unittest
from Atic import get_game_state
from Atic import GameState




class TestFoo(unittest.TestCase):
    def test_case1(self):
        game_matrix = (
            ('X', 'X', 'X', 'T'),
            ('.', '.', '.', '.'),
            ('O', 'O', '.', '.'),
            ('.', '.', '.', '.'),
        )
        state_name = get_game_state(game_matrix)
        self.assertEqual(state_name, GameState.X_WON)

    def test_case2(self):
        game_matrix = (
            ('X', 'O', 'X', 'T'),
            ('X', 'X', 'O', 'O'),
            ('O', 'X', 'O', 'X'),
            ('X', 'X', 'O', 'O'),
        )
        state_name = get_game_state(game_matrix)
        self.assertEqual(state_name, GameState.DRAW)

    def test_case3(self):
        game_matrix = (
            ('X', 'O', 'X', '.'),
            ('O', 'X', '.', '.'),
            ('.', '.', '.', '.'),
            ('.', '.', '.', '.'),
        )
        state_name = get_game_state(game_matrix)
        self.assertEqual(state_name, GameState.NOT_COMPLETED)


    def test_case4(self):
        game_matrix = (
            ('O', 'O', 'X', 'X'),
            ('O', 'X', 'X', 'X'),
            ('O', 'X', '.', 'T'),
            ('O', '.', '.', 'O'),
        )
        state_name = get_game_state(game_matrix)
        self.assertEqual(state_name, GameState.O_WON)


    def test_case5(self):
        game_matrix = (
            ('X', 'X', 'X', 'O'),
            ('.', '.', 'O', '.'),
            ('.', 'O', '.', '.'),
            ('T', '.', '.', '.'),
        )
        state_name = get_game_state(game_matrix)
        self.assertEqual(state_name, GameState.O_WON)

    def test_case6(self):
        game_matrix = (
            ('O', 'X', 'X', 'X'),
            ('X', 'O', '.', '.'),
            ('.', '.', 'O', '.'),
            ('.', '.', '.', 'O'),
        )
        state_name = get_game_state(game_matrix)
        self.assertEqual(state_name, GameState.O_WON)


if __name__ == '__main__':
    unittest.main()
