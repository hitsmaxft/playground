# coding=utf-8
__author__ = 'qixiang'


import unittest
from Bee.Server.TornadoInterface import SingleDb


class DbQueryTestCase(unittest.TestCase):
    def setUp(self):
        self.db=SingleDb
        self.db.connectDb({})

    def testCon(self):
        case = self.db.querySql("SELECT * FROM bee_case")
        self.assertTrue( len(case) > 0)

    def testGetId(self):
        case = self.db.getById(2)

        from Bee.Request import SimpleRequest
        from Bee.Expr import Eval
        import json
        r = SimpleRequest()
        test_data = r.get(case["input"])
        script = Eval(debug=0)
        r = script.runStringOnce(case["expect"], test_data, prefix="entry.%s" % case['refmodules'])

        self.assertTrue(r)
    def testAll(self):
        cases = self.db.getAll()

        from Bee.Request import SimpleRequest
        from Bee.Expr import Eval
        import json
        r = SimpleRequest()
        script = Eval(debug=0)

        for case in cases:
            if input not in case:
                print(case)
                return
            test_data = r.get(case["input"])
            r = script.runStringOnce(case["expect"], test_data, prefix="entry.%s" % case['refmodules'])
            self.assertTrue(r)