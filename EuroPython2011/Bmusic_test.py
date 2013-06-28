import unittest
from Bmusic import get_titles_queries


class TestFoo(unittest.TestCase):
    def test_case1(self):
        titles = [
            'A Perfect Circle - Gravity',
            'Aimee Mann - You Do',
            'Aqualung - Cinderella',
            'Arcade Fire - Haiti',
            'Art of Noise - Pleure',
            'ATB - Marrakech']
        titles_queries = get_titles_queries(titles)
        expected_titles_queries = [
            ('A Perfect Circle - Gravity', 'V'),
            ('Aimee Mann - You Do', ' D'),
            ('Aqualung - Cinderella', 'Q'),
            ('Arcade Fire - Haiti', ' F'),
            ('Art of Noise - Pleure', 'S'),
            ('ATB - Marrakech', 'B')]
        self.assertEqual(titles_queries, expected_titles_queries)

    def test_case2(self):
        titles = [
            'Hybrid - Altitude',
            'Kings of Convenience - The Build-up']
        titles_queries = get_titles_queries(titles)
        expected_titles_queries = [
            ('Hybrid - Altitude', 'A'),
            ('Kings of Convenience - The Build-up', 'C')]
        self.assertEqual(titles_queries, expected_titles_queries)

    def test_case3(self):
        titles = [
            'aaaaaaaabb',
            'aaaaaaabbb',
            'ababababab']
        titles_queries = get_titles_queries(titles)
        expected_titles_queries = [
            ('aaaaaaaabb', "AAAAAAAA"),
            ('aaaaaaabbb', "BBB"),
            ('ababababab', "BA")]
        self.assertEqual(titles_queries, expected_titles_queries)

    def test_case4(self):
        titles = [
            'butter',
            'fly',
            'butterfly']
        titles_queries = get_titles_queries(titles)
        expected_titles_queries = [
            ('butter', None),
            ('fly', None),
            ('butterfly', 'RF')]
        self.assertEqual(titles_queries, expected_titles_queries)

    def test_case5(self):
        titles = [
            'Unknown Artist - Track One']
        titles_queries = get_titles_queries(titles)
        expected_titles_queries = [
            ('Unknown Artist - Track One', '')]
        self.assertEqual(titles_queries, expected_titles_queries)


if __name__ == '__main__':
    unittest.main()
