import pandas as pd

# creating intervals
# setting the closed parameter to 'both'.
# it is also called closed interval
# an interval closed on both sides is
# of the form a<x<b
interval1 = pd.Interval(2, 10, closed='both')

print(interval1.closed)
print(interval1.closed_left)
