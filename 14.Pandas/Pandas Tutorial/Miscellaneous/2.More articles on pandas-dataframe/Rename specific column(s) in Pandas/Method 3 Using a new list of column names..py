# Creating a list of new columns
df_cols = ["Student Name",
		"Marks Obtained",
		"Roll Number"]

# printing the columns
# before renaming
print(df.columns)

# Renaming the columns
df.columns = df_cols

# printing the columns
# after renaming
print(df.columns)
