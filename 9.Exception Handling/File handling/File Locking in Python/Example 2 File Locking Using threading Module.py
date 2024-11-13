import threading

file_path = "example.txt"
lock = threading.Lock()

def write_to_file():
    with lock:
        with open(file_path, "a") as file:
            file.write("Data to be written\n")

# Create multiple threads to write to the file
threads = []
for _ in range(5):
    thread = threading.Thread(target=write_to_file)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()
