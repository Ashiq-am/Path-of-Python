import threading
import time

def thread_task():
    start_time = time.time()
    print("Thread starting")
    time.sleep(2)
    end_time = time.time()
    print(f"Thread finished in {end_time - start_time:.2f} seconds")

# Create and start the thread
thread = threading.Thread(target=thread_task)
thread.start()

# Wait for the thread to complete
thread.join()
