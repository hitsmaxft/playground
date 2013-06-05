import unittest

from Bee.Expr.Eval import Eval
from json import loads,dumps

from Bee.Request import Request

class BasicRequestTestCase(unittest.TestCase):

    def test_simple_request(self):
        r = Request()
        content = r.get('http://s.taobao.com/search?q=t&debug=true&test=1')
        self.assertTrue("recommendBottom" == content["entry"]["recommendbottom"]["DATA"]["*widgetName"])