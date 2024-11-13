import falcon


class ExampleResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Example GET Response'
