# import pandas
import pandas as pd

# create dataframe
df = pd.DataFrame({'Name': ['Mukul', 'Rohan', 'Rahul',
							'Krish', 'Rohit'],
				'Course': ['BCA', 'MBA', 'MBA',
							'BCA', 'BBA'],
				'Address': ['Saharanpur', 'Mohali',
							'Saharanpur', 'Mohali',
							'Noida']})

# Display original dataframe
print("Original dataframe")
print(df)

# Display last index value of Address dataframe
print("last index value of Address Column: ", df['Address'].iloc[-1])
