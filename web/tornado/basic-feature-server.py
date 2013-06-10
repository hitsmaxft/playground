#!/usr/bin/env python2
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.template

simple_tpl='''
<!doctype html>
<html lang="en">
<head><title>page -- {{title}}</title></head>
<link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet">
<body>
<div class="navbar">
    <div class="navbar-inner">
    <a class="brand" href="#">{{ title }}</a>
    </div>
</div>

<div class="container">
    <div class="row">


    <h1>{{title}}</h1>
    <div class="hero-unit">
        <h2>Tornado Hello World</h2>
    </div>
        <h1>simple list</h1>
        <ul>
        {% for word in word_list %}
                <li>{{ word }}</li>
        {% end %}
        </ul>
    <pre>
    {% from pprint import pformat %}
    {{ pformat(sample_dict) }}
    </pre>

    </div>
</div>

<footer class="footer">
    <div class="container">
        <p>Powered by Tornado & bootstrap</p>
    </div>
</footer>

<script type="text/javascript">
window.setTimeout(function(){
    window.location.href=window.location.href
}, 10000)
</script>
</body>
</html>'''

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        tpl = tornado.template.Template(simple_tpl)
        self.write(tpl.generate(
            title='simple hello wrold'
            , word_list = ['simple', 'hello', 'world', '<script>alert(1)</script>' ]
            , sample_dict = {
                'title': 'hello'
                , 'content' : [ 'yep', 'opps', 'blahblah' ]
                }
            ))

application = tornado.web.Application([
    (r"/", MainHandler),
    ], debug=True)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
