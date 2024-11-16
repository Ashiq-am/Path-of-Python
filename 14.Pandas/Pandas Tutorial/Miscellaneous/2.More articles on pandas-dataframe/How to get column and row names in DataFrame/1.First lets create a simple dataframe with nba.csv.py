# Import pandas package
import pandas as pd

# making data frame
data = pd.read_csv("nba.csv")

# calling head() method
# storing in new variable
data_top = data.head(10)

# display
data_top
