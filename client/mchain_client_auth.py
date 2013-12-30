# -*- coding: utf-8 -*-

import urllib2
import json
import sys
import uuid
import argparse
import base64


def build_request(ct):

    jsonrpc_req = {}
    jsonrpc_req['jsonrpc'] = "2.0"
    jsonrpc_req['params'] = [corpus_txt, 1]
    jsonrpc_req['id'] = str(uuid.uuid1())
    jsonrpc_req['method'] = 'generate'

    return json.dumps(jsonrpc_req)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("corpusfile")
    parser.add_argument("server_url")
    parser.add_argument("username")
    parser.add_argument("password")

    args = parser.parse_args()

    upass_encoded = base64.encodestring('%s:%s' % (args.username, args.password))

    with open(args.corpusfile, 'r') as f:
        corpus_txt = f.read()

    jsonrpc_req_txt = build_request(corpus_txt)

    req = urllib2.Request(url=args.server_url, data=jsonrpc_req_txt)
    req.add_header('Authorization', "Basic %s" % (upass_encoded))

    f = urllib2.urlopen(req)
    print f.read()
