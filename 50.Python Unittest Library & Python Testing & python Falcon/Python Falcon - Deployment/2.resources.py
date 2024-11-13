import falcon

class HelloResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Hello, Falcon Geeks!'}
