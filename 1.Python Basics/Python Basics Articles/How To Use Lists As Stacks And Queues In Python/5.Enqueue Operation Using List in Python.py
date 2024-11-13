class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)


# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.items)
