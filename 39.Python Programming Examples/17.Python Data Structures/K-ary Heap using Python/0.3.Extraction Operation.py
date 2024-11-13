def extract_min(self):
    if len(self.heap) == 0:
        return None
    if len(self.heap) == 1:
        return self.heap.pop()

    root = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._bubble_down(0)
    return root

def _bubble_down(self, index):
    smallest = index
    for i in range(1, self.k + 1):
        child_index = self.child(index, i - 1)
        if child_index < len(self.heap) and self.heap[child_index] < self.heap[smallest]:
            smallest = child_index
    if smallest != index:
        self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
        self._bubble_down(smallest)
