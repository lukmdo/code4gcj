#!/usr/bin/env python

import bot
import unittest

class Test_GCJ(unittest.TestCase):
  def setUp(self):
    self.got = [ 
      ['4', 'O', '2', 'B', '1', 'B', '2', 'O', '4'],
      ['3', 'O', '5', 'O', '8', 'B', '100'],
      ['2', 'B', '2', 'B', '1'],
      ['1', 'B', '10'],
      ['2', 'B', '3', 'B', '3'],
      ['2', 'B', '3', 'B', '4'],
      ['2', 'B', '3', 'B', '1'], 
      ['3', 'B', '3', 'B', '1', 'O', '5'],
      ['6', 'B', '30', 'O', '31', 'B', '12', 'O', '12', 'B', '28', 'O', '28'] 
    ]
    self.expected = [6, 100, 4, 10, 4, 5, 6, 7, 68]                                         

  def test_will_turn_on(self):
    for i, data in enumerate(self.got):
      self.failUnlessEqual(bot.solve_case(int(data[0]), *data[1:]), self.expected[i])        

if __name__ == '__main__':
  unittest.main()
