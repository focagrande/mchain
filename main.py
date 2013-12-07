# --*- coding: utf-8 -*-
import sys
from mchain import Mchain

def main(ct, dg, mw):
    mc = Mchain()
    return mc.generate(ct, dg, mw)

if __name__ == '__main__':

    try:
        corpus_fname = sys.argv[1]
        degree = sys.argv[2]
        maxwords = sys.argv[3]
    except IndexError:
        print "usage: %s corpus_file degree maxwords" % sys.argv[0]
        sys.exit(1)

    with open(corpus_fname, 'r') as f:
        corpus_txt = f.read()

    print main(corpus_txt, int(degree), int(maxwords))
