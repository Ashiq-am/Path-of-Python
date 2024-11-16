''''''
'''In this example, a series is created and some values are passed to the series through a for loop. 
After that, the series is passed in pandas insert function to append series in the Data frame with 
values passed.'''

# importing pandas module
import pandas as pd

# creating a blank series
Type_new = pd.Series([])

# reading csv file
data = pd.read_csv("pokemon.csv")

# running a for loop and asigning some values to series
for i in range(len(data)):
    if data["Type"][i] == "Grass":
        Type_new[i] = "Green"

    elif data["Type"][i] == "Fire":
        Type_new[i] = "Orange"

    elif data["Type"][i] == "Water":
        Type_new[i] = "Blue"

    else:
        Type_new[i] = data["Type"][i]

    # inserting new column with values of list made above
data.insert(2, "Type New", Type_new)

# list output
data.head()
