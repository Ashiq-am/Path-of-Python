''''''
'''In this example, Null rows are removed using dropna() method (All though str.swapcase() doesn’t 
throw an error for null values, but it’s a good practice to remove them to avoid errors).

After that, the case of Text in Team column have been swapped using .swapcase() method and the results 
are overwritten in the Team column itself. After that, the Data frame is displayed to view the changes 
made in the text case of Team column.'''



# importing pandas module
import pandas as pd

# making data frame csv at url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(how ='all', inplace = True)

# using swapcase() to interchange case
data["Team"] = data["Team"].str.swapcase()

# display
data
