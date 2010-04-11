#!/usr/bin/env python 

from optparse import OptionParser
    
def min_scalar_product(v1, v2, n=None):
    """Calculates the minimum scalar product for given vectors v1,v2."""
    v1.sort()
    v2.sort()
    if n is None:
        n = len(v1)
    min_scalar_product = 0
    for i in xrange(n):
        min_scalar_product += min_single_product(v1, v2)
    return min_scalar_product    
    
def min_single_product(v1, v2):
    """Assumes v1, v2 are allready sorted. It does in-place podivication
    of v1, v2 to remove used coorsinates."""    
    has_min_value, has_max_value = v1, v2 
    if has_min_value[0] * has_max_value[-1] > has_min_value[-1] * has_max_value[0]:
        has_min_value, has_max_value = v2, v1
    min_product = has_min_value[0] * has_max_value[-1]
    # logging.warn('V1: %s V2: %s .Using max: %i min: %i ==> %i' % (','.join(map(lambda x: str(x), v1)), ','.join(map(lambda x: str(x), v2)), has_max_value[-1], has_min_value[0], min_product))
    has_min_value[:] = has_min_value[1:]  # mofify (v1 or v2) also 
    has_max_value[:] = has_max_value[:-1] # mofify (v1 or v2) also
    return min_product  

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
    for v1, v2, n in gen_next_case(options.in_filename):
        results.append(min_scalar_product(v1, v2, n))
    for i, result in enumerate(results):    
        print "Case #%i: %i" % (i+1, result)   
    
def gen_next_case(filename):
    """Wrap the imput file format and return a list of
       - v1 as list of integers (first vector)
       - v2 as list of integers (second vector)
       - n as vector size (number of coordinates)
    It uses generator to return them one by one."""
    next_line = lambda f: f.readline().rstrip()
    with open(filename, "r") as f:
        num_of_cases = int(next_line(f))
        next_case_size = next_line(f)
        while next_case_size:
            case_size = int(next_case_size)
            v1 = map(lambda x: int(x), next_line(f).split(' '))           
            v2 = map(lambda x: int(x), next_line(f).split(' '))           
            next_case_size = next_line(f)
            yield v1, v2, case_size

if __name__ == "__main__":
    main()
