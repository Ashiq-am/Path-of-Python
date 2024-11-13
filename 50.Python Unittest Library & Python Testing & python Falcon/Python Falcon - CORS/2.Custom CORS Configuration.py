import falcon
from falcon_cors import CORS

# Create a Falcon application instance
app = falcon.App()

# Configure CORS middleware with custom settings
cors = CORS(
    allow_origins_list=['http://localhost:3000'],
    allow_all_methods=True,
    allow_all_headers=True
)
app.add_middleware(cors.middleware)

# Define a Falcon resource class
class GreetingResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Welcome to the Falcon CORS example!'}

# Add a route to the resource
app.add_route('/policy', GreetingResource())

# Run the Falcon application
if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('localhost', 8000, app)
    print('Serving on localhost:8000...')
    httpd.serve_forever()
