import pandas as pd

x = pd.DataFrame([["A", 100, "D"], ["B", 200, "E"], ["C", 100, "F"]],
                 columns=["Name", "Salary", "Department"])

# Searching in whole column
for i in range(len(x.Name)):
    if 200 == x.Salary[i]:
        # indx will store the tuple having that
        # particular value in column.
        indx = i

    # below line will print that tuple
x.iloc[indx]
