# import pandas
import pandas as pd

# create dataframe
df = pd.DataFrame({'Name': ['Mukul', 'Rohan',
							'Rahul', 'Krish',
							'Rohit'],
				'Address': ['Saharanpur', 'Mohali',
							'Saharanpur', 'Mohali',
							'Noida']})

# Display original dataframe
print(" Original dataframe ")
print(df)

# Display last index value of dataframe
# iloc[-1] is return the last element of
# all columns in DataFrame.
print(" last index is ", df.index[-1])
