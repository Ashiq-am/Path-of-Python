def insert(self, value):
    self.heap.append(value)
    self._bubble_up(len(self.heap) - 1)

def _bubble_up(self, index):
    parent_index = self.parent(index)
    while index > 0 and self.heap[index] < self.heap[parent_index]:
        self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
        index = parent_index
        parent_index = self.parent(index)
