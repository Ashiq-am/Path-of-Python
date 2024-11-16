# import pandas
import pandas as pd

# create dataframe
df = pd.DataFrame({'Name': ['Mukul', 'Rohan', 'Rahul',
							'Krish', 'Rohit'],
				'Course': ['BCA', 'MBA', 'MBA', 'BCA',
							'BBA'],
				'Address': ['Saharanpur', 'Mohali',
							'Saharanpur', 'Mohali',
							'Noida']})

# Display original dataframe
print("Original dataframe")
print(df)

# Display last index value of dataframe
# iloc[-1] is return the last element of
# all columns in DataFrame.
print("value of last index column")
print(df.iloc[-1])
