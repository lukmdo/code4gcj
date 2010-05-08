#!/usr/bin/env python
# encoding: utf-8

from optparse import OptionParser

def will_turn_on(devs_num, snaps_num):
    all_devs_on_mask = (2**devs_num)-1
    return (snaps_num & all_devs_on_mask) == all_devs_on_mask

def main():
  """Main function code. Implementing:
      1. parsig args (-i, --in-file)
      2. iterating and transorming input data (results stored in table)
      3. printing out results in required format
  """
  parser = OptionParser(usage="usage: %prog [options] arg") 
  parser.add_option("-i", "--in-file", dest="in_filename", help="provide input data by specifing filename")
  (options, args) = parser.parse_args() 
  if options.in_filename is None:
      parser.print_usage()
      exit(0)
  results = []
  for devs_num, snaps_num in gen_next_case(options.in_filename):
      if will_turn_on(devs_num, snaps_num):
          results.append("ON")
      else:
          results.append("OFF") 
  for i, result in enumerate(results):    
      print "Case #%i: %s" % (i+1, result)

def gen_next_case(filename):
  """Wrap the imput file format and return a list of
      -
      -
      -
  It uses generator to return them one by one."""
  next_line = lambda f: f.readline().rstrip()
  with open(filename, "r") as f:
      num_of_cases = int(next_line(f))
      next_case = next_line(f)
      while next_case:
          devs_num, snaps_num = next_case.split(' ')
          next_case = next_line(f)
          yield int(devs_num), int(snaps_num) 

if __name__ == '__main__':
  main()

