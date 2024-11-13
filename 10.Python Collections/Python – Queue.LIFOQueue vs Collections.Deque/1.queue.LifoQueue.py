# Import required module
import queue

# Initialize LIFO Queue
LIFOq = queue.LifoQueue(maxsize=3)

# qsize() give the maxsize of
# the Queue
print(LIFOq.qsize())

# Data Inserted as 5->9->1->7,
# same as Queue
LIFOq.put(1)
LIFOq.put(2)
LIFOq.put(3)

# Displaying if the Queue is full
print("Full: ", LIFOq.full())

# Displaying size of queue
print("Size: ", LIFOq.qsize())

# Data will be accessed in the
# reverse order Reverse of that
# of Queue
print(LIFOq.get())
print(LIFOq.get())
print(LIFOq.get())

# Displaying if the queue is empty or not
print("Empty: ", LIFOq.empty())
