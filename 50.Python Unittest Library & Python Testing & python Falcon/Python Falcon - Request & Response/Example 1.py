import falcon

class HelloNameResource:
	def on_get(self, req, resp):
		# Retrieve the 'name' parameter from the request, defaulting to 'Guest' if not present
		name = req.params.get("name", "Guest")

		# Build the response body with a personalized greeting
		resp.text = f"Hello, {name}!"

# Create a Falcon API instance
api = falcon.App()

# Add the HelloNameResource to the API, associating it with the endpoint '/hello'
api.add_route("/hello", HelloNameResource())

if __name__ == "__main__":
	from wsgiref import simple_server

	# Set the host and port for the Falcon application
	host = "127.0.0.1"
	port = 8000

	# Create a simple WSGI server using wsgiref and serve the Falcon application
	httpd = simple_server.make_server(host, port, api)
	print(f"Serving on http://{host}:{port}")

	# Serve requests indefinitely
	httpd.serve_forever()
