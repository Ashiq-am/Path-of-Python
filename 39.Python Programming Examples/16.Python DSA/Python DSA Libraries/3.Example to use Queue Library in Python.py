from queue import Queue

# Creating a queue
my_queue = Queue()

# Adding elements to the queue
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

# Removing elements from the queue
# Removes and returns the first element added (FIFO)
element = my_queue.get()
print(element)

# Checking if the queue is empty
print(my_queue.empty())

# Getting the size of the queue
print(my_queue.qsize())

# Other methods available in Queue include: empty,
# qsize, full, task_done, join, etc.
