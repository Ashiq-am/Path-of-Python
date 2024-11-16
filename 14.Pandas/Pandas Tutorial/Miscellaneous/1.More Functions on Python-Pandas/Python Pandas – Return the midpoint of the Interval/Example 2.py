# import packages
import pandas as pd

# creating intervals
# an interval closed on both sides a<=x<=b
interval1 = pd.Interval(0, 10, closed='both')

# an open interval a<x<b. the ends aren't included.
interval2 = pd.Interval(15, 25, closed='neither')
print('interval1\'s left bound is : ' + str(interval1.left))
print('interval1\'s right bound is : ' + str(interval1.right))
print('The length of interval1 is : ' + str(interval1.length))
print('mid point of the interval1 is : '+str(interval1.mid))
print(interval1.closed)

print('interval2\'s left bound is : ' + str(interval2.left))
print('interval2\'s right bound is : ' + str(interval2.right))
print('The length of interval2 is : ' + str(interval2.length))
print('mid point of the interval1 is : '+str(interval2.mid))
print(interval2.closed)
