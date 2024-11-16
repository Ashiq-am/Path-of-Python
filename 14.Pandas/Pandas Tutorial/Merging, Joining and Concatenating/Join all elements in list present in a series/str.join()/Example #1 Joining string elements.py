''''''
'''In this example, the str.join() method is used on Name column (Series of String). As discussed 
earlier, a string is also an array of character and hence every character of string will be joined with 
the passed separator using str.join() method.'''

# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace=True)

# joining string and overwriting
data["Name"] = data["Name"].str.join("-")

# display
data
