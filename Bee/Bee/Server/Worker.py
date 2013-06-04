import urllib
import json
from Bee.Expr import Eval

class Worker(object):
    def __init__(self, script=""):
        self._s = script.splitlines()

    def run(self):

        url = self._s[0].strip()
        rules = self._s[1:]

        data = urllib.urlopen(url)
        if (data):
            data = json.loads(data)
            return Eval.runs(rules, data)
        return False
