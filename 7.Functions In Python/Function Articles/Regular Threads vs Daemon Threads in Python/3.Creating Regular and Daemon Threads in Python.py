import threading
import time

def regular_task():
    for i in range(5):
        print(f"Regular thread running: {i}")
        time.sleep(1)

def daemon_task():
    while True:
        print("Daemon thread running")
        time.sleep(1)

# Regular thread
t1 = threading.Thread(target=regular_task)

# Daemon thread
t2 = threading.Thread(target=daemon_task)
t2.daemon = True

t1.start()
t2.start()

t1.join()  # Main program waits for the regular thread to finish
print("Main program finished")
