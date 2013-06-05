import unittest

from tests.basic_eval import BasicEvalTestCase
from tests.test_request import BasicRequestTestCase

def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BasicEvalTestCase))
    suite.addTest(unittest.makeSuite(BasicRequestTestCase))
    return suite
