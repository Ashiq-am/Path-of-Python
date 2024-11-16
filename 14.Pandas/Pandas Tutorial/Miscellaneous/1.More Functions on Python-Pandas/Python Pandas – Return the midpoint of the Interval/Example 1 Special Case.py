# import packages
import pandas as pd

# creating 1st interval
interval1 = pd.Interval(0, 10)

print('The interval\'s left bound is : ' + str(interval1.left))
print('The interval\'s right bound is : : ' + str(interval1.right))
print('The length of the interval is : ' + str(interval1.length))
print('mid point of the interval is : ' + str((interval1.left+interval1.right)/2))
print(interval1.closed)
