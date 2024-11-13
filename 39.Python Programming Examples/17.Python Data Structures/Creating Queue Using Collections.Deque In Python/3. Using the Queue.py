# Create a queue instance
queue = Queue()

# Enqueue elements into the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Dequeue an element from the queue
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)

# Peek at the front of the queue
front_item = queue.peek()
print("Front item:", front_item)

# Check if the queue is empty
print("Is queue empty?", queue.is_empty())

# Get the size of the queue
print("Queue size:", queue.size())
