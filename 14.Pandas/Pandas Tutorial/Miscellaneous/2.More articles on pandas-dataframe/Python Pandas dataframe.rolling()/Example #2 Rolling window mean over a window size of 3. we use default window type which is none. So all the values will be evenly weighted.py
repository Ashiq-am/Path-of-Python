# importing pandas as pd
import pandas as pd

df = pd.read_csv("apple.csv", parse_dates =["date"], index_col ="date")

# close is the column on which
# we are performing the operation
# mean() function finds the mean over each window
df.close.rolling(3).mean()
