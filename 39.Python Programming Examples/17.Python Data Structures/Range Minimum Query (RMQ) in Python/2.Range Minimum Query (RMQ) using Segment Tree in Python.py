class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [None] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)

        # function to build the segment tree
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node + 1],
                                  self.tree[2 * node + 2])

        # function to find the minimum from start to end
    def query(self, node, start, end, left, right):
        if right < start or left > end:
            return float('inf')
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return min(self.query(2 * node + 1, start, mid, left, right),
                   self.query(2 * node + 2, mid + 1, end, left, right))


# Example usage:
arr = [5, 2, 7, 1, 9, 4, 3]
segment_tree = SegmentTree(arr)
start, end = 1, 4
print("Minimum within the range [1, 4]:", segment_tree.query(
    0, 0, len(arr) - 1, start, end))
