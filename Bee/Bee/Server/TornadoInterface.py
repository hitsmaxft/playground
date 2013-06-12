#!/usr/bin/env python2
import tornado.web
from tornado.httputil import HTTPHeaders
import tornado.template
import tornado.httpclient as httpclient

from Bee.Expr import Eval
from Bee.Request import SimpleRequest

from json import loads,dumps
from urllib import urlopen
import re

from multiprocessing import Pool

ParsePool = Pool(10)

req = SimpleRequest()
http_client = httpclient.AsyncHTTPClient()


class MainHandler(tornado.web.RequestHandler):
    """
    async HttpRequest handler for BeeLangQueue
    """

    def setHeader(self, param={}):
        header=HTTPHeaders()
        for k,v in param:
            self.add_header(k, v)

    @tornado.web.asynchronous
    def get(self):
        """
        for test only
        :return:
        """
        url = "http://127.0.0.1:8888/test_data"
        self.async_get(url)


    def async_get(self, url):
        http_client.fetch(url, self.handle_request)

    def handle_request(self, response):
        """
        request handler
        """
        if response.error:
            self.write("Error:", response.error)
        else:
            data = req.parse(response.body, 'utf-8')
            self.write( data )
            #self.write(response.body)
        self.finish()

    def post(self, url, rules):
        data = req.get(url)
        result = Eval(data).runStringOnce(rules)
        return dumps({"result": result})
