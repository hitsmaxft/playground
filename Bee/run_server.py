from web import application,input
from Bee.Expr import Eval
from Bee.Request import SimpleRequest
from json import loads,dumps
from urllib import urlopen

routers = (
    '/', 'index'
)

req = SimpleRequest()

class index:
    def GET(self):
        return "<form method=\"post\"><input name=\"content\"/><input type=\"submit\" /></form>"
    def POST(self):
        """
        get parameters from post body

        :return:
        """
        storage = input()
        rules = storage.get('rules')
        url = storage.get('url')
        data = req.get(url)
        result = Eval(data).runStringOnce(rules)
        return dumps({"result": result})

if __name__ == "__main__":
    app = application(routers, globals())
    app.run()
