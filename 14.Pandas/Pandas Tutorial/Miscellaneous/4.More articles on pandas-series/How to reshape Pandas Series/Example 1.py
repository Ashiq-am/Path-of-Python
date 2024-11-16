# import pandas library
import pandas as pd

# make an array
array = [2, 4, 6, 8, 10, 12]

# create a series
series_obj = pd.Series(array)

# convert series object into array
arr = series_obj.values

# reshaping series
reshaped_arr = arr.reshape((3, 2))

# show
reshaped_arr
