from intervaltree import IntervalTree, Interval

# Create an interval tree
tree = IntervalTree()

# Add intervals to the tree
tree.add(Interval(1, 5))
tree.add(Interval(3, 8))
tree.add(Interval(6, 10))
tree.add(Interval(12, 15))

# Query intervals that overlap with a given range
query_range = (4, 7)
result_intervals = tree.search(*query_range)

print("Intervals that overlap with the query range:", result_intervals)

# Iterate over the result intervals and print their start and end points
print("Start and end points of the overlapping intervals:")
for interval in result_intervals:
	print("Start:", interval.begin, "End:", interval.end)
