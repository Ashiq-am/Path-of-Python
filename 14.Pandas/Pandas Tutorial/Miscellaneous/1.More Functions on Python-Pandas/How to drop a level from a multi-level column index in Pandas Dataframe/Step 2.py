# Creating a multilevel index
index = pd.MultiIndex.from_tuples([("Group 1", "Group 1"),
								("Group 1", "Group 2"),
								("Group 3","Group 3")])

# Creating a pandas dataframe with
# multilevel-column indexing
df = pd.DataFrame([["Ross","Joey","Chandler"],
				["Rachel","","Monica"]],
				columns=index)

# Labelling the dataframe index.
index = df. index
index. name = "F.R.I.E.N.D.S"

# Showing the above multi-index column
# dataframe
print(df)
