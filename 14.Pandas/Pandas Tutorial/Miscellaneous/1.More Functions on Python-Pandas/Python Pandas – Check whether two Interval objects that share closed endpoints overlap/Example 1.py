# importing pandas library
import pandas as pd

# Creating two closed intervals that
# share the endpoint
Interval1 = pd.Interval(1, 5, closed='both')
Interval2 = pd.Interval(5, 10, closed='both')

# printing the intervals
print("Interval1 :", Interval1)
print("Interval2 :", Interval2)

# display the length of both Interval1
# and Interval2 objects
print("\nInterval1 object length = ", Interval1.length)
print("\nInterval2 object length = ", Interval2.length)

# Check whether both the intervals overlap
print("do the intervals overlap ? :", Interval1.overlaps(Interval2))
