import threading
import time

def daemon_thread_task():
    for i in range(10):
        print(f"Daemon thread running: {i}")
        time.sleep(1)

# Create a daemon thread
thread = threading.Thread(target=daemon_thread_task)
thread.setDaemon(True)
thread.start()

# Main program doesn't wait for the daemon thread to finish
print("Main program completed!")
