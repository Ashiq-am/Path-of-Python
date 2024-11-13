import threading
import time

def regular_thread_task():
    for i in range(5):
        print(f"Regular thread is running: {i}")
        time.sleep(1)

# Create a regular thread
thread = threading.Thread(target=regular_thread_task)
thread.start()

# Main program waits for the regular thread to finish
print("Main program completed!")
thread.join()
