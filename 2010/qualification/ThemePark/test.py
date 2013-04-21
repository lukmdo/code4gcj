#!/usr/bin/env python

import park
import unittest

class Test_GCJ(unittest.TestCase):
    
    def setUp(self):
        self.got = [
            [4, 6, (1, 4, 2, 1,)],
            [100, 10, (1,)],
            [5, 5, (2, 4, 2, 3, 4, 2, 1, 2, 1, 3,)],
        ]
        self.expected = [21, 100, 20]                                         
        
    def test_get_tc(self):
        for i, data in enumerate(self.got):
            self.failUnlessEqual(park.get_tc(*data), self.expected[i])     

if __name__ == '__main__':
    unittest.main()