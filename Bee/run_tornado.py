#!/usr/bin/env python2
import tornado.httpserver
import tornado.httpclient
import tornado.ioloop
import tornado.web
import tornado.template

from Bee.Server.TestSite import TestSiteHandler
from Bee.Server.TornadoInterface import MainHandler


application = tornado.web.Application([
    (r"/api", MainHandler),
    (r"/test_data", TestSiteHandler),
    ], debug=True)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


