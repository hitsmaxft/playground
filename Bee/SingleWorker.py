#!/usr/bin/python2
# -*- coding: utf-8 -*-

import web
from Expr.Eval import runStringOnce

urls = (
    '/api/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name = ""):
        if not name:
            name = 'World'
            return 'Hello, ' + name + '!'
        return (runStringOnce(name))

if __name__ == "__main__":
    app.run()
