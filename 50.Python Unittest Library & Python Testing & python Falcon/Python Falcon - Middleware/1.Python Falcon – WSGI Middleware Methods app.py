import falcon
from wsgiref import simple_server
from middleware import SampleWSGIMiddleware
from resources import SampleResource

# Create a Falcon App instance and add middleware
app = falcon.App(middleware=SampleWSGIMiddleware())

# Add the resource to the Falcon API
app.add_route('/', SampleResource())

# Run the Falcon application
if __name__ == '__main__':
    # Create a WSGI server instance
    httpd = simple_server.make_server('127.0.0.1', 8000, app)

    # Start the server
    print('Falcon server starting on port 8000...')
    httpd.serve_forever()
