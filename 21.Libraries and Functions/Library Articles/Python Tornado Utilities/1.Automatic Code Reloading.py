import tornado.ioloop
import tornado.web
from tornado.autoreload import start, watch


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Tornado with Automatic Code Reloading!")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    # Start monitoring for code changes
    watch("app.py")
    # Start the Tornado I/O loop with automatic reloading enabled
    start()
    tornado.ioloop.IOLoop.current().start()
