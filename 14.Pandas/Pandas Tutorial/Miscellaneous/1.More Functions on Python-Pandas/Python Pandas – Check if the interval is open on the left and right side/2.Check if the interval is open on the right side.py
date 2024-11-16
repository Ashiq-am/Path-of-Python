# import packages
import pandas as pd

# creating intervals
interval1 = pd.Interval(2, 10)

# by default intervals are 'right' closed
print(interval1.closed)

print(interval1.closed_right)
