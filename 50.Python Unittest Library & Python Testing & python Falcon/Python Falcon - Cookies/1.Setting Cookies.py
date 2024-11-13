import falcon


class CookieResource:
	def on_get(self, req, resp):
		# Set cookies
		resp.set_cookie('username', 'JohnDoe')
		resp.set_cookie('session_id', 'abc123', max_age=3600, secure=True)

		# Output
		resp.status = falcon.HTTP_200 # Set HTTP status code
		resp.body = 'Cookies set successfully'


app = falcon.App()
app.add_route('/set_cookies', CookieResource())

# Run the Falcon application
if __name__ == '__main__':
	from wsgiref import simple_server

	httpd = simple_server.make_server('127.0.0.1', 8000, app)
	print("Server started on http://127.0.0.1:8000")
	httpd.serve_forever()
