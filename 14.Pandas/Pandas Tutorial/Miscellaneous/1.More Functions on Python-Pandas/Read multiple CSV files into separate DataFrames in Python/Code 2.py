# import module
import pandas as pd

# assign dataset names
list_of_names = ['crime','username']

# create empty list
dataframes_list = []

# append datasets into teh list
for i in range(len(list_of_names)):
	temp_df = pd.read_csv("./csv/"+list_of_names[i]+".csv")
	dataframes_list.append(temp_df)
