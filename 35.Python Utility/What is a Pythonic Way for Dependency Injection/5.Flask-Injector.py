#pip install flask flask-injector


from flask import Flask
from flask_injector import FlaskInjector
from injector import inject, singleton

class Service:
    def do_something(self):
        print("Service is doing something")

class Client:
    @inject
    def __init__(self, service: Service):
        self.service = service

    def perform_task(self):
        self.service.do_something()

def configure(binder):
    binder.bind(Service, to=Service, scope=singleton)

app = Flask(__name__)

@app.route('/')
def index(client: Client):
    client.perform_task()
    return 'Task performed'

FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run()
