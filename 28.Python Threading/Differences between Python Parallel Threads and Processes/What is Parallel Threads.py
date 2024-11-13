import threading

def GFG():
    for i in range(5):
        print(i)
# Create multiple threads
threads = []
for _ in range(3):
    thread = threading.Thread(target=GFG)
    threads.append(thread)
    thread.start()
# Wait for all threads to complete
for thread in threads:
    thread.join()
