# importing the pandas library
import pandas as pd

# initializing the series
ser = pd.Series(['g', 'e', 'e', 'k', 's'])

# iterating the series until the iterator reaches the end of the series
for i in range(0, ser.size):
	if i == ser.size-1:
		# printing the last element i.e, size of the series-1
		print("The last element in the series using loop is : ", ser[i])

# calculating the length of the series
len = ser.size

# printing the last element i.e len-1 as indexing starts from 0
print("The last element in the series by calculating length is : ", ser[len-1])
