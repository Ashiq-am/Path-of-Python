#importing pandas package
import pandas as pd

#making data frame from csv file
data=pd.read_csv("nba.csv")

#sorting data frame by Team, age and height
data.sort_values(["Team", "Age", "Height"], axis=0,
				ascending=[False,True,False],
inplace=True)

#display
data
