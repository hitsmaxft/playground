import web
from Bee.Expr.Eval import Eval
from json import loads,dumps


urls = (
    '/', 'index'
)
class index:
    def GET(self):
        return "<form method=\"post\"><input name=\"content\"/><input type=\"submit\" /></form>"
    def POST(self):
        input = web.input()
        content = input.get('content')
        print(content)

        text = open("./tests/sample.json").read()
        self._data = loads(text)
        e = Eval(self._data)
        return dumps({"result": e.runStringOnce(content)})

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()