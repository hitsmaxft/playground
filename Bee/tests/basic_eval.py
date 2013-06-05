import unittest
from Bee.Expr.Eval import Eval
from json import loads,dumps

class BasicEvalTestCase(unittest.TestCase):
    def setUp(self):
        from Bee.Request import Request
        r = Request()
        content = r.get('http://s.taobao.com/search?q=t&debug=true&test=1')
        #text = open("./tests/sample.json").read()
        #self._json = content
        self._data = content
        self.e = Eval(self._data)

    def getData(self):
        pass

    def test_eval_node_value(self):
        self.assertEquals(True, self.e.runStringOnce("data.view.navigation.type = 0", self._data))

    def test_eval_node_len(self):
        self.assertEquals(True, self.e.runStringOnce('entry.recommendbottom.DATA.*widgetName = "recommendBottom"', self._data))

    #def test_eval_node_len(self):
        #self.assertEquals(True,self.e.runStringOnce("#data.view.navigation.prop.20000 = 2", self._data))

    #def test_eval_value_gt(self):
        #self.assertEquals(True,self.e.runStringOnce("data.view.navigation.type > 2", self._data))

    #def test_eval_value_gt(self):
        #self.assertEquals(True,self.e.runStringOnce("data.view.navigation.prop.20000 @ 4992", self._data))

    #def test_eval_regex_match(self):
        #self.assertEquals(True, self.e.runStringOnce('"helloword" ~ r"hell[o]word"'))