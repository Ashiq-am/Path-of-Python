import logging
import tornado.ioloop
import tornado.web
from tornado.log import enable_pretty_logging


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Tornado with Logging Support!")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    # Enable colored log output in the terminal
    enable_pretty_logging()
    logging.info("Tornado server starting on port 8888...")
    tornado.ioloop.IOLoop.current().start()
