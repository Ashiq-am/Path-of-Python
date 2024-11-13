# myapp.py

from waitress import serve
import falcon
import json


class HelloWorldResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        message = {"message": "Hello, World!"}
        resp.text = json.dumps(message)
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON


def create_app():
    app = falcon.App()
    hello_world_resource = HelloWorldResource()
    app.add_route('/', hello_world_resource)
    return app


app = create_app()

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
