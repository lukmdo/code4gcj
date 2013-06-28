import unittest
from Bwatersheds import get_label_matrix


class TestFoo(unittest.TestCase):
    def test_case1(self):
        matrix = [
            [9, 6, 3],
            [5, 9, 6],
            [3, 5, 6]]
        got_matrix = get_label_matrix(matrix)
        expected_matrix = [
            ['a', 'b', 'b'],
            ['a', 'a', 'b'],
            ['a', 'a', 'a']]
        self.assertEqual(got_matrix, expected_matrix)

    def test_case2(self):
        matrix = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 7]]
        got_matrix = get_label_matrix(matrix)
        expected_matrix = [
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b']]
        self.assertEqual(got_matrix, expected_matrix)

    def test_case3(self):
        matrix = [
            [7, 6, 7],
            [7, 6, 7]]
        got_matrix = get_label_matrix(matrix)
        expected_matrix = [
            ['a', 'a', 'a'],
            ['b', 'b', 'b']]
        self.assertEqual(got_matrix, expected_matrix)

    def test_case4(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [2, 9, 3, 9, 6],
            [3, 3, 0, 8, 7],
            [4, 9, 8, 9, 8],
            [5, 6, 7, 8, 9]]
        got_matrix = get_label_matrix(matrix)
        expected_matrix = [
            ['a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'b', 'b', 'a'],
            ['a', 'b', 'b', 'b', 'a'],
            ['a', 'b', 'b', 'b', 'a'],
            ['a', 'a', 'a', 'a', 'a']]
        self.assertEqual(got_matrix, expected_matrix)

    def test_case5(self):
        matrix = [
            [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
            [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]]
        got_matrix = get_label_matrix(matrix)
        expected_matrix = [
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'],
            ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
        self.assertEqual(got_matrix, expected_matrix)


if __name__ == '__main__':
    unittest.main()
