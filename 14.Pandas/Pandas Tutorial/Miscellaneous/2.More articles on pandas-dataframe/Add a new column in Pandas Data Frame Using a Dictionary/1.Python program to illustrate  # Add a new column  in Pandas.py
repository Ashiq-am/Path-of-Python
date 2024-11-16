# Python program to illustrate
# Add a new column in Pandas

# Importing the pandas Library
import pandas as pd

# creating a data frame with some data values.
data_frame = pd.DataFrame([[i] for i in range(7)], columns =['data'])

print (data_frame)
