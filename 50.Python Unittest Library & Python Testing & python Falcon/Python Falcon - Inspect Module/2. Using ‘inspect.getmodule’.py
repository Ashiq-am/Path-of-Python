import falcon
import inspect

class ExampleResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Hello, World!'}

module = inspect.getmodule(ExampleResource)
print(module)
