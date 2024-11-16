import pandas as pd

x = pd.DataFrame([["A", 100, "D"], ["B", 200, "E"], ["C", 100, "F"]],
                 columns=["Name", "Salary", "Department"])

# initialize the indx as a list
indx = []

# Searching in whole column
for i in range(len(x.Name)):
    if 100 == x.Salary[i]:
        # indx will store all the tuples having
        # that particular value in column.
        indx.append(i)

    # Final Dataframe having tuples
df = pd.DataFrame()

# this will append all tuples to the final
# dataframe.
for indexes in indx:
    df = df.append(x.iloc[indexes])

df = x.where(x.Salary == 100)

# It will remove NaN rows.
df.dropna()
