# --*- coding: utf-8 -*-
import sys
from mchain import Mchain

def main(ct, dg):
    mc = Mchain(ct, dg)
    return mc.generate()

if __name__ == '__main__':

    try:
        corpus_fname = sys.argv[1]
        degree = sys.argv[2]
    except IndexError:
        print "usage: %s corpus_file degree" % sys.argv[0]
        sys.exit(1)

    with open(corpus_fname, 'r') as f:
        corpus_txt = f.read()

    print main(corpus_txt, int(degree))
