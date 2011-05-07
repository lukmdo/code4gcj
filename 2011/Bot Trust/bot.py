#!/usr/bin/env python
# encoding: utf-8
"""Code for #gcj 2011 - the Bot Trust""" 

from __future__ import with_statement
from optparse import OptionParser

class Bot(object):
  def __init__(self, name, init_pos, *items):
    self.pos = init_pos
    self.name = name
    self.click_pos_all = [p for b, p in reversed(items) if b == name]
 
  def move_on(self, max_hops):
    dist = self.get_next_click_pos() - self.pos
    hops = abs(min(dist, max_hops, key=abs))
    if dist < 0:
      self.pos -= hops
    else:
      self.pos += hops 
    
  def get_next_click_pos(self):
    if len(self.click_pos_all) == 0:
      return self.pos
    return self.click_pos_all[-1]
      
  def clicked(self):
    self.click_pos_all.pop()
    
  
def solve_case(num, *items):
  items = [(items[2*i], int(items[2*i+1])) for i in range(num)]
  bot_by_name = { 
    'O': Bot('O', 1, *items), 
    'B': Bot('B', 1, *items) 
  }  
  timer = 0
  for bot_name, pos in items:
    dist = abs(bot_by_name.get(bot_name).pos-pos) + 1
    for name in 'O', 'B':
      bot = bot_by_name.get(name)
      bot.move_on(dist)
      if name == bot_name:
        bot.clicked()
    timer += dist
  return timer

def main():
  """Main function code. Implementing:
  1. parsig args (-i, --in-file)
  2. iterating and transorming input data (results stored in table)
  3. printing out results in required format
  """
  parser = OptionParser(usage="usage: %prog [options] arg") 
  parser.add_option("-i", "--in-file", dest="in_filename", 
                    help="provide input data by specifing filename")
  (options, args) = parser.parse_args() 
  if options.in_filename is None:
    parser.print_usage()
    exit(0)
  results = []
  for num, items in gen_next_case(options.in_filename):
    result = solve_case(num, *items)
    results.append(result)
  for i, result in enumerate(results):    
    print "Case #%i: %s" % (i+1, result)

def gen_next_case(filename):
  """Wrap the imput file format and return a list of:
  It uses generator to return them one by one."""
  next_line = lambda f: f.readline().rstrip()
  with open(filename, "r") as f:
    num_of_cases = int(next_line(f))
    next_case = next_line(f)
    while next_case:
      items = next_case.split(' ')
      next_case = next_line(f)
      yield int(items[0]), items[1:] 

if __name__ == '__main__':
  main()
