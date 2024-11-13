import falcon
from resources.example_resource import ExampleResource

api = falcon.API()
example_resource = ExampleResource()
api.add_route('/example', example_resource)
