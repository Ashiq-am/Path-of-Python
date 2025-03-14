import fcntl

file_path = "example.txt"

# Open the file in write mode
with open(file_path, "a") as file:
    # Acquire exclusive lock on the file
    fcntl.flock(file.fileno(), fcntl.LOCK_EX)

    # Perform operations on the file
    file.write("Data to be written\n")

    # Release the lock
    fcntl.flock(file.fileno(), fcntl.LOCK_UN)
