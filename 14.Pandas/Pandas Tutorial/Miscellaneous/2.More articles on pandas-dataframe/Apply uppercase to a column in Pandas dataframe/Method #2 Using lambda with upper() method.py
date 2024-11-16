# Import pandas package
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace=True)

# Applying upper() method on 'College' column
data['College'].apply(lambda x: x.upper()).head(10)
