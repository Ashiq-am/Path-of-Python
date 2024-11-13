class Queue:
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.append(item)

# Create a queue
queue = Queue()

# Enqueue elements
queue.enqueue("orange")
queue.enqueue("mango")
queue.enqueue("grapefruit")

# Accessing elements directly from the list is not recommended
# for queue functionality (use dequeue method instead)
print(queue.items)
