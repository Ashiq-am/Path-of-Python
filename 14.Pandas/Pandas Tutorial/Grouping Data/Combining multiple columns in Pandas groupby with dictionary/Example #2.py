# importing pandas as pd
import pandas as pd

# Create dictionary with data
dict = {
	"ID":[1, 2, 3],
	"Movies":["The Godfather", "Fight Club", "Casablanca"],
	"Week_1_Viewers":[30, 30, 40],
	"Week_2_Viewers":[60, 40, 80],
	"Week_3_Viewers":[40, 20, 20] }

# Convert dictionary to dataframe
df = pd.DataFrame(dict)
print(df)
