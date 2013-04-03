# --*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from tornadorpc.json import JSONRPCHandler
from tornadorpc import private, start_server

from mchain import Mchain


class Handler(JSONRPCHandler):

    def ping(self):
        return "OK"

    def generate(self, ct, dg):
        mc = Mchain(ct, dg)
        return mc.generate()


application = tornado.web.Application([
    (r"/", Handler)
])


if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
