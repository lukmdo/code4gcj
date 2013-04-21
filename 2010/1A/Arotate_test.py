import unittest
from Arotate import get_winner
from Arotate import Winners


class TestFoo(unittest.TestCase):
    def test_case1(self):
        data = (
            '.......',
            '.......',
            '.......',
            '...R...',
            '...BB..',
            '..BRB..',
            '.RRBR..',)
        winner = get_winner(data, 3)
        self.assertEqual(winner, None)

    def test_case2(self):
        data = (
            '......',
            '......',
            '.R...R',
            '.R..BB',
            '.R.RBR',
            'RB.BBB',)
        winner = get_winner(data, 4)
        self.assertEqual(winner, Winners.BOTH)

    def test_case3(self):
        data = (
            'R...',
            'BR..',
            'BR..',
            'BR..',)
        winner = get_winner(data, 4)
        self.assertEqual(winner, Winners.RED)

    def test_case4(self):
        data = (
            'B..',
            'RB.',
            'RB.',)
        winner = get_winner(data, 3)
        self.assertEqual(winner, Winners.BLUE)


if __name__ == '__main__':
    unittest.main()
