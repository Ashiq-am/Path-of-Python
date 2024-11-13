def heapify(self, arr):
    self.heap = arr
    for i in reversed(range(len(self.heap) // self.k)):
        self._bubble_down(i)
