from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Using the Queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)
front_item = queue.peek()
print("Front item:", front_item)
print("Is queue empty?", queue.is_empty())
print("Queue size:", queue.size())
