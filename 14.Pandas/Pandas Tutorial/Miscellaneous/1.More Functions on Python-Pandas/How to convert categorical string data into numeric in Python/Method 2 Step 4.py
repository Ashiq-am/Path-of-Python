# removing the column 'Purchased' from df
# as it is of no use now.
df.drop("Purchased", axis=1, inplace=True)

# Appending the array to our dataFrame
# with column name 'Purchased'
df["Purchased"] = label

# printing Dataframe
df
