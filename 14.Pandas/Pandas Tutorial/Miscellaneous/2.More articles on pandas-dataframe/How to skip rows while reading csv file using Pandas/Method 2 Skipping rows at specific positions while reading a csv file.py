# Importing Pandas library
import pandas as pd

# Skiping rows at specific position
df = pd.read_csv("students.csv",
				skiprows = [0, 2, 5])

# Show the dataframe
df
