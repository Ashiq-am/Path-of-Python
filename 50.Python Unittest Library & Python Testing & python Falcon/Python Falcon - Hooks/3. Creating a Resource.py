#app.py

# Define the resource with request handlers
class ResourceWithAuth:
    @falcon.before(auth_hook)
    def on_get(self, req, resp):
        resp.media = {'message': 'You are authenticated!'}

    @falcon.before(auth_hook)
    def on_post(self, req, resp):
        resp.media = {'message': 'Data received!'}
