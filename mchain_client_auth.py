# -*- coding: utf-8 -*-

import urllib2

jsonrpc_req = """
{"jsonrpc": "2.0", "params": ["Poszla Dyna srac na tory", 1], "id": "0ccl8o0s", "method": "generate"}
"""

req = urllib2.Request(url='http://localhost:5000', data=jsonrpc_req)
req.add_header('Authorization', 'Basic enVtaWNybTp0WTVZSmY5MWFpUFJYRzA=')

f = urllib2.urlopen(req)
print f.read()
