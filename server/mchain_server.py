# --*- coding: utf-8 -*-

import sys
import base64

import tornado.ioloop
import tornado.web

from tornadorpc.json import JSONRPCHandler

from mchain import Mchain


class Handler(JSONRPCHandler):

    def ping(self):
        return "OK"

    def generate(self, ct, dg, mw):
        mc = Mchain()
        return mc.generate(ct, dg, mw)


application = tornado.web.Application([
    (r"/", Handler)
])


if __name__ == "__main__":

    try:
        server_port = sys.argv[1]
    except IndexError:
        print "usage: %s port" % (sys.argv[0])
        sys.exit(1)

    application.listen(server_port)
    tornado.ioloop.IOLoop.instance().start()
