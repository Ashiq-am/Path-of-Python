import falcon

class SecureCookieResource:
	def on_get(self, req, resp):
		# Set a secure cookie named 'session_id' with the value 'abc123'
		resp.set_cookie('session_id', 'abc123', secure=True)

		# Output
		resp.status = falcon.HTTP_200
		resp.body = 'Secure cookie set successfully'


app = falcon.App()
app.add_route('/set_secure_cookie', SecureCookieResource())

# Run the Falcon application
if __name__ == '__main__':
	from wsgiref import simple_server

	# Create a simple WSGI server
	httpd = simple_server.make_server('127.0.0.1', 8000, app)

	print('Falcon app is running at http://127.0.0.1:8000/set_secure_cookie')

	# Start the server
	httpd.serve_forever()
