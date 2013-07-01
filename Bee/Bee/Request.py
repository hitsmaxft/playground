#!/usr/bin/env python2

import json
import urllib,re

class SimpleRequest(object):
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
        return self.parse(
            self.__doReq(url)
        )

    def __doReq(self, url, params = {}):
        """
        make request for url, return data

        """
        #TODO error handling for retry
        html_body = urllib.urlopen("%s&debug=true&test=1" % url ).read()
        return html_body

    def get(self, key=None, default=None):
        useCache=True if key else False

        if useCache:
            result = self.cache[key] \
                if key in self.cache else \
                self.makeReq(key)
        else:
             result=self.makeReq(key)

        return result

    def parse(self, html_content="", enc="gb18030"):
        """
        parse json object from html content with regex expr

        doctests
        >>> r = TestRequest() ; r.get('http://s.taobao.com/search?q=t&debug=true&test=true')
        """
        reg_exp = re.compile("<test>(.*)</test>")
        content = reg_exp.search(html_content)
        if None == content:
            return None

        ref_data = content.groups()[0].decode(enc)
        return json.loads(ref_data)

