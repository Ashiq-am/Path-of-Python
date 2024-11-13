class Service:
    def do_something(self):
        print("Service is doing something")

class Client:
    def __init__(self, service: Service):
        self.service = service

    def perform_task(self):
        self.service.do_something()

# Dependency Injection
service = Service()
client = Client(service)
client.perform_task()
