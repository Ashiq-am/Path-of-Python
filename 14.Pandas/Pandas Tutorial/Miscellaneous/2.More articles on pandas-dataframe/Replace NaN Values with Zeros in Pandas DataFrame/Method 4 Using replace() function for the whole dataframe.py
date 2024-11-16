# importing libraries
import pandas as pd
import numpy as np

nums = {'Student Name': [ 'Shrek', 'Shivansh', 'Ishdeep',
						'Siddharth', 'Nakul', 'Prakhar',
						'Yash', 'Srikar', 'Kaustubh',
						'Aditya', 'Manav', 'Dubey'],
		'Roll No.': [ 18229, 18232, np.nan, 18247, 18136,
					np.nan, 18283, 18310, 18102, 18012,
					18121, 18168],
		'Subject ID': [204, np.nan, 201, 105, np.nan, 204,
					101, 101, np.nan, 165, 715, np.nan],
	'Grade Point': [9, np.nan, 7, np.nan, 8, 7, 9, 10,
					np.nan, 9, 6, 8]}

# Create the dataframe
df = pd.DataFrame(nums)

# Apply the function
df = df.replace(np.nan, 0)

# print the DataFrame
df
