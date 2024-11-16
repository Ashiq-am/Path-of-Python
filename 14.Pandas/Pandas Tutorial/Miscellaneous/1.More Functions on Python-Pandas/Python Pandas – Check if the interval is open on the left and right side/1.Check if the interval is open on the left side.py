import pandas as pd

# creating intervals
# setting the closed parameter to
# 'neither'.it is also called open interval
# an interval open on both sides
# is of the form a<x<b
interval1 = pd.Interval(2, 10, closed='neither')

print(interval1.closed)
print(interval1.closed_left)
