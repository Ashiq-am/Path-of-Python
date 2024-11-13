class Service:
    def do_something(self):
        print("Service is doing something")

class Client:
    def __init__(self):
        self.service = None

    def set_service(self, service: Service):
        self.service = service

    def perform_task(self):
        self.service.do_something()

# Dependency Injection
service = Service()
client = Client()
client.set_service(service)
client.perform_task()
