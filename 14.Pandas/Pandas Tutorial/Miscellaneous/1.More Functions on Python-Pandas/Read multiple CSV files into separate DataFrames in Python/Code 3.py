# import modules
import os
import pandas as pd

# assign path
path, dirs, files = next(os.walk("./csv/"))
file_count = len(files)
# create empty list
dataframes_list = []

# append datasets to the list
for i in range(file_count):
    temp_df = pd.read_csv("./csv/" + files[i])
    dataframes_list.append(temp_df)

# display datsets
for dataset in dataframes_list:
    display(dataset)
