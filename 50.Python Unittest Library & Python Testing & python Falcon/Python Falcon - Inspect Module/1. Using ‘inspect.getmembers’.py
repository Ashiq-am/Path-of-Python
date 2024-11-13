import falcon
import inspect

class ExampleResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Hello, World!'}

api = falcon.API()
api.add_route('/example', ExampleResource())

members = inspect.getmembers(ExampleResource)
for member in members:
    print(member)
