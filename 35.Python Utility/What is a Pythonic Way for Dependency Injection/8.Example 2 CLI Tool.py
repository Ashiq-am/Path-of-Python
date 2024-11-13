class Logger:
    def log(self, message):
        print(message)

class Task:
    def __init__(self, logger: Logger):
        self.logger = logger

    def run(self):
        self.logger.log("Task is running")

def main():
    logger = Logger()
    task = Task(logger)
    task.run()

if __name__ == '__main__':
    main()
