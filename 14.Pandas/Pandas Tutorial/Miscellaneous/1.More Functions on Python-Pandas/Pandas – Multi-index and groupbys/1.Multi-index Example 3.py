# importing the pandas library
import pandas as pd

# making data for dataframing
data = {
    'series': ['Peaky blinders', 'Sherlock', 'The crown',
               'Queens Gambit', 'Friends'],

    'Ratings': [4.5, 5, 3.9, 4.2, 5],

    'Date': [2013, 2010, 2016, 2020, 1994]
}

# Dataframing the whole data created
df = pd.DataFrame(data)

# setting first and the second name
# as index column
df.set_index(["series", "Ratings"], inplace=True,
             append=True, drop=False)
# display the dataframe
print(df)
