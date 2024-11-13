import falcon
from http.cookies import SimpleCookie

class CookieResource:
	def on_get(self, req, resp):
		# Setting a cookie with SameSite attribute
		cookie = SimpleCookie()
		cookie['my_cookie'] = 'cookie_value'
		cookie['my_cookie']['SameSite'] = 'Strict'

		# Print the cookie
		resp.text = str(cookie)

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
