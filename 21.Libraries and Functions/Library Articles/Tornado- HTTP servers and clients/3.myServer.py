import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("form.html")

    def post(self):
        name = self.get_body_argument("name")
        email = self.get_body_argument("email")
        if name and email:
            self.write(f"Form Successfully submitted! Name: {name} Email: {email}")
        else:
            self.write("Please fill the name and email.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], template_path="templates")

if __name__ == "__main__":
    app = make_app()
    print("Tornado server is running at http://localhost:8003")
    app.listen(8003)
    tornado.ioloop.IOLoop.current().start()
