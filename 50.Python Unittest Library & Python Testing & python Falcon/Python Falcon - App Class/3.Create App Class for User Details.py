import falcon

class UserResource:
    def on_get(self, req, resp):
        # Logic to fetch and return user data from database
        resp.media = {
            'users': [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]}

class UserProfileResource:
    def on_get(self, req, resp, user_id):
        # Logic to fetch and return user profile data based on user_id
        resp.media = {'user_id': user_id, 'profile': {
            'email': 'alice@example.com', 'age': 30}}

app = falcon.App()
app.add_route('/users', UserResource())
app.add_route('/users/{user_id}', UserProfileResource())

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('localhost', 8000, app)
    print('Serving on localhost:8000...')
    httpd.serve_forever()
