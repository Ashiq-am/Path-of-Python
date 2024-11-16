# import pandas library
import pandas as pd

# read a csv file
df = pd.read_csv('Example.csv', na_values = "not available")

# show the dataframe
print(df)
