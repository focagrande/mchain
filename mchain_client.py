# --*- coding: utf-8 -*-

from jsonrpclib import Server

server = Server('http://localhost:8080')

corpus_fname = './corpus/corpus_5.txt'

with open(corpus_fname, 'r') as f:
    corpus_txt = f.read()

print server.ping()

result = server.generate(corpus_txt, 1)
# print result.encode('latin-1', 'replace')
print result
