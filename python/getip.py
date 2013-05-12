#!/usr/bin/env python
import os
import re
page_text = os.popen('curl -s getip.dyndns.org').read()
page_text.encode('utf-8')
str_match=re.search("[\d.]+",page_text)
if str_match:
	print(str_match.group(0),)
else : print('localhost')
