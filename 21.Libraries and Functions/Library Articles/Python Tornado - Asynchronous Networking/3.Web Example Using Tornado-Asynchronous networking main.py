import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", message="Hello, Tornado!",
                    host=self.request.host)

    def post(self):
        self.redirect("/about")


class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("about.html")

    def post(self):
        self.redirect("/")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/about", AboutHandler),

    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Tornado server running at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
