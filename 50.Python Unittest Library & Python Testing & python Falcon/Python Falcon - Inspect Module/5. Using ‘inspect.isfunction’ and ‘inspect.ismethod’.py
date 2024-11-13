import falcon
import inspect

class ExampleResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Hello, World!'}

print(inspect.isfunction(ExampleResource.on_get))  # True
print(inspect.ismethod(ExampleResource.on_get))    # False
