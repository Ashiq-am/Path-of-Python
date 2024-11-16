# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("nba.csv")

# replacing team name and adding spaces in start and end
new = data["Team"].replace("Boston Celtics", "  Boston Celtics  ").copy()

# checking with custom removed space string
new.str.lstrip() == "Boston Celtics  "