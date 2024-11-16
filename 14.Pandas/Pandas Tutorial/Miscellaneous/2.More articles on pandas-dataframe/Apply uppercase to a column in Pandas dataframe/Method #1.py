# Import pandas package
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# display
data['Name'] = data['Name'].str.upper()

data.head()
