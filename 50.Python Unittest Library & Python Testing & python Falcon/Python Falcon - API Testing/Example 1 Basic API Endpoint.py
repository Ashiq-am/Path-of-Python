import falcon

class HelloWorldResource:
	def on_get(self, req, resp):
		resp.status = falcon.HTTP_200
		resp.media = {'message': 'Hello, Falcon!'}

# Create a Falcon application
app = falcon.App()

# Add a route for the HelloWorldResource
app.add_route('/hello', HelloWorldResource())

if __name__ == '__main__':
	from wsgiref import simple_server

	# Run the Falcon app
	host = 'localhost'
	port = 8000
	httpd = simple_server.make_server(host, port, app)
	print(f'Starting Falcon app on http://{host}:{port}')
	httpd.serve_forever()
