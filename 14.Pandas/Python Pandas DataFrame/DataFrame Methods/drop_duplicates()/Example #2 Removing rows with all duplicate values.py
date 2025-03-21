"""
In this example, rows having all values will be removed.
Since the csv file isn’t having such a row, a random row is duplicated and
inserted in data frame first.

"""



# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# length before adding row
length1 = len(data)

# manually inserting duplicate of a row of row 440
data.loc[1001] = [data["First Name"][440],
                  data["Gender"][440],
                  data["Start Date"][440],
                  data["Last Login Time"][440],
                  data["Salary"][440],
                  data["Bonus %"][440],
                  data["Senior Management"][440],
                  data["Team"][440]]

# length after adding row
length2 = len(data)

# sorting by first name
data.sort_values("First Name", inplace=True)

# dropping duplicate values
data.drop_duplicates(keep=False, inplace=True)

# length after removing duplicates
length3 = len(data)

# printing all data frame lengths
print(length1, length2, length3)
