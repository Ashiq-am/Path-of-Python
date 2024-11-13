import falcon
from http.cookies import SimpleCookie

class CookieResource:
	def on_get(self, req, resp):
		# Simulated client request with cookie
		request_headers = {'Cookie': 'username=JohnDoe; session_id=abc123'}

		# Parse the cookie from the request headers
		cookie = SimpleCookie()
		cookie.load(request_headers.get('Cookie', ''))

		# Accessing individual cookies
		username = cookie.get(
			'username').value if 'username' in cookie else None
		session_id = cookie.get(
			'session_id').value if 'session_id' in cookie else None

		resp.text = f'Username: {username}\nSession ID: {session_id}'

def main():
	app = falcon.App()
	app.add_route('/cookie', CookieResource())

	# Run the Falcon application
	from wsgiref import simple_server
	httpd = simple_server.make_server('127.0.0.1', 8000, app)
	print('Serving on http://127.0.0.1:8000')
	httpd.serve_forever()


if __name__ == '__main__':
	main()
