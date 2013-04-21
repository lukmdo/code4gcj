#!/usr/bin/env python
# encoding: utf-8

from optparse import OptionParser

def cycle_cost(capacity, queue):
    count = 0
    i = 0
    for i, g in enumerate(queue):
        if count + g > capacity:
            break
        count += g
    return (tuple(queue[i:]+queue[0:i]), count)

def get_tc(cycles_num, capacity, queue):
    seen_queues = []
    queue_cost = {}
    tc = 0
    for i in xrange(cycles_num):
        if queue in seen_queues:
            seen_at = seen_queues.index(queue)
            cycles_ahead = cycles_num - (i + 1) 
            (i, x) = divmod(cycles_ahead, i-seen_at)
            reset = 0
            if seen_at > 0:
                reset = queue_cost[seen_queues[seen_at-1]]
            return tc + (tc-reset)*i + queue_cost[seen_queues[seen_at+x]] - reset
        seen_queues.append(queue)
        (next_queue, c) = cycle_cost(capacity, queue)
        tc += c
        queue_cost[queue] = tc
        queue = next_queue
    return tc  
    
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
    i = 0 
    for cycles_num, capacity, groups in gen_next_case(options.in_filename): 
        i += 1
        print "Case #%i: %i" % (i, get_tc(cycles_num, capacity, tuple(groups)))   

def gen_next_case(filename):
    """Wrap the imput file format and return cycles_num, capacity, groups. 
    It uses generator to return them one by one."""
    next_line = lambda f: f.readline().rstrip()
    with open(filename, "r") as f:
        num_of_cases = int(next_line(f))
        data = next_line(f)
        while data:
            cycles_num, capacity, groups_count = data.split(' ')
            cycles_num = int(cycles_num)
            capacity = int(capacity)
            groups = [int(x) for x in next_line(f).split(' ')]
            data = next_line(f)
            yield cycles_num, capacity, groups           

if __name__ == '__main__':
    main()
