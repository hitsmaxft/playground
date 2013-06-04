import unittest

from tests.basic_eval import BasicEvalTestCase

def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BasicEvalTestCase))
    return suite
