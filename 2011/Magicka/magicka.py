#!/usr/bin/env python
# encoding: utf-8
"""Code for #gcj 2011 - Magicka"""

from optparse import OptionParser

def play_magicka(c_num, d_num, l_num, c, d, l):
  l_out = ""
  for i in range(l_num):
    l_out += l[i]
    if c_num > 0:
      k = l_out[-2:]
      if c.has_key(k):
        l_out = l_out[:-2] + c.get(k)
        continue
    if d_num > 0:
      for n in range(len(l_out)):
        k = "".join([l_out[n], l_out[-1]])
        if d.has_key(k):
          l_out = ""
          break
  return l_out

def solve_case(*items):
  c_num = int(items[0])
  d_num = int(items[c_num+1])
  l_num = int(items[c_num+1+d_num+1])
  c, d = dict(), dict()
  for k, v in [(items[i+1][:2], items[i+1][2]) for i in range(c_num)]:
    c[k] = c[k[::-1]] = v
  for k in [items[c_num+1+i+1] for i in range(d_num)]:
    d[k] = d[k[::-1]] = 1
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
