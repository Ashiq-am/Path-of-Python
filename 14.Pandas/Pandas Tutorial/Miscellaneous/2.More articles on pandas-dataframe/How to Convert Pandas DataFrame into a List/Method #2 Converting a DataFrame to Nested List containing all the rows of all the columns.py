import pandas as pd

# Creating a dictionary to store data
data = {'Name': ['Tony', 'Steve', 'Bruce', 'Peter'],
        'Age': [35, 70, 45, 20]}

# Creating DataFrame
df = pd.DataFrame(data)

# Creating an empty list
res = []

# Iterating through the columns of
# dataframe
for column in df.columns:
    # Storing the rows of a column
    # into a temporary list
    li = df[column].tolist()

    # appending the temporary list
    res.append(li)

# Printing the final list
print(res)
