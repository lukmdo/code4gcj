#!/usr/bin/env python

import alien
import unittest

class Test_GCJ(unittest.TestCase):
    
    def setUp(self):
        self.got = [
            ['9', '0123456789', 'oF8'],
            ['Foo', 'oF8', '0123456789'],
            ['13', '0123456789abcdef', '01'],
            ['CODE', 'O!CDE?', 'A?JM!.'],
        ]
        self.decimal_expected = [9, 9, 19, 454]
        self.expected = ['Foo', '9', '10011', 'JAM!'] 
    
    def test_decode_to_decimal(self):
        for i, data in enumerate(self.got):
            self.failUnlessEqual(alien.decode_to_decimal(data[0], data[1]), self.decimal_expected[i])
    
    def test_encode_decimal(self):
        for i, data in enumerate(self.decimal_expected):
            self.failUnlessEqual(alien.encode_decimal(data, self.got[i][2]), self.expected[i])                                           
    
    def test_translate(self):
        for i, data in enumerate(self.got):
            self.failUnlessEqual(alien.translate(*data), self.expected[i])        

if __name__ == '__main__':
    unittest.main()