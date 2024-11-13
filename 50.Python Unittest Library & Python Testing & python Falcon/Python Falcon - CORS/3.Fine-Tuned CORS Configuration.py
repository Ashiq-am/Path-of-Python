import falcon
from falcon_cors import CORS

# Create a Falcon application instance
app = falcon.App()

# Configure CORS middleware with fine-grained settings
cors = CORS(
    allow_origins_list=['http://localhost:3000', 'http://localhost:8080'],
    allow_methods_list=['GET', 'POST'],
    allow_headers_list=['Content-Type', 'Authorization'],
    expose_headers_list=['X-Custom-Header'],
    allow_credentials_all_origins=True
)
app.add_middleware(cors.middleware)

# Define a Falcon resource class
class CustomHeaderResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Custom header example'}

# Add a route to the resource
app.add_route('/custom-header', CustomHeaderResource())

# Run the Falcon application
if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('localhost', 8000, app)
    print('Serving on localhost:8000...')
    httpd.serve_forever()
