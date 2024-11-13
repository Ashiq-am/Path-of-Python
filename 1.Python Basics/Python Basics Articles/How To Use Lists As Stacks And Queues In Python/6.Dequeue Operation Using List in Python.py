class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty. Cannot dequeue.")


# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print("Before Deque:", queue.items)
dequeued_element = queue.dequeue()
print("After Deque:", queue.items)
