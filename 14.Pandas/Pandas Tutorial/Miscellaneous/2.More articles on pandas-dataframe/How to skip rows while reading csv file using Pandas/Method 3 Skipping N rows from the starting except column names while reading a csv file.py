# Importing Pandas library
import pandas as pd

# Skiping 2 rows from start
# except the coulmn names
df = pd.read_csv("students.csv",
				skiprows = [i for i in range(1, 3) ])

# Show the dataframe
df
