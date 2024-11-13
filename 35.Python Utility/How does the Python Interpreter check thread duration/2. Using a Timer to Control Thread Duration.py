import threading
import time

class TimedThread(threading.Thread):
    def __init__(self, duration):
        super().__init__()
        self.duration = duration

    def run(self):
        print("Thread starting")
        time.sleep(self.duration)
        print(f"Thread finished after {self.duration} seconds")

# Create and start the thread with a 3-second duration
thread = TimedThread(3)
thread.start()

# Wait for the thread to complete
thread.join()
