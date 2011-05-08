#!/usr/bin/env python

import magicka
import unittest

class Test_GCJ(unittest.TestCase):
  def setUp(self):
    self.got = [
      # from Sample
      ['0', '0', '2', 'EA'],
      ['1', 'QRI', '0', '4', 'RRQR'],
      ['1', 'QFT', '1', 'QF', '7', 'FAQFDFQ'],
      ['1', 'EEZ', '1', 'QE', '7', 'QEEEERA'],
      ['0', '1', 'QW', '2', 'QW'],
      # from Problem description
      ['1', 'QFT', '1', 'RF', '2', 'QF'],
      ['1', 'QFT', '1', 'RF', '3', 'QEF'],
      ['1', 'QFT', '1', 'RF', '3', 'RFE'],
      ['1', 'QFT', '1', 'RF', '3', 'REF'],
      ['1', 'QFT', '1', 'RF', '3', 'RQF'],
      ['1', 'QFT', '1', 'RF', '3', 'RFQ'],
      # mine
      ['0', '0', '0'],
      ['1', 'EEZ', '1', 'QE', '0'],
    ]
    self.expected = [
      ['E', 'A'], 
      ['R', 'I', 'R'], 
      ['F', 'D', 'T'], 
      ['Z', 'E', 'R', 'A'], 
      [],
      
      ['T'],
      ['Q', 'E', 'F'],
      ['E'],
      [],
      ['R', 'T'],
      ['Q'],
      
      [],
      [],
    ]                                         

  def test_solve_case(self):
    for i, data in enumerate(self.got):
      self.failUnlessEqual(magicka.solve_case(*data), self.expected[i], 
        "Test %s for %s returned %s instead of %s" % (i, data, magicka.solve_case(*data), self.expected[i]))        

if __name__ == '__main__':
  unittest.main()
