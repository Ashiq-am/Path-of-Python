import falcon

class HelloWorldResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/plain'
        resp.text = 'Hello, Falcon WSGI!'

# Create a Falcon application instance
app = falcon.App()

# Add a route to the HelloWorldResource
app.add_route('/hello', HelloWorldResource())

# Run the Falcon application using a WSGI server
if __name__ == '__main__':
    from wsgiref import simple_server

    # Create a WSGI server instance
    httpd = simple_server.make_server('localhost', 8000, app)
    print('Serving on localhost:8000...')
    # Start the server
    httpd.serve_forever()
