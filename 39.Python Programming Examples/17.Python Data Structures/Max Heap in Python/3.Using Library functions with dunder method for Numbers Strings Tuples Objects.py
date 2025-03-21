"""
Python3 program to implement MaxHeap Operation
with built-in module heapq
for String, Numbers, Objects
"""
from functools import total_ordering
import heapq

# why total_ordering: https://www.geeksforgeeks.org/python-functools-total_ordering/


@total_ordering
class Wrapper:
	def __init__(self, val):
		self.val = val

	def __lt__(self, other):
		return self.val > other.val

	def __eq__(self, other):
		return self.val == other.val


# Working on exiting list of int
heap = [10, 20, 400, 30]
wrapper_heap = list(map(lambda item: Wrapper(item), heap))

heapq.heapify(wrapper_heap)
max_item = heapq.heappop(wrapper_heap)

# This will give the max value
print(f"Top of numbers are: {max_item.val}")

# Working on existing list of str
heap = ["this", "code", "is", "wonderful"]
wrapper_heap = list(map(lambda item: Wrapper(item), heap))
heapq.heapify(wrapper_heap)

print("The string heap elements in order: ")
while wrapper_heap:
	top_item = heapq.heappop(wrapper_heap)
	print(top_item.val, end=" ")

# This code is contributed by Supratim Samantray (super_sam)
