class Database:
    def connect(self):
        print("Connecting to the database...")

class Service:
    def __init__(self, database: Database):
        self.database = database

    def execute(self):
        self.database.connect()
        print("Service is executing...")

class Application:
    def __init__(self, service: Service):
        self.service = service

    def run(self):
        self.service.execute()

# Dependency Injection
database = Database()
service = Service(database)
app = Application(service)
app.run()
