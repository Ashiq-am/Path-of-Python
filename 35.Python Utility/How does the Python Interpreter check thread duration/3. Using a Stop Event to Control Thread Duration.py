import threading
import time

def monitored_task(stop_event):
    print("Monitored thread starting")
    while not stop_event.is_set():
        print("Thread is running...")
        time.sleep(1)
    print("Monitored thread stopping")

# Create an event object to signal the thread to stop
stop_event = threading.Event()

# Create and start the monitored thread
monitored_thread = threading.Thread(target=monitored_task, args=(stop_event,))
monitored_thread.start()

# Allow the thread to run for 5 seconds
time.sleep(5)

# Signal the thread to stop
stop_event.set()

# Wait for the thread to complete
monitored_thread.join()

print("Thread has been stopped")
