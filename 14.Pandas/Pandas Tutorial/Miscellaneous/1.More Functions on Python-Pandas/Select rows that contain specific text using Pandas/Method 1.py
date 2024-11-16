# importing pandas as pd
import pandas as pd

# reading csv file
df = pd.read_csv("Assignment.csv")

# filtering the rows where Credit-Rating is Fair
df = df[df['Credit-Rating'].str.contains('Fair')]
print(df)
