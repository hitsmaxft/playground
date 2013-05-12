#!/usr/bin/env python2
#
# usage: python imagebam.py ""

import sys
import urllib2
import re
from BeautifulSoup import BeautifulSoup
import os

def openurl(url):
    try:
        f = urllib2.urlopen(url)
    except:
        print "Error: unable to fetch the page " + url.strip()
        sys.exit(1)
    return f

def download(url,filename, chunk_size=1048576):
    try:
        filein = urllib2.urlopen(url)
    except urllib2.URLError, msg:
        print "Urllib2 error (%s)" % msg
        sys.exit(1)
    except socket.error, (errno, strerror):
        print "Socket error (%s) for host %s (%s)" % (errno, host, strerror)
        sys.exit(1)

    fileout = open(filename, "wb")

    while True:
        try:
            bytes = filein.read(chunk_size)
            fileout.write(bytes)
        except IOError, (errno, strerror):
            print "I/O error (%s): %s" % (errno, strerror)
            sys.exit(1)

        if bytes == "":
            break

    filein.close()
    fileout.close()

def main():
    url = sys.argv[1]
    print "Opening"
    f = openurl(url)
    soup = BeautifulSoup(f)

    print "Finding images"
    images = soup.findAll('a', target=True)
    print " Found %s images." % str(len(images)-1)

    print "Downloading images"
    i = 1
    for image in images:
        f = openurl(image['href'])
        soup = BeautifulSoup(f)
    ## links = soup.findAll('a')
        imageRef = soup.find('img',src=re.compile(".*jpg$"))

    ## import pdb; pdb.set_trace()

## if i == 1 or i == len(images)-1:
## downloadLink = links[4]['href']
## elif i == len(images):
## downloadLink = None
## else:
## downloadLink = links[5]['href']
        if imageRef != None:
            filename = '%02d-%s.jpg'% (i, imageRef['id'])
        downloadLink = imageRef['src']
        ## filename = '.'.join([str(i),'jpg'])
        print " Downloading image %d of %d: %s" % (i,len(images)-1,filename)
        #download(downloadLink,filename)
        os.system('wget %s %s'% (downloadLink, filename))
        i += 1

if __name__ == '__main__':
    main()
