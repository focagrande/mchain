# -*- coding: utf-8 -*-

import urllib2
import json
import sys

corpus_fname = './corpus/corpus_5.txt'

with open(corpus_fname, 'r') as f:
    corpus_txt = f.read()

jsonrpc_req = {}
jsonrpc_req['jsonrpc'] = "2.0"
jsonrpc_req['params'] = [corpus_txt, 1]
jsonrpc_req['id'] = '0ccl8o0s'
jsonrpc_req['method'] = 'generate'

jsonrpc_req_txt = json.dumps(jsonrpc_req)

req = urllib2.Request(url='http://localhost:5000', data=jsonrpc_req_txt)
req.add_header('Authorization', 'Basic enVtaWNybTp0WTVZSmY5MWFpUFJYRzA=')

f = urllib2.urlopen(req)
print f.read()
