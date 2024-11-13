import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Tornado!")

class ApiHandler(tornado.web.RequestHandler):
    def get(self):
        data = {"message": "Hello, Tornado!", "status": "success"}
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(data))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api", ApiHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8001)
    print("Tornado server is running at http://localhost:8001")
    tornado.ioloop.IOLoop.current().start()
