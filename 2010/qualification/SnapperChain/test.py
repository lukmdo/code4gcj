#!/usr/bin/env python

import snap
import unittest

class Test_GCJ(unittest.TestCase):
    
    def setUp(self):
        self.got = [
            [1, 0],
            [1, 1],
            [4, 0],
            [4, 47],  
        ]
        self.expected = [False, True, False, True]                                         
    
    def test_will_turn_on(self):
        for i, data in enumerate(self.got):
            self.failUnlessEqual(snap.will_turn_on(*data), self.expected[i])        

if __name__ == '__main__':
    unittest.main()