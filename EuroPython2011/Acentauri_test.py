import unittest
from Acentauri import get_the_sting


class TestFoo(unittest.TestCase):
    def test_case1(self):
        got = get_the_sting('Mollaristan')
        self.assertEqual(got, 'Mollaristan is ruled by a king.')

    def test_case2(self):
        got = get_the_sting('Auritania')
        self.assertEqual(got, 'Auritania is ruled by a queen.')

    def test_case3(self):
        got = get_the_sting('Zizily')
        self.assertEqual(got, 'Zizily is ruled by nobody.')


if __name__ == '__main__':
    unittest.main()
