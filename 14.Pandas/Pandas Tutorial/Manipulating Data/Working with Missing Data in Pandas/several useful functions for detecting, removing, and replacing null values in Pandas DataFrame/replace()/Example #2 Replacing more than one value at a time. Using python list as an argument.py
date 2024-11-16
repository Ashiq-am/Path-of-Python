''''''
'''We are going to replace team “Boston Celtics” and “Texas” with “Omega Warrior” in the ‘df’ dataframe.'''


# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("nba.csv")

# this will replace "Boston Celtics" and "Texas" with "Omega Warrior"
df.replace(to_replace =["Boston Celtics", "Texas"],
							value ="Omega Warrior")
