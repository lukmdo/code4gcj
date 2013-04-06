import unittest
from Atongues import googlerese_decode


class TestFoo(unittest.TestCase):
    def test_case1(self):
        in_str = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
        out_str = googlerese_decode(in_str)
        self.assertEqual(out_str, 'our language is impossible to understand')

    def test_case2(self):
        in_str = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
        out_str = googlerese_decode(in_str)
        self.assertEqual(
            out_str, 'there are twenty six factorial possibilities')

    def test_case3(self):
        in_str = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
        out_str = googlerese_decode(in_str)
        self.assertEqual(out_str, 'so it is okay if you want to just give up')

if __name__ == '__main__':
    unittest.main()
