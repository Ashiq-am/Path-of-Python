import falcon


class SampleResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Hello, WSGI Falcon Middleware!"
