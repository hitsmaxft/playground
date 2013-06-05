import unittest
from Bee.Expr.Eval import Eval
from json import loads,dumps

class BasicEvalTestCase(unittest.TestCase):
    def setUp(self):
        text = open("./tests/sample.json").read()
        self._json = text
        self._data = loads(text)
        self.e = Eval(self._data)

    def getData(self):
        pass

    def test_eval_node_value(self):
        self.assertEquals(True, self.e.runStringOnce("&JSON:" + self._json + "data.view.navigation.type = 3", self._data))

    #def test_eval_node_len(self):
        #self.assertEquals(True,self.e.runStringOnce("#data.view.navigation.prop.20000 = 2", self._data))

    #def test_eval_value_gt(self):
        #self.assertEquals(True,self.e.runStringOnce("data.view.navigation.type > 2", self._data))

    #def test_eval_value_gt(self):
        #self.assertEquals(True,self.e.runStringOnce("data.view.navigation.prop.20000 @ 4992", self._data))

    #def test_eval_regex_match(self):
        #self.assertEquals(True, self.e.runStringOnce('"helloword" ~ r"hell[o]word"'))
