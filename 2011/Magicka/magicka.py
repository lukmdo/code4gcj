#!/usr/bin/env python
# encoding: utf-8
"""Code for #gcj 2011 - Magicka""" 

from __future__ import with_statement
from optparse import OptionParser

def play_magicka(c_num, d_num, l_num, c, d, l):
  for i in range(1, len(l)):    
    if c_num > 0:
      for k in (l[i-1], l[i]), (l[i], l[i-1]):
        if c.has_key(k):
          l = l[:i-1] + c.get(k) + l[i+1:]
          return play_magicka(c_num, d_num, l_num, c, d, l) 
    if d_num > 0:
      for n, xchar in enumerate(l[:i]):
        for k in (xchar, l[i]), (l[i], xchar):
          if d.has_key(k):
            l = l[i+1:]                                     
            return play_magicka(c_num, d_num, l_num, c, d, l) 
  return l
    
  
def solve_case(*items):
  c_num = int(items[0])
  d_num = int(items[c_num+1])
  l_num = int(items[c_num+1+d_num+1])
  c = dict(((items[i+1][0], items[i+1][1]), items[i+1][2]) for i in range(c_num))
  d = dict(((items[c_num+1+i+1][0], items[c_num+1+i+1][1]), 1) for i in range(d_num))
  l = ""
  if l_num > 0:
    l = items[c_num+1+d_num+1+1]
  l = play_magicka(c_num, d_num, l_num, c, d, l)
  return list(l)


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
  for items in gen_next_case(options.in_filename):
    result = solve_case(*items)
    results.append(result)
  for i, result in enumerate(results):
    out = "[" + ', '.join(result) + "]"    
    print "Case #%i: %s" % (i+1, out)

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
      yield items 

if __name__ == '__main__':
  main()
