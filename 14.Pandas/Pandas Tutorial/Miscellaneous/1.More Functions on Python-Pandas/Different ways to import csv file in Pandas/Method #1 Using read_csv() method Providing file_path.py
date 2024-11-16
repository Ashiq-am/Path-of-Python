# import pandas as pd
import pandas as pd

# Takes the file's folder
filepath = r"C:\Gfg\datasets\nba.csv"

# read the CSV file
df = pd.read_csv(filepath)

# print the first five rows
print(df.head())
