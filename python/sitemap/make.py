#!/home/hitsmaxft/.pythonbrew/pythons/Python-2.7.3/bin/python
# encoding=utf-8

from pysitemap import SiteMap
from datetime import datetime
from langconv import ConverterHandler
import urllib

def genLoc(filePath):
    c = open(filePath)
    conv = ConverterHandler('zh-hant')
    word = u'女装连衣裙'
    for x in xrange(100000):
        line = word
        if len(line):
            keyword = ''
            keyword = urllib.quote(conv.convert(line.strip()).encode('utf-8'))

            if not len(keyword):
                continue
            url = 'http://example.com/?q=%s' % keyword
            yield url

site = SiteMap()

for kw in genLoc('./sample.txt'):
    site.add(
            loc=kw,
            lastmod=datetime.now(),
            changefreq='weekly')

feed = open('./sitemap.xml', 'w')

feed.write(site.to_string())
feed.close()
