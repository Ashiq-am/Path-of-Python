# importing pandas module
import pandas as pd

# creating sample series
data = pd.Series(['a', 'b', 'c', 'd'])

# creating copy of series
new = data.copy()

# assigning new values
new[1]='Changed value'

# printing data
print(new)
print(data)
