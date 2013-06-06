import unittest

from tests.basic_script import BasicScriptTestCase
from tests.test_request import BasicRequestTestCase

def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BasicScriptTestCase))
    #suite.addTest(unittest.makeSuite(BasicRequestTestCase))
    return suite
