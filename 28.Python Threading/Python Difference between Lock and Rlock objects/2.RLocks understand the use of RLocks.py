import threading


# initializing the shared resource
geek = 0

# creating a Lock object
lock = threading.Lock()

# the below thread is accessing the
# shared resource
lock.acquire()
geek = geek + 1

# This thread will be blocked
lock.acquire()
geek = geek + 2
lock.release()

# displaying the value of shared resource
print(geek)
