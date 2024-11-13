import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

# Define options
define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="enable debug mode", type=bool)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Tornado with Options!")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=options.debug)


if __name__ == "__main__":
    # Parse command-line options
    parse_command_line()

    # Create the Tornado application
    app = make_app()

    # Start the Tornado server
    app.listen(options.port)
    print(f"Server started on port {options.port}")

    # Start the I/O loop
    tornado.ioloop.IOLoop.current().start()
