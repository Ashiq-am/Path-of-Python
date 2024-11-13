class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.items:
            return self.items[0]
        else:
            raise IndexError("Queue is empty. No front element.")


# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
front_element = queue.front()
print(front_element)
