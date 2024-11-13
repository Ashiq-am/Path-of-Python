import falcon

class SampleResource:
    async def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Hello, ASGI Falcon Middleware!"
