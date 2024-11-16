import pandas as pd # import the pandas module

# python list of numbers
data1 = [10, 20, 50, 30, 15]

# convert the list to a pandas series
s1 = pd.Series(data1)

# creates a figure of size 20 inches wide and 10 inches high
s1.plot(figsize=(20, 10))
