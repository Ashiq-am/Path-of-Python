# pandas pckage is required
import pandas as pd

# converting csv file to data frame
data_frame = pd.read_csv("test.txt", sep='\t',
						names=['Name', 'Age', 'Profession'])


# printing data frame
print("Data frame")
print(data_frame)

# printing row header
print("Row header")
print(list(data_frame.columns))
