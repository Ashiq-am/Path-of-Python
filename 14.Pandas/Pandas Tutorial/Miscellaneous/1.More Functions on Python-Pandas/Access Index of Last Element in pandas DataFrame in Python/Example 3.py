# import pandas
import pandas as pd

# create dataframe
df = pd.DataFrame({'Name': ['sanjay', 'suresh',
							'Rahul', 'Krish',
							'vihan'],
				'Address': ['Haridwar', 'Mohali',
							'mohali', 'Mohali',
							'saharanpur']})

# Display original dataframe
print(" Original dataframe ")
print(df)

# Display last index value of 0 index column
print("last index value of 0 index column is ", df.iat[-1, 0])
