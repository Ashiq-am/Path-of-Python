# importing pandas library
import pandas as pd

# reading the given csv file
# and creating dataframe
account = pd.read_csv("GeeksforGeeks.txt",delimiter = '/')

# store dataframe into csv file
account.to_csv('GeeksforGeeks.csv',index = None)
