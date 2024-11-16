# pandas pckage is required
import pandas as pd

# declaring a data frame with three rowsand three columns
data_frame = pd.read_csv("test.txt")

# printing data frame
print("Original Data frame")
print(data_frame)

# adding column names
data_frame_new = pd.read_csv("test.txt", names=['A', 'B', 'C'])
print("New Data frame")
print(data_frame_new)

# printing row header
print("Row header")
print(list(data_frame_new.columns))
