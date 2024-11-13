import falcon
from falcon_cors import CORS

# Create a Falcon application instance
app = falcon.App()

# Configure CORS middleware
cors = CORS(allow_all_origins=True)
app.add_middleware(cors.middleware)

# Define your Falcon resource classes and routes


class MyResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Hello, CORS!'}


app.add_route('/hello', MyResource())

# Run the Falcon application
if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('localhost', 8002, app)
    print('Serving on localhost:8002...')
    httpd.serve_forever()
