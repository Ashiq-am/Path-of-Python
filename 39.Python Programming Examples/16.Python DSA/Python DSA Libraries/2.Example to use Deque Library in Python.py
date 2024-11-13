from collections import deque

# Creating a deque
my_queue = deque()

# Adding elements to the queue
my_queue.append(1) # Adds to the right end
my_queue.appendleft(2) # Adds to the left end

# Removing elements from the queue
element = my_queue.pop() # Removes and returns from the right end
element = my_queue.popleft() # Removes and returns from the left end

# Other methods available in deque include: extend, extendleft, rotate, etc.
