# import pandas library
import pandas as pd

# dictionary
record = {
    "Name": ["Tom", "Jack", "Lucy",
             "Bob", "Jerry", "Alice",
             "Thomas", "Barbie"],

    "Marks": [9, 19, 20,
              17, 11, 18,
              5, 8],

    "Status": ["Fail", "Pass", "Pass",
               "Pass", "Pass", "Pass",
               "Fail", "Fail"]}

# converting record into
# pandas dataframe
df = pd.DataFrame(record)

# select first 3 rows
# from the dataframe
df1 = df.head(3)

# show the dataframe
df1
