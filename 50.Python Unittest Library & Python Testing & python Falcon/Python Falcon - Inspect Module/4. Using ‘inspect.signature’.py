import falcon
import inspect

class ExampleResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Hello, World!'}

sig = inspect.signature(ExampleResource.on_get)
print(sig)
