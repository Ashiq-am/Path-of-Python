from queue import Queue

# Initializing a queue
que = Queue()

# Adding elements to a queue
que.put(1)
que.put(2)
que.put(3)
que.put(4)
que.put(5)

# display the queue
print("Initial queue")
print(que.queue)

# casting into the list
li = list(que.queue)
print("\nConverted into the list")
print(li)
