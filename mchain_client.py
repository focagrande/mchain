# --*- coding: utf-8 -*-

import sys
import jsonrpclib

server = jsonrpclib.Server('http://localhost:5000')


def request(ct, dg, mw):

    result = server.generate(ct, dg, mw)
    return result.encode('latin-1', 'replace')


if __name__ == '__main__':

    try:
        corpus_fname = sys.argv[1]
        degree = int(sys.argv[2])
        maxwords = int(sys.argv[3])
    except IndexError:
        print "usage %s corpus_file degree maxwords" % (sys.argv[0])
        sys.exit(1)

with open(corpus_fname, 'r') as f:
    corpus_txt = f.read()

print request(corpus_txt, degree, maxwords)
