import falcon
from waitress import serve


class HelloWorldResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200 # Set the HTTP status code to 200 OK
        resp.text = "Hello, Falcon World!" # The response body

# Create a Falcon app
app = falcon.App()

# Add a route that maps the URL path to the HelloWorldResource
app.add_route('/hello', HelloWorldResource())

if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=8000)
