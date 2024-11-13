import falcon

class FormSubmitResource:
	def on_post(self, req, resp):
		data = req.media
		name = data.get('name', 'Guest')
		resp.status = falcon.HTTP_200
		resp.media = {'message': f'Hello, {name}! Form submitted successfully.'}

# Create a Falcon application
app = falcon.App()

# Add a route for the FormSubmitResource
app.add_route('/submit', FormSubmitResource())

if __name__ == '__main__':
	from wsgiref import simple_server

	# Run the Falcon app
	host = 'localhost'
	port = 8000
	httpd = simple_server.make_server(host, port, app)
	print(f'Starting Falcon app on http://{host}:{port}')
	httpd.serve_forever()
