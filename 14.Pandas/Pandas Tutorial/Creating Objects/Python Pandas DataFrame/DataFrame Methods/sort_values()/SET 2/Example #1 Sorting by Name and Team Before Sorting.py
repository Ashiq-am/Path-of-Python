#importing pandas package
import pandas as pd

#making data frame from csv file
data=pd.read_csv("nba.csv")

#sorting data frame by Team and then By names
data.sort_values(["Team", "Name"], axis=0,
				ascending=True, inplace=True)

#display
data
