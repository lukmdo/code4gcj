#!/usr/bin/env python 

from optparse import OptionParser
from math import log

def encode_decimal(num, alphabet):
    pass

def decode_to_decimal(seqence, alphabet):
    decimal = 0
    weight = len(alphabet)
    for i, c in enumerate(reversed(seqence)):
        decimal += alphabet.index(c) * (weight**i)
    return decimal 

def translate(seqence, from_alphabet, to_alphabet):
    return encode_decimal(decode_to_decimal(seqence, from_alphabet), to_alphabet)
    
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
    for num, l_from, l_to in gen_next_case(options.in_filename):
        results.append(translate(num, l_from, l_to))
    for i, result in enumerate(results):    
        print "Case #%i: %i" % (i+1, result)

def gen_next_case(filename):
    """Wrap the imput file format and return a list of
        -
        -
        -
    It uses generator to return them one by one."""
    next_line = lambda f: f.readline().rstrip()
    with open(filename, "r") as f:
        num_of_cases = int(next_line(f))
        next_num, next_l_from, next_l_to = next_line(f).split(' ')
        while next_num:
            num, l_from, l_to = next_num, next_l_from.split(), next_l_to.split()
            next_num, next_l_form, next_l_to = next_line(f).split(' ')
            yield source_num, l_from, l_to

if __name__ == "__main__":
    main()
    