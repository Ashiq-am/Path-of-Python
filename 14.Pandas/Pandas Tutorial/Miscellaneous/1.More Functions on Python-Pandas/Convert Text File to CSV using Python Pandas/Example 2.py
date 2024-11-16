# importing pandas library
import pandas as pd

# reading given csv file
# and creating dataframe
websites = pd.read_csv("GeeksforGeeks.txt",header = None)

# adding column headings
websites.columns = ['Name', 'Type', 'Website']

# store dataframe into csv file
websites.to_csv('GeeksforGeeks.csv', index = None)
