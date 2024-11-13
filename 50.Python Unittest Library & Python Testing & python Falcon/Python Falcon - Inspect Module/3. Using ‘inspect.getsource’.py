import falcon
import inspect

class ExampleResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Hello, World!'}

source_code = inspect.getsource(ExampleResource.on_get)
print(source_code)
