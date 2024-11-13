class Service:
    def do_something(self):
        print("Service is doing something")

class Client:
    def perform_task(self, service: Service):
        service.do_something()

# Dependency Injection
service = Service()
client = Client()
client.perform_task(service)
