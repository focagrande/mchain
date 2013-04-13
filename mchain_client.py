# --*- coding: utf-8 -*-

import jsonrpclib

server = jsonrpclib.Server('http://localhost:5000')

corpus_fname = './corpus/corpus_5.txt'

with open(corpus_fname, 'r') as f:
    corpus_txt = f.read()

print server.ping()

result = server.generate("Poszla Dyna srac na tory", 1)
print result.encode('latin-1', 'replace')
print jsonrpclib.history.request
# print result
