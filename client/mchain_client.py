# --*- coding: utf-8 -*-

"""Markov chain generator client example. Using jsonrpclib"""

import sys
import jsonrpclib


def request(url, crp, dgr, mwr):
    """Make a json-rpc request. Return response as string

    Parameters:
    url -- URL of Markov chain generator server
    crp -- string with corpus text
    dgr -- degree. Length of a generator key
    mwr -- maximal length of generated text (in words)

    """

    server = jsonrpclib.Server(url)
    result = server.generate(crp, dgr, mwr)
    return result.encode('latin-1', 'replace')


if __name__ == '__main__':

    try:
        url = sys.argv[1]
        crf = sys.argv[2]
        dgr = int(sys.argv[3])
        mwr = int(sys.argv[4])
    except IndexError:
        print "usage %s server_url corpus_file degree maxwords" % (sys.argv[0])
        sys.exit(1)

    with open(crf, 'r') as f:
        crp = f.read()

    print request(url, crp, dgr, mwr)
