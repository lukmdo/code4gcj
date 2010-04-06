#!/usr/bin/env python

from optparse import OptionParser
# from pprint import pprint

def main():
    parser = OptionParser(usage="usage: %prog [options] arg") 
    parser.add_option("-i", "--in-file", dest="in_filename", help="provide input data by specifing filename")
    (options, args) = parser.parse_args() 
    if options.in_filename is None:
        parser.print_usage()
        exit(0)
    results = []    
    next_case = gen_next_case(options.in_filename)
    for engines, phrases in next_case:
        engine_in_use = None
        score = 0
        if len(phrases) == 0:
            results.append(score)
            continue
        for i, phrase in enumerate(phrases):            
            if engine_in_use is None:
                engine_in_use = suggest(engines, phrases, exclude=phrases[0])
            elif engine_in_use == phrase:
                engine_in_use = suggest(engines, phrases[i:], exclude=engine_in_use)
                score += 1
        results.append(score)   
    for i, result in enumerate(results):    
        print "Case #%i: %i" % (i+1, result)

def suggest(engines, phrases, exclude=False):
    if exclude:
        engines = engines.difference(exclude)
    not_used_engines = engines.difference(set(phrases))
    if not_used_engines:
        return not_used_engines.pop()
    engine_score = dict()
    for engine in engines:
        engine_score[engine] = phrases.index(engine)
    best_score = max(engine_score.values())
    for engine, score in engine_score.items():
        if score == best_score:
            return engine   

def gen_next_case(filename):
    next_line = lambda f: f.readline().rstrip()
    with open(filename, "r") as f:
        num_of_cases = int(next_line(f))
        engines_lines = next_line(f)
        while engines_lines: 
            engines_lines = int(engines_lines)            
            engines = set([next_line(f) for i in xrange(engines_lines)])
            phrases_lines = int(next_line(f))
            phrases = [next_line(f) for i in xrange(phrases_lines)]
            engines_lines = next_line(f)
            yield engines, phrases
                     
class DataFile(object):
    def __init__(self, name):
        self.file = open(name, "r")
        self.num_of_cases = int(self.next_line()) 
    def next_line(self):
        return self.file.readline().rstrip('\r\n')
    def get_next_case(self):
        while True:
            engines_lines = int(self.next_line())
            engines = set([self.next_line() for i in xrange(engines_lines)])
            phrases_lines = int(self.next_line())
            phrases = [self.next_line() for i in xrange(phrases_lines)]
            yield [engines, phrases]            
           
if __name__ == "__main__":
    main() 