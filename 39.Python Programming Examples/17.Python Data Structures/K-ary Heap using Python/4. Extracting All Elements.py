class KaryHeap:
    def __init__(self, k=2):
        self.k = k
        self.heap = []

    def parent(self, i):
        return (i - 1) // self.k

    def children(self, i):
        return [self.k * i + j + 1 for j in range(self.k) if self.k * i + j + 1 < len(self.heap)]

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return min_value

    def sift_down(self, i):
        while True:
            smallest = i
            for child in self.children(i):
                if self.heap[child] < self.heap[smallest]:
                    smallest = child
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def build_heap(self, array):
        self.heap = array[:]
        for i in range(len(self.heap) // self.k, -1, -1):
            self.sift_down(i)

    def decrease_key(self, i, new_value):
        if new_value > self.heap[i]:
            raise ValueError("New value is greater than the current value")
        self.heap[i] = new_value
        self.sift_up(i)
# Create a ternary heap (3-ary heap)
heap = KaryHeap(k=3)

# Insert elements
heap.insert(10)
heap.insert(4)
heap.insert(7)
heap.insert(3)
heap.insert(5)

print("Heap before extracting all elements:", heap.heap)

# Extract all elements
extracted_elements = []
while heap.heap:
    extracted_elements.append(heap.extract_min())

print("Extracted elements in sorted order:", extracted_elements)
print("Heap after extracting all elements:", heap.heap)
