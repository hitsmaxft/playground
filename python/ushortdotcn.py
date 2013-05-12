#!/usr/bin/env python3

from http.client import HTTPConnection
from urllib.parse import urlparse
import sys
from socket import gethostbyname

def unshort(url):
    parsed = urlparse(url)
    req = HTTPConnection(gethostbyname(parsed.netloc))
    req.request('HEAD', parsed.path)
    response = req.getresponse()
    if response.status//100 == 3 and response.getheader('Location'):
        print(response.status)
        return response.getheader('Location')
    else:
        print(response.status)
        return url

if(len(sys.argv)>1):
    print("Original url : {!s}".format(unshort(sys.argv[1])));
