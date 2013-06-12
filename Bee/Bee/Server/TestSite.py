#!/usr/bin/env python2
import tornado.httpserver
import tornado.httpclient
import tornado.ioloop
import tornado.web
import tornado.template



class TestSiteHandler(tornado.web.RequestHandler):
    """
    simple test data
    """
    def get(self):
        simple_tpl="""{% autoescape None %}<test>{{ json_encode(data) }}</test>"""
        data={
                "nav":{
                    "type":3,
                    "prop":{
                        "20000" : ["50102","324342"],
                        "413" : ["50102","324342"],
                        }
                    }
                }
        tpl = tornado.template.Template(simple_tpl)
        self.write(tpl.generate(data=data))
