import falcon
from falcon.asgi import App as ASGIApp


class HelloWorldResource:
    async def on_get(self, req, resp):
        resp.media = {'message': 'Hello, Falcon ASGI!'}


app = ASGIApp()
app.add_route('/hello', HelloWorldResource())

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)
