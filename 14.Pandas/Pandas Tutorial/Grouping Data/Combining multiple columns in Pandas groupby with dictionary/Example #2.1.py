# Create the groupby_dict
groupby_dict = {"Week_1_Viewers":"Total_Viewers",
		"Week_2_Viewers":"Total_Viewers",
		"Week_3_Viewers":"Total_Viewers",
		"Movies":"Movies" }

df = df.set_index('ID')
df = df.groupby(groupby_dict, axis = 1).sum()
print(df)
