import unittest
from Bee.Request import SimpleRequest

class BasicRequestTestCase(unittest.TestCase):

    def test_simple_request(self):
        r = SimpleRequest()
        content = r.get('http://s.taobao.com/search?q=t&debug=true&test=1', {})
        self.assertTrue("recommendBottom" == content.get("entry", {}).get("recommendbottom", {}).get("DATA", {}).get("*widgetName"))
