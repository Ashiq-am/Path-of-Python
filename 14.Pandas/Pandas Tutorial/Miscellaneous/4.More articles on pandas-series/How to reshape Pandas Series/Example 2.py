# import pandas library
import pandas as pd

# make an array
array = ["ankit","shaurya",
		"shivangi", "priya",
		"jeet","ananya"]

# create a series
series_obj = pd.Series(array)

print("Given Series:\n", series_obj)

# convert series object into array
arr = series_obj.values

# reshaping series
reshaped_arr = arr.reshape((2, 3))

# show
print("After Reshaping: \n", reshaped_arr)
