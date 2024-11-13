#app.py continue...

# Set up the Falcon API and add the route
app = falcon.App()
app.add_route('/secure', ResourceWithAuth())

# Run the application using the built-in WSGI server
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()
