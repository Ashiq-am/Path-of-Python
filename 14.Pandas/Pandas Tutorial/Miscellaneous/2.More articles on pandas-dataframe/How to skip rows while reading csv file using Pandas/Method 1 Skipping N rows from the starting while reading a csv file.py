# Importing Pandas library
import pandas as pd

# Skiping 2 rows from start in csv
# and initialize it to a dataframe
df = pd.read_csv("students.csv",
				skiprows = 2)

# Show the dataframe
df
