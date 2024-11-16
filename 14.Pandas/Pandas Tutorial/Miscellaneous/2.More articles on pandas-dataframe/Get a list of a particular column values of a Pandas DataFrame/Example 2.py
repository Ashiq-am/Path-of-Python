# import pandas library
import pandas as pd

# dictionary
dict = {'Name': ['Martha', 'Tim',
                 'Rob', 'Georgia'],
        'Marks': [87, 91,
                  97, 95]}

# create a dataframe object
df = pd.DataFrame(dict)

# show the dataframe
print(df)

# iterating over and calling
# tolist() method for
# each column
for i in list(df):
    # show the list of values
    print(df[i].tolist())
