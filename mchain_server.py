# --*- coding: utf-8 -*-

import base64

import tornado.ioloop
import tornado.web

from tornadorpc.json import JSONRPCHandler

from mchain import Mchain

def require_basic_auth(handler_class):

    def wrap_execute(handler_execute):

        def require_basic_auth(handler, kwargs):

            auth_header = handler.request.headers.get('Authorization')

            if auth_header is None or not auth_header.startswith('Basic '):
                handler.set_status(401)
                handler.set_header('WWW-Authenticate', 'Basic realm=Restricted')
                handler._transforms = []
                handler.finish()
                return False

            auth_decoded = base64.decodestring(auth_header[6:])
            username, password = auth_decoded.split(':', 2)
            return True

        def _execute(self, transforms, *args, **kwargs):

            if not require_basic_auth(self, kwargs):
                return False
            return handler_execute(self, transforms, *args, **kwargs)

        return _execute

    handler_class._execute = wrap_execute(handler_class._execute)
    return handler_class

@require_basic_auth
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
    application.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
