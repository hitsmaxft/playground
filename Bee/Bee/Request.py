#!/usr/bin/env python2

import json
import urllib,re

class TestRequest(object):
    """
    parse remote data from page with json data
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
            self.__doReq(url)
        )

    def __doReq(self, url, params = {}):
        """
        make request for url, return data

        """

        #TODO error handling for retry
        html_body = urllib.urlopen(url).read().decode("gb18030")
        return html_body

    def get(self, key=None, default=None):
        result = self.cache[key] \
            if key in self.cache else \
            self.makeReq(key)

        if result == None:
            return default

    def _parse(self, html_content=""):
        """
        parse json object from html content with regex expr

        doctests
        >>> r = TestRequest() ; r.get('http://s.taobao.com/search?q=t&debug=true&test=1')
        """
        reg_exp = re.compile("<test>(.*)</test>")
        content = reg_exp.search(html_content)

        if None == content:
            return None

        self.cache[self.url] = json.loads(content.groups()[0])
        return self.cache[self.url]
