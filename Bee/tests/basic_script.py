import unittest
from Bee.Expr import Eval
from json import loads,dumps
from Bee import BeeLang

def wrap_rule(rule, data):
    return "~JSON:{}\n{}".format(dumps(data), rule)

class BasicScriptTestCase(unittest.TestCase):
    def setUp(self):
        from Bee.Request import TestRequest
        #r = TestRequest()
        #content = r.get('http://s.taobao.com/search?q=t&debug=true&test=1')
        content = open("./tests/sample.json").read()
        self._json = content
        self._data = loads(content)
        self.e = Eval(0)

    def getData(self):
        pass

    def test_json_global(self):
        self.assertTrue(
            self.e.runStringOnce(
                wrap_rule(
                    "data.view.navigation.type = 3\n#data.view.navigation.prop.20000 = 2",
                    self._data
                )
            )
        )

    def test_node_value2(self):
        self.assertFalse(self.e.runStringOnce(
            wrap_rule(
                "data.view.navigation.type = 0", self._data
            )))

    def test_node_len(self):
        self.assertTrue(
            self.e.runStringOnce('entry.recommendbottom.DATA.*widgetName = "recommendBottom"',
                                 self._data
            )
        )

    def test_node_len(self):
        self.assertTrue(wrap_rule(self.e.runStringOnce("#data.view.navigation.prop.20000 = 2"), self._data))

    def test_value_gt(self):
        self.assertEquals(True,self.e.runStringOnce("data.view.navigation.type > 2", self._data))

    def test_value_gt(self):
        self.assertTrue(self.e.runStringOnce("data.view.navigation.prop.20000 @ 4992", self._data))

    def test_regex_match(self):
        self.assertEquals(True, self.e.runStringOnce('"helloword" ~ r"hell[o]word"', self._data))

    def test_double_eval(self):
        self.assertTrue(
            self.e.runStringOnce(
                wrap_rule(
                    "data.view.navigation.type = 3\n#data.view.navigation.prop.20000 = 2",
                    self._data
                )
            )
        )
        self.assertTrue(self.e.runStringOnce('data.view.navigation.type = 3'))
