# Importing Pandas library
import pandas as pd

# Skiping 2 rows from end
df = pd.read_csv("students.csv",
				skipfooter = 5,
				engine = 'python')

# Show the dataframe
df
