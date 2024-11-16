# pandas pckage is required
import pandas as pd

# declaring a data frame with three rowsand three columns
data = [['Mallika', 23, 'Student'], [
	'Yash', 25, 'Tutor'], ['Abc', 14, 'Clerk']]

# creating a pandas data frame
data_frame = pd.DataFrame(data, columns=['Name', 'Age', 'Profession'])

# printing data frame
print("Data frame")
print(data_frame)

# printing row header
print("Row header")

print(list(data_frame.columns))
