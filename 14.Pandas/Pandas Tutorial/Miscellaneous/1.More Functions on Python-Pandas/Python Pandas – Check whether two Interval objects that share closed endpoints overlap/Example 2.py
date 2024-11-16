# importing pandas library
import pandas as pd
Intervals = pd.arrays.IntervalArray.from_tuples(
	[(1, 6), (6, 10), (10, 15), (20, 25)], closed="both")

# Display the IntervalArray
print("Intervals_array", Intervals)

# check if the given intervals overlap with [3,16]
print(Intervals.overlaps(pd.Interval(3, 16, closed='both')))
