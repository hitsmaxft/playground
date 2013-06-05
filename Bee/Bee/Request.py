#!/usr/bin/env python2

import json

class Request(object):
    """
    parse remote data from web page
    simple for cache and retry , expire data  with time and use times

    load json from special uri, with cache support
    """
    def __init__(self, options = {}):
        self.url = ""
        self.format = "json"
        self.cache = {}
        for k in options:
            setattr(self , k , options[k])
        pass

    def makeReq(self, url):
        return self._parse(
            url, self.__doReq(url)
        )

    def __doReq(self, url):
        return None
        return '{"data": {"nav": {"type": 3}}}'

    def get(self, key):
        return self.cache[key] \
            if key in self.cache else \
            self.makeReq(key)

    def _parse(self, url="", content=""):
        """
        >>> r = Request() ; r.get('http://s.taobao.com/search?q=t&debug=true&test=1')
        {u'data': {u'nav': {u'type': 3}}}
        """
        import urllib,re
        html_body = urllib.urlopen(url).read().decode("gb18030")
        reg_exp = re.compile("<test>(.*)</test>")
        content = reg_exp.search(html_body)
        self.cache[self.url] = json.loads(content.groups()[0])
        return self.cache[self.url]
