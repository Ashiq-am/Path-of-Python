# importing the module
import pandas as pd

# making data frame from the csv file
dataframe = pd.read_csv("csvfile1.csv")

# using the replace() method
dataframe.replace(to_replace="Fashion",
                  value="Fashion industry",
                  inplace=True)
dataframe.replace(to_replace="Food",
                  value="Food Industry",
                  inplace=True)
dataframe.replace(to_replace="IT",
                  value="IT Industry",
                  inplace=True)

# writing the dataframe to another csv file
dataframe.to_csv('outputfile.csv',
                 index=False)
