#pip install dependency-injector


from dependency_injector import containers, providers

class Service:
    def do_something(self):
        print("Service is doing something")

class Client:
    def __init__(self, service: Service):
        self.service = service

    def perform_task(self):
        self.service.do_something()

class Container(containers.DeclarativeContainer):
    service = providers.Singleton(Service)
    client = providers.Factory(Client, service=service)

container = Container()
client = container.client()
client.perform_task()
