# Import pandas package
import pandas as pd

# making data frame
data = pd.read_csv("nba.csv")

# calling head() method
# storing in new variable
data_top = data.head()

# list(data_top) or
list(data_top.index)
