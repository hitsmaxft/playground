#!/usr/bin/env python2
# coding=utf-8
from tornado.httputil import HTTPHeaders
import tornado.template
import tornado.httpclient as httpclient
from tornado import gen

from tornado.web import asynchronous


from Bee.Expr import Eval
from Bee.Request import SimpleRequest

from json import loads,dumps
from urllib import urlopen
import re

from multiprocessing import Pool

from torndb import Connection


ParsePool = Pool(10)

req = SimpleRequest()
http_client = httpclient.AsyncHTTPClient()

class DbReader():
    """
    singleton db reader
    """
    def __init__(self):

        pass

    def getById(self, item_id, limit_count=99):
        """
        query one record by id from db
        """
        if not id:
            return None
        sql = "select * from bee_case where `id` = %(id)s limit %(limit)s " % {
                'id': item_id
                , 'limit': limit_count
            }

        result = self.db.query(sql)

        if (len(result) >0):
            return result[0]
        else:
            return None

    def getByModule(self, module_id, limit_count=999):
        sql = "select * from bee_case where `refmodules` = %(id)s limit %(limit)s " % {
                'id': module_id
                , 'limit': limit_count
            }
        return self.db.query(sql)
        pass

    def getAll(self):
        sql = "select * from bee_case"
        return self.db.query(sql)

    def querySql(self, sql):
        return self.db.query(sql)
    def connectDb(self, config):
        self.db = Connection("10.232.41.141", "mido", user='root', password='taozi_123')
        pass


SingleDb = DbReader()


class MainHandler(tornado.web.RequestHandler):
    """
    async HttpRequest handler for BeeLangQueue
    """

    def setHeader(self, param={}):
        header=HTTPHeaders()
        for k,v in param:
            self.add_header(k, v)

    @asynchronous
    def get(self):
        """
        for test only
        :return:
        """
        url = "http://127.0.0.1:8888/test_data"
        self.async_get(url)


    def async_get(self, url):
        http_client.fetch(url, self.handle_request)

    def async_request(self, url):
        http_client.fetch(url, self.handle_request)

    def handle_get(self, response):
        pass

    def handle_request(self, response):
        """
        request handler
        """
        rules = self.get_argument("rules")
        if response.error:
            self.write("Error:", response.error)
        else:
            data = req.parse(response.body, 'gb18030')
            result = Eval(data).runStringOnce(rules)
            self.write( result )
            #self.write(response.body)
        self.finish()


    @asynchronous
    @gen.engine
    def post(self, url=None, rules=None):
        url = "{}&test=true&debug=true".format(self.get_argument("url"))
        rules = self.get_argument("rules")
        node_prefix = self.get_argument("node_prefix")
        http_client.fetch(url,
                          callback=(yield gen.Callback("key")))
        response = yield gen.Wait("key")
        if response.error:
            self.write("Error:", response.error)
        else:
            if None != response.body:
                data = req.parse(response.body, 'gb18030')
                result = Eval(data, node_prefix=node_prefix, debug=0).runStringOnce(rules)
                self.write( dumps(result) )
            else:
                self.write( "ok" )

        self.finish()